# 🚆 خطة التنفيذ — Power BI فقط (v2 — مُراجَعة)

> **المشروع:** UK Train Rides Analysis  
> **المنهجية:** Divide & Conquer — كل عضو صفحة Power BI  
> **القاعدة الذهبية:** كل الشغل داخل Power BI. لا Python. لا Feature Engineering خارجي.  
> **الأعمدة الجديدة:** 4 فقط (F10–F13) كـ Calculated Columns + أعمدة Sort مساعدة

---

## ⚙️ المرحلة 0 — TL: إعداد الـ Foundation (يوم 1–2)

> تنتهي **قبل** أن يبدأ أي عضو.

| # | المهمة | التفاصيل |
|---|--------|----------|
| 1 | **استيراد البيانات** | Get Data → CSV → `UK Train Rides new.csv` |
| 2 | **تنظيف في Power Query** | التواريخ → `Date`، الأوقات → `Time`، الأسعار → `Decimal` |
| 3 | **معالجة Railcard Nulls** | Power Query: `Replace Values` → null → `"None"` |
| 4 | **بناء Star Schema** | 5 Dimension Tables + 1 Fact Table |
| 5 | **الأعمدة الأربعة الجديدة** | Calculated Columns (F10–F13) |
| 6 | **أعمدة Sort المساعدة** | لترتيب Day_Name و Booking_Window |
| 7 | **DAX Measures** | جميع المقاييس في مجلد `_Measures` |
| 8 | **Weekend_Label** | عمود مساعد في Dim_Date لعرض "Weekend"/"Weekday" |
| 9 | **نشر الملف** | رفع `.pbix` على GitHub |

→ **Verify:** فتح Matrix visual بسيط — لو الأرقام ظهرت صح مع Slicer، الأساس سليم.

---

### 0.1 Star Schema — جداول الأبعاد

#### Dim_Date
```dax
Dim_Date = 
ADDCOLUMNS(
    CALENDAR(DATE(2023, 12, 1), DATE(2024, 5, 31)),
    "Date_Key",      VALUE(FORMAT([Date], "YYYYMMDD")),
    "Full_Date",     [Date],
    "Day_Name",      FORMAT([Date], "dddd"),
    "Day_of_Week",   WEEKDAY([Date], 2),
    "Week_Number",   WEEKNUM([Date], 2),
    "Month_Number",  MONTH([Date]),
    "Month_Name",    FORMAT([Date], "MMMM"),
    "Quarter",       "Q" & QUARTER([Date]),
    "Year",          YEAR([Date]),
    "Is_Weekend",    IF(WEEKDAY([Date], 2) >= 6, TRUE(), FALSE()),
    "Weekend_Label", IF(WEEKDAY([Date], 2) >= 6, "Weekend", "Weekday")
)
```

> ✅ **إصلاح:** أُضيف `Full_Date` و `Weekend_Label` اللذان كانا مفقودين.

**بعد الإنشاء — Sort Orders (مهمة TL):**
- `Month_Name` → Sort By Column → `Month_Number`
- `Day_Name` → Sort By Column → `Day_of_Week`

#### Dim_Station
```dax
Dim_Station = 
DISTINCT(
    UNION(
        SELECTCOLUMNS(Fact_Rides, "Station_Name", Fact_Rides[Departure Station]),
        SELECTCOLUMNS(Fact_Rides, "Station_Name", Fact_Rides[Arrival Destination])
    )
)
```

> ✅ **إصلاح:** العلاقات ستكون على النص `Station_Name` مباشرة (لا حاجة لـ Surrogate Key لأن عدد المحطات صغير = 32).

#### Dim_Ticket
```dax
Dim_Ticket = 
DISTINCT(
    SELECTCOLUMNS(Fact_Rides, 
        "Ticket_Class", Fact_Rides[Ticket Class],
        "Ticket_Type",  Fact_Rides[Ticket Type]
    )
)
```

#### Dim_Payment و Dim_Railcard
```dax
Dim_Payment  = DISTINCT(SELECTCOLUMNS(Fact_Rides, "Payment_Method", Fact_Rides[Payment Method]))
Dim_Railcard = DISTINCT(SELECTCOLUMNS(Fact_Rides, "Railcard_Type",  Fact_Rides[Railcard]))
```

---

### 0.2 الأعمدة الأربعة الجديدة (Calculated Columns)

#### F10 — Time_Period
```dax
Time_Period = 
VAR H = HOUR(Fact_Rides[Departure Time])
RETURN SWITCH(TRUE(),
    H >= 6  && H <= 9,  "Morning Peak",
    H >= 10 && H <= 15, "Midday",
    H >= 16 && H <= 19, "Evening Peak",
    "Off-Peak"
)
```

