# 📋 Team Workflow — UK Train Rides Analysis

> **توزيع المهام الرسمي** | 4 أعضاء | Instructor: Kareem Bakly

---

## 👑 TL — Eyad Ahmed (Team Leader)

### المسؤوليات:
- **Project Plan:** تقسيم المهام + تحديد الأدوات + ترتيب التسليم
- **Data Architecture:** Star Schema (Fact_Rides + 5 Dimension Tables) + Surrogate Keys على كل الأبعاد
- **DAX Engine:** كل الـ Measures والـ Calculated Columns
- **Report Build:** كل صفحات التقرير الأربعة
- **Design System:** تطبيق Azure Rail Glassmorphism عبر كل الصفحات
- **Integration & QA:** الدمج النهائي + مراجعة الجودة

### الـ Deliverables:
1. ✅ Data Model كامل (Star Schema + Surrogate Keys)
2. ✅ Executive Summary Page (5 KPI Cards + Line Chart + Station Bar Chart + Map)
3. ✅ Revenue Deep Dive Page (Matrix + Treemap + Price Bands + Railcard)
4. ✅ Operations & Reliability Page (Gauge + Delay Reasons + Worst Routes)
5. ✅ Demand & Booking Patterns Page (Heatmap + Departure Hours + Booking Window)
6. ✅ Report Theme (Azure Rail Glassmorphism الفاتح)
7. ✅ Page Navigation System
8. ✅ Final Integration & Testing

---

## 🐍 Ahmed Ali (Data Analyst)

### المسؤوليات:
- **Python:** تنظيف البيانات (Data Cleaning)
- **EDA:** التحليل الاستكشافي للبيانات

### الـ Deliverables:
1. ✅ Cleaned Dataset
2. ✅ EDA Notebook

---

## 📊 Mostafa Sabry (Data Analyst)

### المسؤوليات:
- **Excel:** داشبورد مساند يعكس مقاييس الـ Power BI

### الـ Deliverables:
1. ✅ Excel Dashboard (5 KPI Cards + 4 Charts + Formula-based calculations)

---

## 🤝 Rawan Tarek (Contributor)

### المساهمة:
- مسودة صفحة Power BI مبكرة في مرحلة الاستكشاف

---

## 🔄 Delivery Pipeline

1. **Data Preparation** — Python cleaning & EDA · *Ahmed Ali*
2. **Data Modeling** — Star Schema + Surrogate Keys · *Eyad Ahmed*
3. **Measure Layer** — DAX authoring · *Eyad Ahmed*
4. **Report Build** — 4-page Power BI development · *Eyad Ahmed*
5. **Parallel Validation** — Excel cross-check · *Mostafa Sabry*
6. **Integration & QA** — Final consolidation and release · *Eyad Ahmed*

---

## 🎨 Design Standards

| Standard | Value |
|----------|-------|
| **Primary Colors** | Deep Navy `#003366` + Azure Blue `#0078D4` |
| **Semantic Colors** | Blue = On Time · Amber = Delayed · Red = Cancelled |
| **Typography** | Segoe UI |
| **Canvas** | 1664 × 936 px |
| **Corners** | 12–20px rounded |
| **Transitions** | 800ms ease-in-out |

النظام ده مطبق بنفس الشكل على الصفحات الأربعة، عشان التقرير يقرا كمنتج واحد مش أربع صفحات منفصلة.
