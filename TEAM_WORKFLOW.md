# 🚂 دليل عمل فريق مشروع قطارات المملكة المتحدة (UK Train Rides)

أهلاً بكم يا شباب! تم الانتهاء من إعداد الملف الأساسي (`Foundation_v1.pbix`) الذي يحتوي على الـ Data Model والـ Measures الجاهزة.

## 📌 توزيع المهام وتفاصيل الصفحات

كل فرد في الفريق مسؤول عن صفحة محددة. إليكم المتطلبات **المبدئية** لكل صفحة (استخدموا الـ Measures الجاهزة في مجلد `_Measures`):

### 📄 1. MA: صفحة Executive Summary (ملخص الإدارة)
* **الهدف:** نظرة عليا على أداء الشبكة.
* **المرئيات (Visuals) المطلوبة:**
  * **3 كروت (KPI Cards):** لعرض `Total_Revenue`, `Total_Rides`, `On_Time_Pct`.
  * **Line Chart (مزدوج المحور):** المحور الأفقي: `Month_Name`، المحور الرأسي 1: `Total_Revenue`، المحور الرأسي 2: `Total_Rides`.
  * **Bar Chart:** المحور الرأسي: `Station_Name`، القيم: `Revenue_by_Departure` (أعلى 10 محطات).
  * **Stacked Bar:** المحور الأفقي: `Month_Name`، تقسيم (Legend): `Journey Status`، القيم: `Total_Rides`.
  * **Slicers:** للفلترة بـ `Month_Name` و `Weekend_Label`.
* **التصميم المقترح:** أزرق داكن وأبيض.

### 📄 2. MB: صفحة Revenue Deep Dive (تحليل الإيرادات)
* **الهدف:** تحليل مصادر الإيرادات والخسائر.
* **المرئيات (Visuals) المطلوبة:**
  * **2 كروت (KPI Cards):** لعرض `Refunded_Revenue`, `Avg_Ticket_Price`.
  * **Stacked Bar:** المحور الأفقي: `Price_Band`، تقسيم: `Month_Name`، القيم: `Total_Revenue`.
  * **Matrix:** الصفوف: `Ticket_Class`، الأعمدة: `Ticket_Type`، القيم: `Total_Revenue` و `Total_Rides` (مع إضافة Data Bars/Color Scale).
  * **Column Chart:** المحور الأفقي: `Railcard_Type` (استبعد "None" بفلتر)، القيم: `Total_Revenue`.
  * **Treemap:** التجميع: `Booking_Window`، القيم: `Total_Revenue`.
  * **Slicers:** للفلترة بـ `Price_Band` و `Month_Name`.
* **التصميم المقترح:** أخضر داكن وذهبي (مع استخدام الأحمر للخسائر فقط).

### 📄 3. MC: صفحة Operations & Reliability (العمليات والموثوقية)
* **الهدف:** قياس الموثوقية التشغيلية (تأخيرات، إلغاءات).
* **المرئيات (Visuals) المطلوبة:**
  * **2 كروت (KPI Cards):** لعرض `On_Time_Pct`, `Cancellation_Rate`.
  * **Gauge:** لعرض `On_Time_Pct` (الهدف 90%).
  * **Bar Chart:** المحور الرأسي: `Station_Name`، القيم: `Cancellation_Rate`.
  * **Column Chart:** المحور الأفقي: `Month_Name`، القيم: `Avg_Delay_Min`.
  * **Waterfall Chart:** يوضح توزيع الـ `Total_Rides` حسب الـ `Journey Status` (On Time → Delayed → Cancelled).
  * **جدول (Table):** يوضح تفاصيل المحطات (`Departure Station`, `Arrival Destination`, `Journey Status`) والقيم: `Total_Rides`, `On_Time_Pct`.
  * **Slicer:** للفلترة بـ `Journey Status`.
* **التصميم المقترح:** رمادي مع أحمر (للتأخير/الإلغاء) وأخضر (في الموعد).

### 📄 4. MD: صفحة Demand & Booking Patterns (أنماط الطلب والحجز)
* **الهدف:** فهم سلوك المسافرين وأنماط الحجز.
* **المرئيات (Visuals) المطلوبة:**
  * **Column Chart:** المحور الأفقي: `Day_Name`، القيم: `Total_Rides`.
  * **Heatmap (Matrix):** الصفوف `Month_Name`، الأعمدة `Day_Name`، القيم `Total_Rides` (باستخدام Color Scale).
  * **Bar Chart:** المحور الرأسي: `Time_Period`، القيم: `Total_Rides`.
  * **Bar Chart:** المحور الرأسي: `Booking_Window`، القيم: `Total_Rides`.
  * **Scatter Chart:** المحور الأفقي: `Booking_Window`، المحور الرأسي: `Avg_Ticket_Price`، التقسيم اللوني: `Ticket_Type`.
  * **Slicers:** للفلترة بـ `Time_Period` و `Weekend_Label`.
* **التصميم المقترح:** بنفسجي داكن وبرتقالي.

---

## 💡 الإبداع والحرية في التصميم

هذه المتطلبات هي **الأساس والمطلوب كحد أدنى**، لكن **كل شخص حر تماماً في تعديل وتطوير صفحته بالطريقة التي يراها مناسبة!** 
يمكنك إضافة أي تحسينات بصرية إضافية، استخدام ألوان وتصاميم حديثة، إضافة Tooltips، أو استبدال Visual بآخر إذا وجدت أنه يوصل الفكرة بشكل أفضل لمتخذ القرار. 

## ⚠️ شرط هام جداً عند الرفع (Commit)

لكي نتمكن من دمج العمل بسلاسة وتتبع التحسينات، **يشترط عند رفع ملفك (Upload/Push) أن تقوم بإرفاق ملاحظة واضحة (Commit Message/Note)** توضح الآتي:
1. ما هي الصفحة التي قمت بتحديثها (مثال: Page 2 - MB).
2. أبرز الإضافات أو التحسينات التي قمت بها (مثال: "تم إضافة Treemap وإضافة تنسيق شرطي للـ Matrix").

بالتوفيق للجميع، ولنخرج بلوحة تحكم (Dashboard) احترافية ومتميزة! 🚀
