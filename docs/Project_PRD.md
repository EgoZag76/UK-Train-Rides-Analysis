# 🚆 تحليل رحلات القطارات في المملكة المتحدة — وثيقة متطلبات المنتج (PRD)

> **الإصدار:** 2.0 — نهائي  
> **التاريخ:** 22 أبريل 2026  
> **حجم الفريق:** 5 أعضاء (1 قائد + 4 أعضاء)  
> **الأدوات:** Python (Data Cleaning & Feature Engineering) → Power BI (Modeling, DAX, Dashboards)  
> **المنهجية:** تقسيم العمل (Divide & Conquer)

---

## 1. ملخص تنفيذي

### 1.1 نظرة عامة على المشروع

يحلل هذا المشروع **31,653 سجل معاملات للسكك الحديدية في المملكة المتحدة** (يناير — أبريل 2024) لاستخراج Insights تجارية عبر ثلاثة محاور استراتيجية: **Revenue Optimization** (تحسين الإيرادات)، **Operational Reliability** (الموثوقية التشغيلية)، و **Demand Intelligence** (تحليل الطلب). يجمع التحليل بين Data Engineering باستخدام Python و Dashboards التفاعلية في Power BI لتقديم منتج تحليلي متكامل لإدارة السكك الحديدية.

### 1.2 سياق العمل (Business Context)

تواجه صناعة السكك الحديدية في المملكة المتحدة تحديات متزايدة: توقعات ركاب أعلى، تكاليف تشغيلية متزايدة، والحاجة إلى استراتيجيات جدولة وتسعير مبنية على البيانات. تمثل هذه الـ Dataset نافذة فريدة مدتها 4 أشهر لتحليل سلوك المعاملات (Transaction-level behavior) واكتشاف أنماط غير مرئية في التقارير التقليدية.

### 1.3 المحاور الاستراتيجية وأهداف العمل

| المحور | الهدف | السؤال الرئيسي |
|--------|------|-------------|
| 💰 **الإيرادات (Revenue)** | تعظيم إيرادات التذاكر وتحديد فرص التسعير | ما هي المسارات وأنواع التذاكر والأوقات التي تدر أكبر إيرادات؟ وأين تُفقد الأموال؟ |
| ⏱️ **العمليات (Operations)** | تحسين الأداء في الوقت المحدد (On-Time Performance) وتقليل الإلغاءات | ما هي المسارات/المحطات الأقل موثوقية؟ وما هي العوامل المرتبطة بالتأخير؟ |
| 📈 **الطلب (Demand)** | فهم سلوك الحجز والتنبؤ بالطلب المستقبلي | متى يحجز الركاب؟ ما الذي يحرك أوقات الذروة؟ هل يمكننا التنبؤ (Forecasting) بشهر مايو 2024؟ |

### 1.4 معايير النجاح (Success Criteria)

| المقياس (Metric) | الهدف (Target) |
|--------|--------|
| Data Completeness | معالجة 100% من القيم الفارغة (Nulls)، وتحليل جميع الأعمدة الـ 17 |
| Feature Engineering | إنشاء ≥ 8 أعمدة مشتقة جديدة (Derived columns) |
| Analysis Depth | الإجابة على ≥ 20 سؤالاً تحليلياً مع Visualizations |
| Dashboard Quality | 5 صفحات تفاعلية في Power BI بتصميم متناسق |
| Forecasting | 3 نماذج تنبؤية (Predictive models) لعدد الرحلات، الإيرادات، وتوزيع الطلب |
| Documentation | Data Dictionary، تقرير تنظيف البيانات (Cleaning Report)، و Model Cards |

---

## 2. ملف البيانات (Dataset Profile)

### 2.1 البيانات الوصفية (Source Metadata)

| الخاصية | القيمة |
|----------|-------|
| **اسم الملف** | `UK Train Rides new.csv` |
| **عدد السجلات** | 31,653 معاملة |
| **عدد الأعمدة** | 17 عمود أصلي |
| **النطاق الزمني** | المشتريات: 8 ديسمبر 2023 — 30 أبريل 2024 |
| | الرحلات: 1 يناير 2024 — 30 أبريل 2024 |
| **مستوى التفصيل (Granularity)** | كل صف = معاملة تذكرة واحدة |
| **Primary Key** | `Transaction ID` (31,653 قيمة فريدة — تم التحقق منها) |

### 2.2 جرد الأعمدة (Original 17 Columns)

