# 📋 Team Workflow — UK Train Rides Analysis

> **توزيع المهام الرسمي** | 4 أعضاء | Instructor: Kareem Bakly

---

## 👑 TL — Eyad Ahmed (Team Leader)

### المسؤوليات:
- **Dashboard Page:** Executive Summary + Forecasting (Optional)
- **Data Architecture:** Star Schema (Fact_Rides + 5 Dimension Tables)
- **DAX Engine:** كل الـ Measures والـ Calculated Columns
- **Integration & QA:** دمج صفحات الفريق + مراجعة الجودة
- **Design System:** تطبيق Azure Rail Glassmorphism عبر كل الصفحات

### الـ Deliverables:
1. ✅ Data Model كامل (Star Schema)
2. ✅ Executive Summary Page (KPI Cards + Charts)
3. ✅ Forecasting Page (اختياري)
4. ✅ Report Theme JSON
5. ✅ Page Navigation System
6. ✅ Final Integration & Testing

---

## 📊 MB — Ahmed Ali (Data Analyst)

### المسؤوليات:
- **Dashboard Page:** Revenue Deep Dive

### الـ Deliverables:
1. Revenue breakdown by Departure Station (Bar Chart)
2. Ticket Class × Ticket Type Revenue Matrix (with Data Bars)
3. Revenue Treemap (Station → Class → Type)
4. Refund Analysis (Rate + Trend)
5. Month-over-Month Revenue Change (with ▲▼ indicators)
6. Reference Lines (Average Revenue per Station)

### الـ Visuals المطلوبة:
- Clustered Bar Chart (Revenue by Station)
- Matrix with Conditional Formatting
- Treemap (3-level drill-down)
- Line Chart (Revenue Trend)
- Ribbon Chart (Station Ranking over Time)

---

## ⏱️ MC — Mostafa Sabry (Data Analyst)

### المسؤوليات:
- **Dashboard Page:** Operations & Reliability

### الـ Deliverables:
1. On-Time Performance Rate (Gauge with 90% Target)
2. Delay Root Cause Analysis (Donut Chart)
3. Cancellation Rate Tracking (Alert-Style KPI)
4. Journey Status Waterfall (On Time → Delayed → Cancelled)
5. Top 10 Worst Routes by Delay (Bar Chart)
6. Delay Distribution Histogram

### الـ Visuals المطلوبة:
- Gauge Chart (On-Time %)
- Donut Chart (Delay Reasons)
- Waterfall Chart (Status Breakdown)
- Bar Chart (Top 10 Delays)
- Line Chart (Monthly Trend with Anomaly Detection)
- Heatmap Matrix (Route × Status)

---

## 📈 MD — Rawan Tarek (Data Analyst)

### المسؤوليات:
- **Dashboard Page:** Demand & Booking Patterns

### الـ Deliverables:
1. Monthly Demand Heatmap (Month × Day of Week)
2. Booking Window Analysis (Days between Purchase & Journey)
3. Peak Hours Identification (Time Period Bar Chart)
4. Purchase Type Distribution (Donut Chart)
5. Price vs Revenue Scatter (with Bubble Size = Rides)
6. Booking Funnel (All → Advance → On Day)

### الـ Visuals المطلوبة:
- Matrix Heatmap (Conditional Colors)
- Clustered Bar Chart (Booking Window)
- Bar Chart (Time Periods with Peak Highlight)
- Donut Chart (Purchase Type)
- Scatter/Bubble Chart (Price × Revenue)
- Area Chart (Monthly Demand by Class)

---

## 📅 Workflow Steps

```
1. Clone Repo → Read GETTING_STARTED.md
2. Open Foundation_v1_TL.pbix → Find your page
3. Read ADVANCED_DASHBOARD_GUIDE.md → Follow design rules
4. Build your visuals → Apply design system colors
5. Save → Notify TL for review
6. TL merges all pages → Final QA
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
