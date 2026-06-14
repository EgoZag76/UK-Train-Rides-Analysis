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
2. ✅ Executive Summary Page (5 KPI Cards + Line Chart + Station Bar Chart + 100% Stacked Bar + Station Map)
3. ✅ Forecasting Page (اختياري - مدمج في Power BI)
4. ✅ Report Theme JSON (Azure Rail Glassmorphism الفاتح)
5. ✅ Page Navigation System
6. ✅ Final Integration & Testing

---

## 📊 MB — Ahmed Ali (Data Analyst)

### المسؤوليات:
- **Dashboard Page:** Revenue Deep Dive

### الـ Deliverables:
1. Revenue by Top 10 Routes (Bar Chart via `Route` F14)
2. Ticket Class × Ticket Type Revenue Matrix (with Data Bars)
3. Revenue Treemap (Route → Class → Type)
4. Stacked Bar (Price_Band × Month Revenue)
5. Railcard Revenue (Filtered, excluding "None")
6. Month-over-Month Revenue Change (with ▲▼ indicators)

### الـ Visuals المطلوبة:
- Bar Chart (Revenue by Top 10 Routes)
- Matrix with Conditional Formatting (Ticket Class × Ticket Type)
- Treemap (Route → Ticket Class → Ticket Type)
- Stacked Bar (Price_Band × Month)
- Column Chart (Railcard Revenue, filtered)
- KPI Cards (× 2: Refunded_Revenue + Avg_Ticket_Price)

---

## ⏱️ MC — Mostafa Sabry (Data Analyst)

### المسؤوليات:
- **Dashboard Page:** Operations & Reliability

### الـ Deliverables:
1. On-Time Performance Rate (Gauge with 90% Target - الفعلي 86.8% قرار سردي واعٍ)
2. Delay Root Cause Analysis / أسباب التأخير والإلغاء (Donut/Bar Chart for Reason for Delay)
3. Delay Distribution Histogram (عبر `Delay_Minutes` F16)
4. Journey Status 100% Stacked Bar Chart (Month_Name × Journey Status)
5. Top 10 Worst Routes by Delay/Cancellation (Bar Chart via `Route` F14)
6. Cancellation Rate Tracking (KPI Card)

### الـ Visuals المطلوبة:
- Gauge Chart (On-Time % - Target 90%)
- Donut/Bar Chart (Reason for Delay)
- Histogram (Delay_Minutes F16)
- 100% Stacked Bar Chart (Journey Status Breakdown by Month)
- Bar Chart (Top 10 Worst Routes via Route F14)
- KPI Cards (× 2: On_Time_Pct + Cancellation_Rate)

---

## 📈 MD — Rawan Tarek (Data Analyst)

### المسؤوليات:
- **Dashboard Page:** Demand & Booking Patterns

### الـ Deliverables:
1. Monthly Demand Heatmap (Month × Day of Week)
2. Booking Window Analysis (Days between Purchase & Journey)
3. Peak Hours Identification (`Departure_Hour` (F17) **أو** Time_Period Bar Chart)
4. Purchase Type Distribution (Donut Chart)
5. Price vs Booking Lead Days Scatter (X = `Booking_Lead_Days` (F15), Y = Average Ticket Price, Bubble Size = Rides)
6. Booking Funnel (All → Advance → On Day)

### الـ Visuals المطلوبة:
- Column Chart (Day_Name Rides, sorted)
- Matrix Heatmap (Conditional Colors)
- Bar Chart (`Departure_Hour` (F17) **أو** Time Periods with Peak Highlight)
- Bar Chart (Booking Window, sorted)
- Scatter/Bubble Chart (`Booking_Lead_Days` (F15) × Average Price)
- Donut Chart (Purchase Type)

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