| # | العمود | النوع (Type) | القيم الفارغة (Nulls) | القيم الفريدة | أمثلة | ملاحظات |
|---|--------|------|-------|--------|---------------|-------|
| 1 | Transaction ID | Text | 0 | 31,653 | UUID-style | Primary Key |
| 2 | Date of Purchase | Text→Date | 0 | 128 | `2023-12-08` | يحتاج إلى Date conversion |
| 3 | Time of Purchase | Text→Time | 0 | 24,351 | `14:32:15` | Timestamp دقيق |
| 4 | Purchase Type | Categorical | 0 | 2 | `Online`, `Station` | Binary channel |
| 5 | Payment Method | Categorical | 0 | 3 | `Contactless`, `Credit Card`, `Debit Card` | — |
| 6 | Railcard | Categorical | **20,918** ⚠️ | 3 (+NaN) | `Adult`, `Disabled`, `Senior`, `NaN` | **66% null** — القيمة الفارغة = "None" |
| 7 | Ticket Class | Categorical | 0 | 2 | `Standard`, `First Class` | — |
| 8 | Ticket Type | Categorical | 0 | 3 | `Advance`, `Off-Peak`, `Anytime` | فئة التسعير (Pricing tier) |
| 9 | Price | Integer | 0 | 125 | £1 — £267 | المتوسط: £23.44، الوسيط: £11 |
| 10 | Departure Station | Categorical | 0 | 12 | `London Paddington`, `York`, إلخ | 12 محطة مغادرة |
| 11 | Arrival Destination | Categorical | 0 | 32 | `Birmingham New Street`, إلخ | 32 وجهة وصول |
| 12 | Date of Journey | Text→Date | 0 | 121 | `2024-01-01` | يحتاج إلى Date conversion |
| 13 | Departure Time | Text→Time | 0 | 96 | `11:00:00` | المغادرة المجدولة |
| 14 | Arrival Time | Text→Time | 0 | 203 | `13:30:00` | الوصول المجدول |
| 15 | Actual Arrival Time | Text→Time | 0 | 624 | `13:30:00`, `11:40:00` | وقت الوصول الفعلي |
| 16 | Journey Status | Categorical | 0 | 3 | `On Time`, `Delayed`, `Cancelled` | — |
| 17 | Refund Request | Categorical | 0 | 2 | `Yes`, `No` | — |

### 2.3 مشاكل جودة البيانات (Data Quality Issues)

| المشكلة | العمود | التأثير | الحل (Resolution) |
|-------|--------|--------|------------|
| 🔴 معدل Null مرتفع | `Railcard` | 66% null (20,918 صف) | استبدال `NaN` بـ `"None"` (الركاب بدون بطاقة خصم) |
| 🟡 اختلاف الأنواع (Type Mismatch) | `Date of Purchase`, `Date of Journey` | مخزنة كـ Text وليس Datetime | تحويلها إلى `datetime64` |
| 🟡 اختلاف الأنواع | `Time of Purchase`, `Departure Time`, `Arrival Time`, `Actual Arrival Time` | مخزنة كـ Text وليس Time | تحويلها إلى `timedelta` |
| 🟡 انحراف في السعر (Price Skew) | `Price` | انحراف لليمين (متوسط £23, أعلى £267) | التوثيق، وإنشاء فئات سعرية (Price Bands) |
| 🟢 لا توجد تكرارات (No Duplicates) | `Transaction ID` | 31,653 فريد = 31,653 صف | البيانات نظيفة من التكرار |

---

## 3. هندسة الميزات المطلوبة (Feature Engineering)

> **الفلسفة:** إنشاء أعمدة جديدة تحول البيانات الخام إلى أبعاد تحليلية. يجب أن يجيب كل عمود جديد على الأقل على سؤال تجاري واحد لا يمكن للبيانات الأصلية الإجابة عليه مباشرةً.

### 3.1 مواصفات الأعمدة الجديدة

