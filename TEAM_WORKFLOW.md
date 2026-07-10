# 📋 Team Workflow — UK Train Rides Analysis

> **توزيع المهام الرسمي** | 4 أعضاء | Instructor: Kareem Bakly

---

## 👑 TL — Eyad Ahmed (Team Leader)

### المسؤوليات:
- **Dashboard Page:** Executive Summary
- **Data Architecture:** Star Schema (Fact_Rides + 5 Dimension Tables) + Surrogate Keys على كل الأبعاد
- **DAX Engine:** كل الـ Measures والـ Calculated Columns
- **Integration & QA:** دمج صفحات الفريق + مراجعة الجودة
- **Design System:** تطبيق Azure Rail Glassmorphism عبر كل الصفحات

### الـ Deliverables:
1. ✅ Data Model كامل (Star Schema + Surrogate Keys)
2. ✅ Executive Summary Page (5 KPI Cards + Line Chart + Station Bar Chart + Map)
3. ✅ Report Theme (Azure Rail Glassmorphism الفاتح)
4. ✅ Page Navigation System
5. ✅ Final Integration & Testing

---

## 📈 MD — Rawan Tarek (Data Analyst)

### المسؤوليات:
- **Dashboard Pages:** Revenue Deep Dive + Operations & Reliability + Demand & Booking Patterns

### الـ Deliverables:
1. Revenue by Top 10 Routes (Bar Chart via `Route` F14)
2. Ticket Class × Ticket Type Revenue Matrix
3. On-Time Performance Rate (Gauge - الفعلي 86.8%)
4. Delay Root Cause Analysis (Donut/Bar Chart for Reason for Delay)
5. Delay Distribution Histogram (`Delay_Minutes` F16)
6. Journey Status 100% Stacked Bar Chart (Month × Journey Status)
7. Monthly Demand Heatmap (Month × Day of Week)
8. Peak Hours Identification
9. Purchase Type Distribution (Donut Chart)

### الـ Visuals المطلوبة:
- Bar Chart (Revenue by Top 10 Routes)
- Matrix with Conditional Formatting (Ticket Class × Ticket Type)
- Gauge Chart (On-Time % - Target 90%)
- Donut/Bar Chart (Reason for Delay)
- Histogram (Delay_Minutes F16)
- 100% Stacked Bar Chart (Journey Status Breakdown by Month)
- Matrix Heatmap (Conditional Colors)
- Bar Chart (Peak Hours / Time Periods)
- Donut Chart (Purchase Type)
- KPI Cards (Refunded_Revenue, Avg_Ticket_Price, On_Time_Pct, Cancellation_Rate)

---

## 🐍 MB — Ahmed Ali (Data Analyst)

### المسؤوليات:
- **Track:** Python — Data Cleaning & Exploratory Data Analysis (EDA)

### الـ Deliverables:
1. تنظيف الداتا الخام (railway.csv) قبل دخولها Power BI
2. Notebook كامل (`feature_cleaned.ipynb`) بخطوات التنظيف والتحليل
3. Exploratory Data Analysis (توزيعات، outliers، علاقات بين الأعمدة)
4. تقرير مختصر بأهم الـ insights

---

## 📊 MC — Mostafa Sabry (Data Analyst)

### المسؤوليات:
- **Track:** Excel — داشبورد مبسّط مطابق لأرقام الـ Power BI

### الـ Deliverables:
1. 5 KPI Cards: Total Revenue · Total Rides · On-Time % · Cancellation % · Avg Ticket Price
2. Revenue by Month (Chart)
3. Journey Status Breakdown (Chart)
4. Top Stations by Revenue (Chart)
5. Rides by Day of Week (Chart)
6. كل الحسابات Formulas (مش أرقام ثابتة)

---

## 📅 Workflow Steps

```
1. Ahmed Ali ينظف الداتا في Python → يسلّم النسخة النضيفة
2. Eyad يبني Star Schema + Surrogate Keys + DAX + Executive Summary
3. Rawan تبني صفحات Revenue / Operations / Demand على نفس الموديل والثيم
4. Mostafa يبني داشبورد Excel من نفس الداتا، ويتأكد من مطابقة الأرقام
5. Eyad يعمل QA نهائي ودمج كل حاجة قبل الدفاع
```

---

## 🎨 Design Rules (Mandatory)

| Rule | Value |
|------|-------|
| Canvas Size | 1664 × 936 px |
| Primary Color | Deep Navy #003366 |
| Accent Color | Azure Blue #0078D4 |
| Font | Segoe UI |
| Header Height | 45px Navy band |
| Corner Radius | 12px cards, 20px containers |
| Animation | ON, 800ms |

---

> 📌 For detailed design guide, see: **ADVANCED_DASHBOARD_GUIDE.md**
