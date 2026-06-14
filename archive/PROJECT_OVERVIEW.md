# 🚆 UK Train Rides Analysis — Project Overview

---

## 📌 المشروع (About This Project)

تحليل شامل لبيانات رحلات القطارات في المملكة المتحدة خلال الفترة من **يناير إلى أبريل 2024**، يهدف إلى استخراج رؤى تجارية (Business Insights) قابلة للتنفيذ عبر ثلاثة محاور استراتيجية: **الإيرادات، العمليات، والطلب**.

---

## 📊 البيانات (Dataset at a Glance)

| المؤشر | القيمة |
|--------|--------|
| **إجمالي المعاملات** | 31,653 سجل |
| **الفترة الزمنية** | يناير – أبريل 2024 |
| **محطات المغادرة** | 12 محطة |
| **وجهات الوصول** | 32 وجهة |
| **أنواع التذاكر** | Advance · Off-Peak · Anytime |
| **فئات التذاكر** | Standard · First Class |
| **أعمدة أصلية** | 17 عمود |
| **أعمدة مُهندسة (Features)** | +13 عمود جديد |

---

## 🎯 المحاور الاستراتيجية (Strategic Pillars)

### 💰 Revenue Optimization — تحسين الإيرادات
تحليل مصادر الإيرادات حسب المسار، نوع التذكرة، وفئتها. تحديد الفرص السعرية وقياس خسائر الإيرادات الناتجة عن الإلغاءات والاستردادات.

### ⏱️ Operational Reliability — الموثوقية التشغيلية
قياس أداء الخدمة من حيث الالتزام بالمواعيد (On-Time Performance)، تحليل أنماط التأخير وشدته، ورصد المحطات والمسارات الأقل موثوقية.

### 📈 Demand Intelligence — تحليل الطلب
فهم سلوك الحجز المسبق، أوقات الذروة، أنماط الأيام والأشهر، والتنبؤ بالطلب المستقبلي لشهر مايو 2024.

---

## 🗂️ صفحات الـ Dashboard

| # | الصفحة | الوصف | اللون الرئيسي |
|---|--------|-------|---------------|
| 1 | **Executive Summary** | نظرة عامة شاملة بأهم المؤشرات (KPIs) | 🔵 Navy `#1B2A4A` |
| 2 | **Revenue Deep Dive** | تفصيل الإيرادات حسب المسار والتذاكر | 🟢 Emerald `#064E3B` |
| 3 | **Operations & Reliability** | جودة الخدمة والتأخيرات والإلغاءات | 🔴 Crimson `#7F1D1D` |
| 4 | **Demand & Booking Patterns** | سلوك الحجز وأوقات الذروة | 🟣 Purple `#4C1D95` |
| 5 | **Forecasting & Predictions** | التنبؤ بالطلب والإيرادات لمايو 2024 | 🔵 Navy `#1B2A4A` |

---

## 🔢 أهم المؤشرات (Key Metrics)

- **Total Revenue** — إجمالي الإيرادات
- **Total Journeys** — إجمالي عدد الرحلات
- **On-Time Performance (OTP%)** — نسبة الالتزام بالمواعيد
- **Cancellation Rate** — معدل الإلغاء
- **Average Ticket Price** — متوسط سعر التذكرة
- **Revenue Lost (Refunds)** — الإيرادات المفقودة بسبب الاسترداد
- **Average Delay (min)** — متوسط التأخير بالدقائق
- **Peak Hour** — ساعة الذروة
- **Top Route by Revenue** — أعلى مسار إيراداً
- **Avg Booking Lead Days** — متوسط أيام الحجز المسبق

---

## 👥 فريق العمل (Team)

| الدور | المسؤولية |
|-------|-----------|
| **Team Leader (TL)** | Data Modeling · DAX · Integration · QA · Executive Summary & Forecasting Pages |
| **Member A (MA)** | Data Cleaning (Dates) · Executive Summary Page |
| **Member B (MB)** | Data Cleaning (Payment) · Revenue Deep Dive Page |
| **Member C (MC)** | Data Cleaning (Tickets) · Operations & Reliability Page |
| **Member D (MD)** | Data Cleaning (Journey) · Demand & Booking Patterns Page |

---

## 🛠️ الأدوات المستخدمة (Tools & Stack)

| الأداة | الاستخدام |
|--------|-----------|
| **Python** | Data Cleaning · Feature Engineering · Forecasting |
| **Power BI** | Data Modeling · DAX · Interactive Dashboards |
| **GitHub** | Version Control · Team Collaboration |
| **CSV / XLSX** | Data Storage & Exchange |

---

## 📐 نموذج البيانات (Data Model)

```
        ┌─────────────┐
        │  Dim_Date    │
        └──────┬──────┘
               │
┌──────────┐   │   ┌──────────────┐
│Dim_Station├───┼───┤  Fact_Rides   │
└──────────┘   │   │  (31,653)    │
               │   └───┬─────┬───┘
        ┌──────┴──┐    │     │
        │Dim_Ticket│    │     │
        └─────────┘    │     │
                 ┌─────┴──┐  │
                 │Dim_Pay  │  │
                 └─────────┘  │
                        ┌─────┴────┐
                        │Dim_Rail   │
                        └──────────┘
```
**Star Schema** — جدول حقائق مركزي مع جداول أبعاد مرتبطة

---

## 📅 الجدول الزمني (Timeline)

| الأسبوع | المرحلة |
|---------|---------|
| **Week 1** | 🧹 Data Cleaning & Feature Engineering |
| **Week 2** | 📊 Analysis (20+ Analytical Questions) |
| **Week 3** | 🔮 Forecasting (3 Predictive Models) |
| **Week 4** | 🎨 Power BI Dashboard & Final Report |

---

> **ملاحظة:** هذا الملخص مُصمم ليكون صفحة "Project Overview" في أول صفحة من الـ Dashboard أو كمرجع سريع لأي شخص يريد فهم المشروع بنظرة واحدة.
