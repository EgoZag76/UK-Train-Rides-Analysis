# 🚀 دليل البدء السريع لفريق العمل (Getting Started Guide)

أهلاً بكم في مشروع **UK Train Rides Analysis**! 🎉
هذا الملف مصمم عشان يسهل عليك كعضو في الفريق إنك تفهم الـ Repository (المستودع) ده بيحتوي على إيه، وتبدأ شغلك إزاي من غير أي تشتت.

---

## 📁 محتويات الـ Repository (إيه الملفات الموجودة هنا؟)

عشان تفهم المشروع بسهولة، دي أهم الملفات اللي هتحتاجها:

1. **`MD/Foundation_v1_TL.pbix`**: 
   ده ملف الـ Power BI النهائي. فيه الداتا بعد التنظيف والـ Data Modeling (Star Schema + Surrogate Keys) والأربع صفحات كاملة.

2. **`TEAM_WORKFLOW.md`**: 
   أهم ملف ليك! بيوضح دور كل واحد في الفريق بالتفصيل حسب الأداة اللي بيشتغل عليها (Power BI / Python / Excel). **لازم تقرأه أول حاجة.**

3. **`UK Train Rides new.csv`**:
   ملف البيانات الأصلي الخام — نقطة البداية لمسار الـ Python (التنظيف والـ EDA).

4. **`UK_Train_Rides_Dashboard.xlsx`**:
   داشبورد Excel مبسّطة بنفس أرقام الـ Power BI.

5. **`Project_Data.pdf`**:
   بيانات المشروع الرسمية (الاسم، الشرح، الفريق، مهام كل عضو، المحاضر).

6. **`Presentation.pptx`**:
   السلايدات اللي هنعرضها يوم المناقشة.

7. **`README.md`**:
   شرح عام عن المشروع وأهدافه.

---

## 🛠️ إزاي تبدأ شغلك؟ (حسب المسار بتاعك)

المشروع مقسّم على **3 مسارات**، كل واحد بأدواته الخاصة — مش كل الفريق بيشتغل على نفس الملف:

### 🅰️ مسار الـ Power BI (Eyad Ahmed)
1. حمّل `MD/Foundation_v1_TL.pbix` وافتحه بـ Power BI Desktop.
2. اقرأ `TEAM_WORKFLOW.md` لمعرفة تفاصيل بناء التقرير بالكامل.
3. اتبع `ADVANCED_DASHBOARD_GUIDE.md` للألوان والستايل الموحّد.

### 🅱️ مسار الـ Python (Ahmed Ali)
1. حمّل `UK Train Rides new.csv` (الداتا الخام).
2. نظّف الداتا واعمل EDA في Notebook (`feature_cleaned.ipynb`).
3. سلّم النسخة النضيفة والـ insights لباقي الفريق.

### 🅲 مسار الـ Excel (Mostafa Sabry)
1. حمّل `UK Train Rides new.csv`.
2. ابني داشبورد Excel بنفس الـ KPIs الموجودة في الـ Power BI (Total Revenue, Rides, On-Time%, Cancellation%, Avg Price).
3. تأكد إن أرقامك مطابقة تمامًا لأرقام الـ Power BI قبل التسليم.

### تسليم الشغل 🤝
كل واحد يبلّغ الـ Team Leader (إياد) لما يخلّص، وإياد بيعمل المراجعة النهائية (QA) ودمج أي حاجة محتاجة تتجمّع.

---

## 👥 أعضاء الفريق

| الكود | الاسم | المسار |
|-------|-------|--------|
| TL | Eyad Ahmed (Leader) | Power BI — Full Build (Data Model + 4 Pages + DAX) |
| Contributor | Rawan Tarek | Early Power BI page draft (exploration phase) |
| MB | Ahmed Ali | Python — Data Cleaning & EDA |
| MC | Mostafa Sabry | Excel Dashboard |

---

## 💡 نصائح سريعة لنجاح الفريق:
- **التواصل المستمر:** لو في Metric معين مش واضح أو محتاج مساعدة، اسأل الفريق.
- **مطابقة الأرقام:** كل الأدوات الثلاثة (Power BI / Python / Excel) لازم تطلّع نفس الأرقام الأساسية (Revenue, Rides, On-Time%...). أي فرق = فيه مشكلة محتاجة تتحل قبل التسليم.
- **الإبداع:** المتطلبات المكتوبة هي إطار عمل (Framework)، لو شايف حاجة هتوصل المعلومة أحسن، استخدمها فورًا!

**بالتوفيق للجميع في المشروع! 🔥**
