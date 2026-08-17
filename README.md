# 🚆 UK Train Rides Analysis

> **Power BI Interactive Dashboard** analyzing **31,653 UK railway transactions** (Jan–Apr 2024)
>
> Design System: **Azure Rail Glassmorphism** — Deep Navy (#003366) + Azure Blue (#0078D4)

---

## 📋 Project Info

| Field | Details |
|-------|---------|
| **Instructor** | Kareem Bakly |
| **Tools** | Power BI Desktop, Python, Excel, GitHub |
| **Dataset** | 31,653 transactions × 18 columns |
| **Period** | January — April 2024 |
| **Data Model** | Star Schema (1 Fact + 5 Dimensions) with Surrogate Keys |

---

## 🎯 Strategic Objectives

1. **Revenue Optimization** — Identify revenue leakage, optimize pricing, analyze refund patterns
2. **Operational Reliability** — Monitor on-time %, analyze delays, track cancellations
3. **Demand Intelligence** — Understand booking behaviors, peak patterns, seasonal trends

---

## 📊 Dashboard Pages

| Page | What it answers |
|------|-----------------|
| **Executive Summary** | Five headline KPIs — revenue, rides, on-time %, average fare, cancellation rate — above trend, geographic, and station-ranking views |
| **Revenue Deep Dive** | Revenue by route, class × ticket-type matrix, price bands by month, railcard segments, refunded revenue |
| **Operations & Reliability** | On-time performance against a 90% target, delay reasons, delay-minute distribution, worst routes by delay |
| **Demand & Booking Patterns** | Rides by day and departure hour, month × day demand heatmap, booking-window mix, lead days vs ticket price |

All four pages share a persistent navigation bar and two global slicers, so filter context carries across the report. A semantic color convention is applied throughout — blue for on-time, amber for delayed, red for cancelled.

---

## 👥 Team

| Member | Role | Contribution |
|--------|------|--------------|
| **Eyad Ahmed** | Team Lead | Project plan, task breakdown, and delivery sequence · **Full Power BI build** — star schema data model, all DAX measures, all four report pages, design system, and final integration |
| **Ahmed Ali** | Data Analyst | Python — data cleaning and exploratory data analysis (EDA) |
| **Mostafa Sabry** | Data Analyst | Excel — supporting dashboard with KPI cards and analytical charts |
| **Rawan Tarek** | Contributor | Early Power BI page draft during the exploration phase |

---

## 📁 Repository Structure

```
├── 📂 MD/
│   └── 📊 Foundation_v1_TL.pbix
├── 📄 Project_Data.pdf
├── 📊 UK_Train_Rides_Dashboard.xlsx
├── 🎤 Presentation.pptx
├── 📋 README.md
├── 📑 TEAM_WORKFLOW.md
├── 📐 ADVANCED_DASHBOARD_GUIDE.md
├── 🗂️ UK Train Rides new.csv
├── 📂 docs/
└── 📂 archive/
```

---

## 🚀 Quick Start

1. Clone the repository
2. Open `MD/Foundation_v1_TL.pbix` in Power BI Desktop
3. Reference `ADVANCED_DASHBOARD_GUIDE.md` for the design standards
4. Reference `TEAM_WORKFLOW.md` for how the delivery was structured

---

*Built by Team Eyad Ahmed | Instructor: Kareem Bakly*
