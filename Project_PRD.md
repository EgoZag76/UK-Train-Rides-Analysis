# 🚆 تحليل رحلات القطارات في المملكة المتحدة — وثيقة متطلبات المنتج (PRD)

> **الإصدار:** 2.1 — نهائي (تحديث الفريق والمنهجية)  
> **التاريخ:** 14 يونيو 2026  
> **حجم الفريق:** 4 أعضاء (1 قائد + 3 أعضاء)  
> **الأدوات:** Power BI Desktop (Power Query, DAX, Dashboards)  
> **المنهجية:** تقسيم العمل (Divide & Conquer) — كل عضو صفحة Power BI (سردية موحدة)

---

## 1. ملخص تنفيذي

### 1.1 نظرة عامة على المشروع

يحلل هذا المشروع **31,653 سجل معاملات للسكك الحديدية في المملكة المتحدة** (يناير - أبريل 2024) لاستخراج Insights تجارية عبر ثلاثة محاور استراتيجية: **Revenue Optimization** (تحسين الإيرادات)، **Operational Reliability** (الموثوقية التشغيلية)، و **Demand Intelligence** (تحليل الطلب). يتم تنفيذ كافة خطوات تنظيف البيانات، النمذجة (Star Schema)، وحساب المؤشرات (DAX) وبناء الـ Dashboards بالكامل داخل Power BI لتقديم منتج تحليلي متكامل لإدارة السكك الحديدية.

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
| Data Completeness | معالجة 100% من القيم الفارغة (Nulls)، وتحليل جميع الأعمدة الـ 18 (بما فيها أسباب التأخير) |
| Feature Engineering | إنشاء 4 أعمدة مشتقة جديدة (F10–F13) داخل Power BI كـ Calculated Columns |
| Analysis Depth | الإجابة على الأسئلة التحليلية المطلوبة باستخدام مرئيات Power BI |
| Dashboard Quality | 4 صفحات تفاعلية أساسية في Power BI بتصميم متناسق (Azure Rail Glassmorphism) |
| Forecasting | تفعيل التنبؤ المدمج في Power BI (Built-in Forecast) للرحلات والإيرادات كخيار استكشافي |
| Documentation | دليل بناء الـ Data Model، ودليل التصميم، ودليل البدء السريع للفريق |
| Revenue Target | تحقيق إيرادات مستهدفة واقعية بقيمة 750,000£ (الفعلي 741,921£) بدلاً من 800,000£ لتجنب إظهار المؤشر باللون الأحمر دائماً |
| On-Time Performance (OTP) | تحقيق نسبة دقة مواعيد مستهدفة 90% (الأداء الفعلي 86.8% - قرار سردي واعٍ لتوضيح فجوة الأداء) |

---

## 2. ملف البيانات (Dataset Profile)

### 2.1 البيانات الوصفية (Source Metadata)

| الخاصية | القيمة |
|----------|-------|
| **اسم الملف** | `UK Train Rides new.csv` |
| **عدد السجلات** | 31,653 معاملة |
| **عدد الأعمدة** | 18 عمود أصلي |
| **النطاق الزمني** | المشتريات: 8 ديسمبر 2023 — 30 أبريل 2024 |
| | الرحلات: 1 يناير 2024 — 30 أبريل 2024 |
| **مستوى التفصيل (Granularity)** | كل صف = معاملة تذكرة واحدة |
| **Primary Key** | `Transaction ID` (31,653 قيمة فريدة — تم التحقق منها) |

### 2.2 جرد الأعمدة (Original 18 Columns)

