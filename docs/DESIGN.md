# Design System: Azure Rail Glassmorphism (Light)
**Project ID:** uk-train-rides-dashboard-light

---

## 1. Visual Theme & Atmosphere
The UI embodies an **"Azure Rail Glassmorphism"** aesthetic—clean, light, modern, and highly readable. It uses a **translucent light glassmorphism** approach on a soft light-gray canvas to create depth and structure. The atmosphere is premium, bright, and professional, designed to make data visuals stand out with minimal cognitive load.

---

## 2. Color Palette & Roles

### Base Canvas & Surfaces
* **Base Background:** (`#F4F6F9`) - Soft light gray with a gentle cool undertone.
* **Glass Surface (Cards & Panels):** (`rgba(255, 255, 255, 0.85)`) - Translucent white for visual cards and KPI containers.
* **Glass Border:** (`rgba(255, 255, 255, 0.4)`) - Soft white border to define edges.
* **Divider Gradient:** `linear-gradient(90deg, #003366 0%, transparent 100%)`

### Brand Colors
* **Primary (Deep Navy):** (`#003366`) - Primary color for dashboard headers, page titles, and main text.
* **Accent (Azure Blue):** (`#0078D4`) - Accent color for active slicers, interactive elements, and highlight metrics.

### Status Colors
* **On-Time (Success Emerald):** (`#10B981`) - Used for positive operational metrics (OTP).
* **Delayed (Warning Amber):** (`#F59E0B`) - Used for delayed journeys and minor alerts.
* **Cancelled (Alert Crimson):** (`#EF4444`) - Used for cancellations, lost revenue, and critical alerts.

### Typography Colors
* **Primary Text (Deep Navy):** (`#003366`) - High-contrast text for headers and primary numbers.
* **Secondary Text (Slate Gray):** (`#5C6B73`) - Used for labels, descriptions, and axis values.

---

## 3. Typography Rules
* **Font Family:** `Segoe UI` (default Power BI) or a modern sans-serif like `Metropolis` / `Inter`.
* **Hierarchy:**
  - **Dashboard Title:** 24px, Bold, Deep Navy.
  - **Visual Headers:** 14px, Semi-Bold, Deep Navy.
  - **KPI Values:** 32px-40px, Bold, Deep Navy or Azure Blue.
  - **Body/Labels:** 10px-11px, Regular, Slate Gray.

---

## 4. Component Stylings
* **Cards/Containers (Dashboard Visual Slots):** 
  - **Shape:** Rounded corners (`border-radius: 12px`).
  - **Appearance:** Semi-translucent white (`rgba(255, 255, 255, 0.85)`) with a `1px` white border (`rgba(255, 255, 255, 0.4)`).
  - **Shadow:** Soft, highly diffused drop shadow (`box-shadow: 0 4px 30px rgba(0, 0, 0, 0.05)`) to lift cards off the background.
* **Navigation & Slicers:**
  - **Layout:** Top bar containing global filters (Month, Weekend/Weekday) and page navigation.
  - **Active State:** Highlighted with a light blue background (`rgba(0, 120, 212, 0.15)`) with deep navy/azure blue text.

---

## 5. Layout Principles (Dashboard Patterns)
* **Grid Structure:** Strict grid alignment with clean rows and columns.
* **Header Area:** The top 12% of the screen is reserved for the Dashboard Title, global slicers, and navigation.
* **KPI Ribbon:** A horizontal row of 3-4 primary KPI cards directly below the header.
* **Whitespace (Padding):** Generous gaps (`16px` to `24px`) between card containers to ensure breathing room and prevent visual clutter.

---

## ⚙️ Technical Implementation Note for Power BI

> [!NOTE]
> **Power BI Glassmorphism Workaround:**
> Since Power BI does not natively support CSS `backdrop-filter: blur()`, the Glassmorphism effect must be implemented as follows:
> 1. Use a high-fidelity static background image (containing the background color and soft glass visual panels/glows) generated from a design tool or via Stitch.
> 2. Import the background image into Power BI under **Format Page → Canvas Background**. Set **Image Fit** to "Fit" or "Fill" and set **Transparency** to `0%`.
> 3. Set the background color of all Power BI visual containers (cards, charts, tables) to **transparent** (Transparency `100%`) so they align perfectly with the glass card outlines on the background image.