| # | العمود الجديد (New Column) | المنطق / المعادلة (Logic) | النوع | الغرض (Purpose) |
|---|-----------|----------------|------|---------| 
| F1 | `Booking_Lead_Days` | `Date of Journey − Date of Purchase` (بالأيام) | Integer | متى يقوم الركاب بالحجز مسبقًا؟ |
| F2 | `Route` | `Departure Station + " → " + Arrival Destination` | Text | التحليل على مستوى المسار (Route-level) |
| F3 | `Delay_Minutes` | إذا كان `Journey Status = "Delayed"`: `Actual Arrival Time − Arrival Time` (بالأيام). غير ذلك: `0` | Integer | قياس شدة التأخير |
| F4 | `Delay_Category` | إذا `0` → `"On Time"`, `≤ 15` → `"Minor (≤15min)"`, `> 15` → `"Major (>15min)"` | Text | تصنيف التأخير للتحليل |
| F5 | `Journey_Duration_Min` | `Arrival Time − Departure Time` (بالدقائق) | Integer | مدة الرحلة المخطط لها |
| F6 | `Departure_Hour` | استخراج الساعة من `Departure Time` (0–23) | Integer | تحليل الذروة بالساعة |
| F7 | `Day_of_Week` | `Date of Journey.dayofweek` → `Monday..Sunday` | Text | أنماط أيام الأسبوع مقابل عطلة نهاية الأسبوع |
| F8 | `Month` | `Date of Journey.month_name()` → `January..April` | Text | تحليل الاتجاه الشهري (Monthly trend) |
| F9 | `Is_Weekend` | `Day_of_Week ∈ {Saturday, Sunday}` → `True/False` | Boolean | علم (Flag) لـ عطلة نهاية الأسبوع |
| F10 | `Time_Period` | بناءً على `Departure_Hour`: `06-09` → `"Morning Peak"`, `10-15` → `"Midday"`, `16-19` → `"Evening Peak"`, غير ذلك → `"Off-Peak"` | Text | تصنيف فترة الطلب |
| F11 | `Price_Band` | `≤10` → `"Budget"`, `≤30` → `"Standard"`, `≤60` → `"Premium"`, `>60` → `"Luxury"` | Text | تقسيم الإيرادات (Revenue segmentation) |
| F12 | `Booking_Window` | بناءً على `Booking_Lead_Days`: `0` → `"Same Day"`, `1-3` → `"Short"`, `4-7` → `"Medium"`, `8-14` → `"Long"`, `>14` → `"Very Long"` | Text | سلوك الحجز المسبق |
| F13 | `Revenue_Lost_Flag` | `Journey Status = "Cancelled"` و `Refund Request = "Yes"` → `True` | Boolean | تتبع خسائر الإيرادات (Revenue loss) |

### 3.2 قواعد التعامل مع القيم الفارغة (Null Handling Rules)

| العمود | القاعدة | كود المعالجة |
|--------|------|-----------| 
| `Railcard` | استبدال `NaN` بـ `"None"` | `df['Railcard'].fillna('None')` |
| `Delay_Minutes` | تعيين `0` للرحلات غير المتأخرة | منطق مبني في الحساب |
| بقية الأعمدة | لا توجد قيم فارغة | تم التحقق — لا يتطلب إجراء |

---

## 4. الأسئلة التحليلية المطلوبة (Analytical Questions - 20+)

### 4.1 تحليل الإيرادات (Revenue Analysis)

| # | السؤال | الشكل البياني (Primary Visual) |
|---|----------|---------------|
| R1 | ما هو إجمالي الإيرادات (Total revenue) وكيف يتجه شهرياً؟ | Line Chart |
| R2 | ما هي أفضل 10 مسارات (Top 10 routes) من حيث الإيرادات؟ | Horizontal Bar |
| R3 | كيف تختلف الإيرادات بين أنواع التذاكر (Advance vs Off-Peak vs Anytime)؟ | Grouped Column |
| R4 | ما هو تقسيم الإيرادات بين Standard و First Class؟ | Pie/Donut |
| R5 | كيف يختلف متوسط سعر التذكرة (Average ticket price) حسب المسار؟ | Scatter Plot |
| R6 | ما هو إجمالي خسارة الإيرادات المقدرة من الرحلات الملغاة المستردة؟ | KPI Card |

### 4.2 تحليل العمليات (Operations Analysis)

| # | السؤال | الشكل البياني (Primary Visual) |
|---|----------|---------------|
| O1 | ما هو معدل الأداء الإجمالي في الوقت المحدد (On-Time Performance - OTP)؟ | KPI Gauge |
| O2 | ما هي المسارات التي تعاني من أعلى معدلات التأخير؟ | Bar Chart |
| O3 | ما هو متوسط وقت التأخير بالدقائق للرحلات المتأخرة؟ | KPI Card |
| O4 | كيف يبدو توزيع التأخير عبر ساعات اليوم؟ | Heatmap/Line |
| O5 | ما هي المحطات التي تسجل أكثر عدد من الإلغاءات؟ | Bar Chart |
| O6 | هل يوجد ارتباط (Correlation) بين سعر التذكرة وحالة الرحلة (Journey Status)؟ | Box Plot |
| O7 | ما النسبة المئوية للركاب المتأخرين/الملغاة رحلاتهم الذين يطلبون استرداد أموال (Refunds)؟ | Stacked Bar |

### 4.3 تحليل الطلب (Demand Analysis)

| # | السؤال | الشكل البياني (Primary Visual) |
|---|----------|---------------|
| D1 | ما هو اتجاه حجم الرحلات اليومية عبر الفترة (Jan–Apr)؟ | Area Chart |
| D2 | أي يوم من أيام الأسبوع هو الأكثر ازدحاماً؟ | Column Chart |
| D3 | ما هي ساعة المغادرة (Departure hour) الأكثر ازدحاماً؟ | Histogram |
| D4 | كم من الوقت (أيام) يستغرقه الركاب عادةً للحجز مسبقاً؟ | Distribution Plot |
| D5 | ما هو التقسيم بين مشتريات (Online vs Station) وما اتجاهه؟ | Stacked Area |
| D6 | كيف يتوزع استخدام بطاقات الخصم (Railcard usage)؟ | Donut Chart |
| D7 | هل يوجد فرق في الطلب بين عطلة نهاية الأسبوع وأيام العمل؟ | Grouped Bar |