| # | العمود | النوع (Type) | القيم الفارغة (Nulls) | القيم الفريدة | أمثلة | ملاحظات |
|---|--------|------|-------|--------|---------------|-------|
| 1 | Transaction ID | Text | 0 | 31,653 | UUID-style | Primary Key |
| 2 | Date of Purchase | Text→Date | 0 | 128 | `2023-12-08` | تحويل إلى Date في Power Query |
| 3 | Time of Purchase | Text→Time | 0 | 24,351 | `14:32:15` | تحويل إلى Time في Power Query |
| 4 | Purchase Type | Categorical | 0 | 2 | `Online`, `Station` | Binary channel |
| 5 | Payment Method | Categorical | 0 | 3 | `Contactless`, `Credit Card`, `Debit Card` | — |
| 6 | Railcard | Categorical | **20,918** ⚠️ | 3 (+NaN) | `Adult`, `Disabled`, `Senior`, `NaN` | **66% null** — القيمة الفارغة = "None" |
| 7 | Ticket Class | Categorical | 0 | 2 | `Standard`, `First Class` | — |
| 8 | Ticket Type | Categorical | 0 | 3 | `Advance`, `Off-Peak`, `Anytime` | فئة التسعير (Pricing tier) |
| 9 | Price | Decimal | 0 | 125 | £1 — £267 | تحويل إلى Decimal في Power Query |
| 10 | Departure Station | Categorical | 0 | 12 | `London Paddington`, `York`, إلخ | 12 محطة مغادرة |
| 11 | Arrival Destination | Categorical | 0 | 32 | `Birmingham New Street`, إلخ | 32 وجهة وصول |
| 12 | Date of Journey | Text→Date | 0 | 121 | `2024-01-01` | تحويل إلى Date في Power Query |
| 13 | Departure Time | Text→Time | 0 | 96 | `11:00:00` | تحويل إلى Time في Power Query |
| 14 | Arrival Time | Text→Time | 0 | 203 | `13:30:00` | تحويل إلى Time في Power Query |
| 15 | Actual Arrival Time | Text→Time | 0 | 624 | `13:30:00`, `11:40:00` | تحويل إلى Time في Power Query |
| 16 | Journey Status | Categorical | 0 | 3 | `On Time`, `Delayed`, `Cancelled` | — |
| 17 | Refund Request | Categorical | 0 | 2 | `Yes`, `No` | — |
| 18 | Reason for Delay | Categorical | **28,291** ⚠️ | 8 (+NaN) | `Weather`, `Signal Failure`, etc. | يحتوي على أسباب التأخير أو الإلغاء. |

### 2.3 مشاكل جودة البيانات (Data Quality Issues)

| المشكلة | العمود | التأثير | الحل (Resolution) |
|-------|--------|--------|------------|
| 🔴 معدل Null مرتفع | `Railcard` | 66% null (20,918 صف) | استبدال `NaN` بـ `"None"` (الركاب بدون بطاقة خصم) في Power Query |
| 🟡 اختلاف الأنواع (Type Mismatch) | `Date of Purchase`, `Date of Journey` | مخزنة كـ Text وليس Date | تحويلها إلى نوع `Date` في Power Query |
| 🟡 اختلاف الأنواع | `Time of Purchase`, `Departure Time`, `Arrival Time`, `Actual Arrival Time` | مخزنة كـ Text وليس Time | تحويلها إلى نوع `Time` في Power Query |
| 🟡 دمج قيم متشابهة مكررة | `Reason for Delay` | وجود قيم مكررة بأسماء مختلفة مثل "Weather" و "Weather Conditions" | دمجها لتكون قيمة واحدة "Weather" في Power Query |
| 🟡 انحراف في السعر (Price Skew) | `Price` | انحراف لليمين (متوسط £23, أعلى £267) | تحويل لنوع `Decimal` في Power Query، وإنشاء فئات سعرية (Price Bands) كـ Calculated Column |
| 🟢 لا توجد تكرارات (No Duplicates) | `Transaction ID` | 31,653 فريد = 31,653 صف | البيانات نظيفة من التكرار |

---

## 3. هندسة الميزات المطلوبة (Feature Engineering)

> **الفلسفة:** إنشاء أعمدة جديدة تحول البيانات الخام إلى أبعاد تحليلية. يجب أن يجيب كل عمود جديد على الأقل على سؤال تجاري واحد لا يمكن للبيانات الأصلية الإجابة عليه مباشرةً.

### 3.1 مواصفات الأعمدة الجديدة

| # | العمود الجديد (New Column) | المنطق / المعادلة (Logic) | النوع | الغرض (Purpose) |
|---|-----------|----------------|------|---------|
| F1 | `Booking_Lead_Days` | `Date of Journey − Date of Purchase` (بالأيام) | Integer | متى يقوم الركاب بالحجز مسبقًا؟ |
| F2 | `Route` | `Departure Station + " → " + Arrival Destination` | Text | التحليل على مستوى المسار (Route-level) |
| F3 | `Delay_Minutes` | إذا كان `Journey Status = "Delayed"`: `Actual Arrival Time − Arrival Time` (بالدقائق). غير ذلك: `0` | Integer | قياس شدة التأخير |
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

### 3.2 قواعد التعامل مع القيم الفارغة والتنظيف (Null Handling & Cleaning Rules)