#### F11 — Price_Band
```dax
Price_Band = 
SWITCH(TRUE(),
    Fact_Rides[Price] <= 10, "Budget",
    Fact_Rides[Price] <= 30, "Standard",
    Fact_Rides[Price] <= 60, "Premium",
    "Luxury"
)
```

#### F12 — Booking_Window
```dax
Booking_Window = 
VAR LeadDays = MAX(0, DATEDIFF(Fact_Rides[Date of Purchase], Fact_Rides[Date of Journey], DAY))
RETURN SWITCH(TRUE(),
    LeadDays = 0,   "Same Day",
    LeadDays <= 3,  "Short (1-3d)",
    LeadDays <= 7,  "Medium (4-7d)",
    LeadDays <= 14, "Long (8-14d)",
    "Very Long (>14d)"
)
```

> ✅ **إصلاح:** `MAX(0, ...)` يمنع القيم السالبة من الوقوع في "Very Long" بالخطأ.

#### F13 — Revenue_Lost_Flag
```dax
Revenue_Lost_Flag = 
IF(
    Fact_Rides[Journey Status] = "Cancelled" && Fact_Rides[Refund Request] = "Yes",
    TRUE(), FALSE()
)
```

**أعمدة Sort مساعدة (يكتبها TL فقط — ليست Features):**

```dax
-- في Fact_Rides:
Booking_Window_Sort = 
SWITCH(Fact_Rides[Booking_Window],
    "Same Day", 1, "Short (1-3d)", 2, "Medium (4-7d)", 3,
    "Long (8-14d)", 4, "Very Long (>14d)", 5
)

Time_Period_Sort = 
SWITCH(Fact_Rides[Time_Period],
    "Morning Peak", 1, "Midday", 2, "Evening Peak", 3, "Off-Peak", 4
)
```

ثم: `Booking_Window` → Sort By → `Booking_Window_Sort`  
و `Time_Period` → Sort By → `Time_Period_Sort`

---

### 0.3 DAX Measures (يكتبها TL فقط)

```dax
Total_Revenue       = SUM(Fact_Rides[Price])
Avg_Ticket_Price    = AVERAGE(Fact_Rides[Price])
Total_Rides         = COUNTROWS(Fact_Rides)

Refunded_Revenue = 
CALCULATE(SUM(Fact_Rides[Price]), Fact_Rides[Revenue_Lost_Flag] = TRUE())

On_Time_Pct = 
DIVIDE(
    CALCULATE(COUNTROWS(Fact_Rides), Fact_Rides[Journey Status] = "On Time"),
    COUNTROWS(Fact_Rides), 0
)

Cancellation_Rate = 
DIVIDE(
    CALCULATE(COUNTROWS(Fact_Rides), Fact_Rides[Journey Status] = "Cancelled"),
    COUNTROWS(Fact_Rides), 0
)

Avg_Delay_Min = 
AVERAGEX(
    FILTER(Fact_Rides, Fact_Rides[Journey Status] = "Delayed"),
    DATEDIFF(Fact_Rides[Arrival Time], Fact_Rides[Actual Arrival Time], MINUTE)
)

Revenue_by_Purchase_Date = 
CALCULATE(
    SUM(Fact_Rides[Price]),
    USERELATIONSHIP(Fact_Rides[Date of Purchase], Dim_Date[Full_Date])
)

Revenue_by_Departure = 
CALCULATE(
    SUM(Fact_Rides[Price]),
    TREATAS(VALUES(Dim_Station[Station_Name]), Fact_Rides[Departure Station])
)
```

> ✅ **إصلاحات:**
> - `Total_Revenue_Lost` → سُمّي `Refunded_Revenue` (أدق — هي الإيرادات المُستردة فعلاً)
> - `Avg_Delay_Min` → حُذف `CALCULATE` الخارجي الزائد
> - أُضيف `Revenue_by_Departure` لحل مشكلة الـ Role-Playing Dimension في صفحة 1

---

### 0.4 العلاقات (Relationships)

| من | إلى | الحالة |
|----|-----|--------|
| `Dim_Date[Full_Date]` | `Fact_Rides[Date of Journey]` | ✅ Active |
| `Dim_Date[Full_Date]` | `Fact_Rides[Date of Purchase]` | ⚪ Inactive |
| `Dim_Station[Station_Name]` | `Fact_Rides[Departure Station]` | ✅ Active |
| `Dim_Station[Station_Name]` | `Fact_Rides[Arrival Destination]` | ⚪ Inactive |
| `Dim_Ticket[Ticket_Class]+[Ticket_Type]` | `Fact_Rides` | ✅ Active |
| `Dim_Payment[Payment_Method]` | `Fact_Rides[Payment Method]` | ✅ Active |
| `Dim_Railcard[Railcard_Type]` | `Fact_Rides[Railcard]` | ✅ Active |