### 4.4 تحليلات متقاطعة (Cross-Cutting Analysis)

| # | السؤال | الشكل البياني (Primary Visual) |
|---|----------|---------------|
| X1 | ما هو مزيج (Route + Ticket Type + Class) الذي يدر أكبر قدر من الإيرادات؟ | Treemap |
| X2 | هل الركاب الذين يحجزون في وقت مبكر يحصلون على تذاكر أرخص؟ | Scatter + Trend |
| X3 | ما هي طريقة الدفع (Payment Method) المفضلة حسب قناة الشراء (Purchase channel)؟ | Stacked Bar |

---

## 5. نماذج التنبؤ (Forecasting Models)

| النموذج | المتغير المستهدف (Target Variable) | الطريقة (Method) | المدى (Horizon) |
|-------|----------------|--------|---------| 
| **Forecast 1** | عدد الرحلات الشهرية | Linear Regression + ARIMA | مايو 2024 |
| **Forecast 2** | الإيرادات اليومية | Time Series (Prophet/ARIMA) | مايو 2024 |
| **Forecast 3** | انقسام الطلب على أنواع التذاكر | Proportional Trend Extrapolation | مايو 2024 |

### ملفات التنبؤ المطلوبة للـ Dashboard

| الملف | الأعمدة | الاستخدام |
|------|---------|-------------|
| `ride_count_forecast.csv` | `Date, Predicted_Rides, Lower_CI, Upper_CI` | Power BI |
| `daily_revenue_forecast.csv` | `Date, Predicted_Revenue, Lower_CI, Upper_CI` | Power BI |
| `ticket_demand_forecast.csv` | `Date, Advance_Pct, OffPeak_Pct, Anytime_Pct` | Power BI |

---

## 6. مواصفات Power BI Dashboard

### 6.1 Data Model — Star Schema

يجب تطبيق نموذج (Star Schema) في Power BI لتجنب المشاكل في العلاقات الدائرية:
- جدول للوقت (Dim_Date)
- جدول للمحطات (Dim_Station)
- جدول للتذاكر (Dim_Ticket)
- جدول لطرق الدفع (Dim_Payment)
ترتبط جميعها بجدول الحقائق المركزي (Fact_Rides).

### 6.2 صفحات الـ Dashboard

- 📊 **الصفحة 1: ملخص تنفيذي (Executive Summary):** نظرة عامة للإدارة مع KPIs (الإجمالي، نسبة On-Time، إلخ).
- 💰 **الصفحة 2: الإيرادات (Revenue Deep Dive):** تحليل تفصيلي للإيرادات حسب المسار وفئة التذكرة ونوعها.
- ⏱️ **الصفحة 3: العمليات والموثوقية (Operations & Reliability):** تقييم جودة الخدمة، التأخيرات، ومعدلات الإلغاء، ومطالبات الاسترداد.
- 📈 **الصفحة 4: الطلب وسلوك الحجز (Demand & Booking Patterns):** تحليل أوقات الشراء والفترات الزمنية للاستباق.
- 🔮 **الصفحة 5: التنبؤات (Forecasting & Predictions):** استخدام ملفات CSV التنبؤية لتوقع الإيرادات والطلب لشهر مايو 2024.

### 6.3 نمط التصميم (Power BI Theme)

- الأساسي (الرؤوس): Navy Blue داكن (`#1B2A4A`)
- مميز 1 (للإيرادات): Teal (`#0EA5E9`)
- مميز 2 (للتأخيرات): Orange (`#F97316`)
- مميز 3 (في الوقت المحدد): Emerald (`#10B981`)
- مميز 4 (الملغاة): Red (`#EF4444`)

---

## 7. ملخص المخرجات (Deliverables Summary)

1. Dataset منقح ومهندس (`Cleaned_Data_Final.csv`)
2. Data Dictionary (`data_dictionary.md`)
3. Cleaning Report (`cleaning_report.md`)
4. Analysis Notebook (`02_analysis.ipynb`)
5. Forecasting Notebook (`03_forecasting.ipynb`)
6. Forecast CSV Files
7. Power BI Dashboard (`UK_Trains_Dashboard.pbix`)
8. Model Cards (`model_cards.md`)
9. التقرير النهائي (`final_report.md`)
10. العرض التقديمي (`presentation.pptx`)

---

> **حالة الوثيقة:** ✅ معتمدة للتنفيذ (Approved for Implementation)  
> **الخطوة التالية:** راجع `Team_Implementation_Plan.md` لمعرفة جدول التنفيذ الأسبوعي وتقسيم المهام.