| العمود | القاعدة | منطق المعالجة في Power Query / DAX |
|--------|------|-----------|
| `Railcard` | استبدال `NaN` بـ `"None"` | Power Query: `Table.ReplaceValue` لـ null بـ `"None"` |
| `Reason for Delay` | دمج القيم المتشابهة | Power Query: استبدال `"Weather Conditions"` بـ `"Weather"` |
| `Delay_Minutes` | تعيين `0` للرحلات غير المتأخرة | DAX: معادلة `IF` مبنية في حساب دقائق التأخير |
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

## 5. نماذج التنبؤ (Forecasting Models) - اختياري

لضمان بقاء خط معالجة البيانات وبناء لوحة القيادة بالكامل داخل Power BI، يتم الاعتماد حصرياً على أداة التنبؤ المدمجة (Power BI Analytics Forecast) كإجراء استكشافي لتوقع الإيرادات وحجم الرحلات اليومية بدلاً من النماذج الخارجية المعقدة:

| النموذج | المتغير المستهدف (Target Variable) | الطريقة (Method) | المدى (Horizon) |
|-------|----------------|--------|---------|
| **التنبؤ بالرحلات والإيرادات** | عدد الرحلات اليومية / الإيرادات اليومية | Power BI built-in forecasting (Exponential Smoothing) | مايو 2024 (30 يوم) |

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

لوحة تحكم تفاعلية تتكون من 4 صفحات رئيسية (بالإضافة إلى إمكانية تفعيل التنبؤ في الصفحة الأولى كـ Visual Analytics):
- 📊 **الصفحة 1: ملخص تنفيذي (Executive Summary):** نظرة عامة للإدارة مع KPIs (الإيرادات، الرحلات، الموثوقية) وخريطة للمحطات.
- 💰 **الصفحة 2: الإيرادات Deep Dive (Revenue Analysis):** تحليل تفصيلي للإيرادات حسب فئة التذكرة، والمسار (Route)، وتتبع المبالغ المستردة.
- ⏱️ **الصفحة 3: العمليات والموثوقية (Operations & Reliability):** تقييم دقة المواعيد (OTP)، معدلات الإلغاء، وتفصيل أسباب التأخير (Reason for Delay).
- 📈 **الصفحة 4: الطلب وسلوك الحجز (Demand & Booking Patterns):** تحليل فترات الحجز المسبق باليوم، أوقات الذروة، وتوزيع الطلب عبر أيام الأسبوع والأشهر.

### 6.3 نمط التصميم (Power BI Theme — Azure Rail Glassmorphism)

يتم تطبيق تصميم **"Azure Rail Glassmorphism" (الفاتح)** عبر كافة الصفحات كمرجعية وحيدة لنظام التصميم:
* **الألوان الرئيسية:**
  - أزرق داكن (Deep Navy): `#003366` (للرؤوس والنصوص الرئيسية)
  - أزرق سماوي (Azure Blue): `#0078D4` (كعنصر تمييز وتفاعل)
* **الألوان الوظيفية (توزيع الأداء):**
  - في الوقت المحدد (On-Time): `#10B981` (أخضر زمردي)
  - تأخير (Delayed): `#F59E0B` (برتقالي/ذهبي دافئ)
  - ملغاة (Cancelled): `#EF4444` (أحمر ناصع)
* **مؤثرات Glassmorphism:**
  - يُعتمد على خلفية ثابتة بتصميم زجاجي (Static Background Image) حيث أن Power BI لا يدعم الـ backdrop blur بشكل أصلي.
  - الحاويات والبطاقات تكون بخلفية بيضاء شبه شفافة `rgba(255,255,255,0.85)` مع حدود بيضاء ناعمة `rgba(255,255,255,0.4)`.

---

## 7. ملخص المخرجات (Deliverables Summary)

1. ملف البيانات النظيفة (`UK Train Rides new.csv`)
2. دليل بناء الـ Data Model في Power BI (`docs/Power_BI_Modeling_Guide.md`)
3. دليل التصميم الفاتح Azure Rail Glassmorphism (`docs/DESIGN.md`)
4. خطة تنفيذ ومسار العمل للفريق (`TEAM_WORKFLOW.md`)
5. لوحة القيادة التفاعلية (`Foundation_v1_TL.pbix`)
6. دليل البدء السريع للفريق (`GETTING_STARTED.md` و `GETTING_STARTED_اول حاجه تقرأ ده.md`)

---

> **حالة الوثيقة:** ✅ معتمدة للتنفيذ (Approved for Implementation)  
> **الخطوة التالية:** راجع `docs/New_Implementation_Plan.rtl.md` لمعرفة جدول التنفيذ الأسبوعي وتقسيم المهام.