> جميعها **One-to-Many** + **Single Direction** فقط.

---

## 📄 توزيع الصفحات

| العضو | الصفحة | العنوان |
|-------|--------|---------|
| **MA** | 1 | Executive Summary — ملخص الإدارة |
| **MB** | 2 | Revenue Deep Dive — تفصيل الإيرادات |
| **MC** | 3 | Operations & Reliability — العمليات |
| **MD** | 4 | Demand & Booking Patterns — الطلب |

---

## 📄 صفحة 1 — MA: Executive Summary

**الهدف:** نظرة عليا على أداء الشبكة.

| # | Visual | الحقول | Measure |
|---|--------|--------|---------|
| 1 | **KPI Card** × 3 | — | `Total_Revenue`, `Total_Rides`, `On_Time_Pct` |
| 2 | **Line Chart** (Dual Axis) | `Dim_Date[Month_Name]` → X | Y1: `Total_Revenue` / Y2: `Total_Rides` |
| 3 | **Bar Chart** | `Dim_Station[Station_Name]` → Y | `Revenue_by_Departure` (Top 10) |
| 4 | **Stacked Bar** | `Dim_Date[Month_Name]` → X, `Journey Status` → Legend | `Total_Rides` |
| 5 | **Slicer** | `Dim_Date[Month_Name]` | — |
| 6 | **Slicer** | `Dim_Date[Weekend_Label]` | — |

**التصميم:** أزرق داكن + أبيض | Segoe UI | KPIs في الأعلى

---

## 📄 صفحة 2 — MB: Revenue Deep Dive

**الهدف:** تحليل مصادر الإيرادات والخسائر.

| # | Visual | الحقول | Measure |
|---|--------|--------|---------|
| 1 | **KPI Card** × 2 | — | `Refunded_Revenue`, `Avg_Ticket_Price` |
| 2 | **Stacked Bar** | `Price_Band` → X, `Month_Name` → Legend | `Total_Revenue` |
| 3 | **Matrix** + Conditional Formatting | `Ticket_Class` × `Ticket_Type` | `Total_Revenue`, `Total_Rides` |
| 4 | **Column Chart** (Filtered) | `Railcard_Type` → X (بدون "None") | `Total_Revenue` |
| 5 | **Treemap** | `Booking_Window` → Group | `Total_Revenue` |
| 6 | **Slicer** | `Price_Band` | — |
| 7 | **Slicer** | `Dim_Date[Month_Name]` | — |

**التصميم:** أخضر داكن + ذهبي | الأحمر للخسائر فقط (باعتدال)

---

## 📄 صفحة 3 — MC: Operations & Reliability

**الهدف:** قياس الموثوقية التشغيلية.

| # | Visual | الحقول | Measure |
|---|--------|--------|---------|
| 1 | **KPI Card** × 2 | — | `On_Time_Pct`, `Cancellation_Rate` |
| 2 | **Gauge** | — | `On_Time_Pct` (Target = 90%) |
| 3 | **Bar Chart** | `Dim_Station[Station_Name]` → Y | `Cancellation_Rate` |
| 4 | **Column Chart** | `Dim_Date[Month_Name]` → X | `Avg_Delay_Min` |
| 5 | **Waterfall Chart** | Journey Status categories | `Total_Rides` → On Time → Delayed → Cancelled |
| 6 | **Table** | `Departure Station` + `Arrival Destination` + `Journey Status` | `Total_Rides`, `On_Time_Pct` |
| 7 | **Slicer** | `Fact_Rides[Journey Status]` | — |

**التصميم:** رمادي + أحمر (تأخير) + أخضر (On Time) | Gauge مركزي

---

## 📄 صفحة 4 — MD: Demand & Booking Patterns

**الهدف:** فهم سلوك الحجز وأنماط الطلب.

| # | Visual | الحقول | Measure |
|---|--------|--------|---------|
| 1 | **Column Chart** | `Day_Name` → X (Sorted by Day_of_Week) | `Total_Rides` |
| 2 | **Heatmap (Matrix)** | `Month_Name` × `Day_Name` + Color Scale | `Total_Rides` |
| 3 | **Bar Chart** | `Time_Period` → Y (Sorted) | `Total_Rides` |
| 4 | **Bar Chart** | `Booking_Window` → Y (Sorted) | `Total_Rides` |
| 5 | **Scatter Chart** | X: `Booking_Window` / Y: `Avg_Ticket_Price` | Color: `Ticket Type` |
| 6 | **Slicer** | `Time_Period` | — |
| 7 | **Slicer** | `Weekend_Label` | — |

