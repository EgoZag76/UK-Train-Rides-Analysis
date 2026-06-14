[ANTIGRAVITY_BRIEF.md](https://github.com/user-attachments/files/28927172/ANTIGRAVITY_BRIEF.md)
# ANTIGRAVITY_BRIEF — UK Train Rides Analysis (Repo Cleanup Pass)

> ملف توجيه لـ Antigravity. اقرأه بالكامل قبل أي تعديل.
> **نطاق شغلك = ملفات التوثيق والخطط على GitHub فقط** (`.md` / JSON / نصوص).
> **ممنوع تمامًا:** لمس `Foundation_v1_TL.pbix` أو `UK Train Rides new.csv` أو مجلد `buttons/`.
> مهام Power BI اليدوية في القسم الأخير (Appendix) — دي **مرجع للمالك (Eyad)**، **مش مهام ليك**. لا تحاول تنفيذها.

---

## 0. السياق
مشروع DEPI (Data Analysis track). Dashboard على Power BI لتحليل 31,653 معاملة قطارات بريطانية (Jan–Apr 2024).
الموديل (Star Schema) **مبني وسليم بالفعل** — مش محتاج إعادة بناء. مشكلة الـ repo الحقيقية = **توثيق متناقض ومتكرر**: سرديتان متعارضتان، 4 لوحات ألوان، وحقائق داتا غلط. مهمتك توحيد وتنظيف التوثيق.

---

## 1. حقائق الداتا المؤكدة (Ground Truth — لا تخالفها في أي ملف)
- الداتا = Maven Analytics "UK Train Rides", **31,653 صف**, **18 عمود** (مش 17).
- الـ18 عمود تشمل **`Reason for Delay`**.
- Total Revenue ≈ **£741,921**.
- Journey Status: On Time **86.8%** / Delayed **7.2%** / Cancelled **5.9%**.
- Routes: 12 محطة مغادرة × 32 وصول = **65 مسار فعلي**.
- ملاحظة تنظيف: عمود الأسباب فيه "Weather" و"Weather Conditions" منفصلين (لازم يتدمجوا)، و`Railcard` فيه null تتحول لـ "None".

---

## 2. القرارات النهائية (Single Source of Truth — طبّقها عبر كل الملفات)
- **الفريق = 4 أعضاء**: Eyad Ahmed (TL) + Ahmed Ali + Mostafa Sabry + Rawan Tarek. (لا وجود لـ "MA" ولا "5 أعضاء".)
- **المنهجية = Power BI only** (Power Query + DAX). لا Python في الـ pipeline الأساسي.
- **Forecasting = optional** عبر Power BI built-in forecast فقط (يُوصف كـ exploratory، لا ARIMA/Prophet).
- **Theme وحيد معتمد = "Azure Rail Glassmorphism" (الفاتح)**. أي theme تاني (الـ Dark "Command Center") يتأرشف.

---

## 3. المشاكل وحلولها (نفّذ بالترتيب)

### المشكلة 1 — سرديتان متناقضتان في الـ repo
**الوصف:** ملفات قديمة (5 أعضاء + Python) تعيش جنب ملفات جديدة (4 أعضاء + Power BI only). أي مراجِع هيتلخبط.
**الحل:**
- أنشئ فولدر `archive/` وانقل له: `docs/Project_PRD.md`، `docs/Team_Implementation_Plan.md`، `docs/PROJECT_OVERVIEW.md`.
- المصادر الرسمية المعتمدة: `Project_PRD.md` (الجذر)، `TEAM_WORKFLOW.md`، `New_Implementation_Plan.rtl.md`.
- امسح أي ذكر لـ "5 أعضاء" أو "MA" في الملفات الباقية واستبدله بنظام الـ4.

### المشكلة 2 — حقائق داتا غلط في التوثيق
**الوصف:** بعض الملفات تقول "17 عمود" وتتجاهل `Reason for Delay`.
**الحل:**
- وحّد عدد الأعمدة على **18** في كل الملفات.
- أضف `Reason for Delay` (Categorical) لأي جرد أعمدة.
- أضف ملاحظة Power Query: دمج "Weather"+"Weather Conditions"، واستبدال null في `Railcard` بـ "None".

### المشكلة 3 — نظام التصميم متضارب (4 لوحات ألوان)
**الوصف:** Glassmorphism فاتح vs Command Center داكن vs لوحتين قدام في PRD/Overview.
**الحل:**
- اعتمد **Azure Rail Glassmorphism (الفاتح)** المصدر الوحيد للألوان والـ Report Theme JSON.
- انقل `docs/DESIGN.md` (النسخة الداكنة) لـ `archive/`، أو ضع أعلاه ملاحظة "غير معتمد — مرجع تاريخي".
- وحّد كل ذكر للألوان في الملفات الباقية على palette الـ Glassmorphism.
- أضف ملاحظة تقنية: الـ glassmorphism في Power BI = صورة خلفية ثابتة (لا backdrop blur native).

### المشكلة 4 — Targets غير واقعية في التوثيق
**الوصف:** Revenue target = 800,000 بينما الفعلي ≈ 741,921 → الـ KPI أحمر دائمًا.
**الحل:**
- في أي ملف يذكر الـ target: استبدل 800,000 بـ target واقعي (≈ 750,000) أو What-If parameter.
- وضّح أن On-Time gauge target = 90% بينما الفعلي 86.8% (قرار سرد واعٍ).

### المشكلة 5 — specs الـ Visuals تحتاج تحديث
**الوصف:** بعض اختيارات الـ charts ضعيفة، وفيه visuals مفقودة.
**الحل (حدّث الـ specs في `TEAM_WORKFLOW.md` و `New_Implementation_Plan.rtl.md`):**
- صفحة 2 (Revenue): أعِد بُعد Route للتحليل. بدّل Treemap(Booking_Window) بـ Treemap(Route → Class → Type).
- صفحة 3 (Operations): أضف visual لـ **Reason for Delay** (Donut/Bar). بدّل Waterfall(Journey Status) بـ 100% Stacked Bar.
- صفحة 4 (Demand): اجعل الـ Scatter محوره X = Booking_Lead_Days (رقمي) لا Booking_Window المصنّف.
- أضف **Map visual واحد على الأقل** (filled/bubble للمحطات) في صفحة 1 أو 3.

---

## 4. Git — بعد التعديلات
```bash
git checkout -b repo-cleanup-pass
git add -A
git commit -m "Cleanup: unify methodology (4 members, Power BI only), correct dataset facts (18 cols + Reason for Delay), single Glassmorphism theme, realistic targets, visual spec updates"
git push -u origin repo-cleanup-pass
# افتح Pull Request للمراجعة قبل الدمج في main — لا تدمج مباشرة.
```

---

## Appendix — مهام Power BI اليدوية (مرجع للمالك فقط — NOT for the agent)

> دي داخل ملف الـ `.pbix` ولا يقدر الـ agent يلمسها. checklist لـ Eyad ينفّذه في Power BI Desktop.
> الموديل (Star Schema + role-playing + composite key لـ Dim_Ticket) **سليم بالفعل** — دي إضافات/تنظيف فقط.

- [ ] **(الأهم) إرجاع `Reason for Delay`**: راجع خطوات Power Query وتأكد إن العمود مش متشال أثناء التنظيف. ادمج "Weather"+"Weather Conditions".
- [ ] **تكملة `Dim_Date`**: أضف `Day_of_Week`, `Week_Number`, `Is_Weekend`, `Weekend_Label`. ثم Day_Name → Sort by → Day_of_Week. وأكّد **Mark as Date Table**.
- [ ] **إضافة 5 features** (Calculated Columns): `Route`, `Booking_Lead_Days` (رقمي), `Delay_Minutes` (مع معالجة عبور منتصف الليل), `Departure_Hour`, `Delay_Category`.
- [ ] **تنظيف الـ Fact**: شيل الأعمدة الوصفية المكررة (Departure Station, Arrival Destination, Ticket Class, Ticket Type, Payment Method, Railcard) من Fact_Rides بعد التأكد إن الـ visuals بتعتمد على الـ Dimensions. (احتفظ بالمفاتيح + المقاييس فقط.)
- [ ] **تصحيح الـ target**: عدّل measure الـ Revenue target لقيمة واقعية أو What-If.
- [ ] **التحقق**: افتح Matrix بسيط وقارن بالأرقام المؤكدة (Total ≈ £741,921، On-Time 86.8%).

> الأكواد (DAX) للنقط دي تتكتب في مرحلة التنفيذ — مش جزء من تخطيط النضافة الحالي.