**التصميم:** بنفسجي داكن + برتقالي | Heatmap بطيف أزرق متدرج

---

## 📋 قواعد الفريق

| القاعدة | التفصيل |
|---------|---------|
| ❌ لا Python | كل العمل داخل Power BI |
| ❌ لا Calculated Columns إضافية | F10–F13 + Sort columns فقط (TL) |
| ❌ لا Measures جديدة من الأعضاء | يستخدمون measures TL الجاهزة |
| ✅ Visual Customization | كل عضو حر في تصميم صفحته |
| ✅ Conditional Formatting | Data Bars, Color Scales, Icons |
| ✅ Sync Slicers | Month_Name و Weekend_Label مشتركين |
| ✅ Page Tooltips | كل عضو ينشئ Tooltip لأبرز Visual |

---

## 📅 الجدول الزمني

| اليوم | المهمة | المسؤول |
|-------|--------|---------|
| 1–2 | Star Schema + Columns + Sort Orders + Measures | **TL** |
| 3 | رفع `Foundation_v1.pbix` على GitHub | **TL** |
| 3–5 | كل عضو يصمم صفحته | **MA, MB, MC, MD** |
| 6 | مراجعة TL + تنسيق Global Theme | **TL** |
| 7 | التسليم النهائي `UK_Trains_Dashboard.pbix` | **TL** |

---

## ✅ Checklist

- [ ] TL: Star Schema (5 Dim + 1 Fact) مع العلاقات
- [ ] TL: `Full_Date` + `Weekend_Label` موجودين في Dim_Date
- [ ] TL: Sort Orders مضبوطة (Day_Name, Month_Name, Booking_Window, Time_Period)
- [ ] TL: 4 Calculated Columns (F10–F13) + Sort columns
- [ ] TL: جميع Measures في `_Measures` (شاملة `Revenue_by_Departure`)
- [ ] MA: صفحة 1 (6 Visuals + Dual Y-Axis على Line Chart)
- [ ] MB: صفحة 2 (7 Visuals + Matrix بـ Conditional Formatting)
- [ ] MC: صفحة 3 (7 Visuals + Waterfall بدل Pie)
- [ ] MD: صفحة 4 (7 Visuals + Scatter Chart + Sort Orders)
- [ ] TL: مراجعة نهائية + Global Theme

---

## 🔴 سجل التغييرات (v1 → v2)

| # | المشكلة | الإصلاح |
|---|---------|---------|
| 1 | `Full_Date` غير معرّف في Dim_Date | ✅ أُضيف صراحةً |
| 2 | `Weekend_Label` يظهر TRUE/FALSE | ✅ أُضيف عمود "Weekend"/"Weekday" |
| 3 | Sort Orders غير مذكورة | ✅ أُضيفت لـ Day, Month, Booking_Window, Time_Period |
| 4 | `Avg_Delay_Min` بـ CALCULATE زائد | ✅ حُذف CALCULATE الخارجي |
| 5 | `Booking_Window` لا يعالج القيم السالبة | ✅ أُضيف `MAX(0, ...)` |
| 6 | Route column يتعارض مع قاعدة F10–F13 | ✅ Table يستخدم الأعمدة الأصلية مباشرة |
| 7 | Donut في صفحة 1 ضعيف لـ 3 قيم | ✅ بُدّل بـ Stacked Bar |
| 8 | Pie في صفحة 3 مكرر من صفحة 1 | ✅ بُدّل بـ Waterfall Chart |
| 9 | Line Chart صفحة 1 بدون Dual Axis | ✅ أُضيف Secondary Y-Axis |
| 10 | Railcard chart يظهر "None" كأكبر شريحة | ✅ Visual-Level Filter يستبعد "None" |
| 11 | Matrix بدون Conditional Formatting | ✅ أُضيفت Data Bars / Color Scale |
| 12 | Line Chart صفحة 4 مزدحم (180 نقطة) | ✅ بُدّل بـ Scatter Chart (Price vs Booking) |
| 13 | `Total_Revenue_Lost` اسم غير دقيق | ✅ سُمّي `Refunded_Revenue` |
| 14 | لا يوجد `Revenue_by_Departure` | ✅ أُضيف measure بـ TREATAS |

> **حالة الوثيقة:** ✅ v2 — مُراجَعة وجاهزة للتنفيذ
