# Design System: UK Train Rides Power BI Dashboard
**Project ID:** uk-train-rides-dashboard

## 1. Visual Theme & Atmosphere
The UI embodies a **"Command Center"** aesthetic—premium, data-dense, and highly professional. It utilizes a **Modern Dark Mode** approach with subtle glassmorphic elements to create depth. The atmosphere is sleek, authoritative, and focused on minimizing cognitive load while highlighting critical insights. It feels like a high-end SaaS analytics platform, designed specifically to frame Power BI visuals beautifully.

## 2. Color Palette & Roles

**Base Canvas & Surfaces:**
* **Midnight Space (App Background):** (`#0B132B`) - Deep, immersive background for the main canvas.
* **Slate Glass (Card/Container Background):** (`#1C2541`) - Used for visual containers, panels, and KPI card backgrounds. 
* **Subtle Border (Dividers):** (`#2B375A`) - Used for borders and separators to create structure without visual noise.

**Typography Colors:**
* **Crisp White (Primary Text):** (`#FFFFFF`) - High contrast for main KPI numbers and section headers.
* **Ash Gray (Secondary Text):** (`#8D99AE`) - For axis labels, subtitles, and metadata.

**Semantic & Page-Specific Accents:**
* **Executive Blue (Page 1 - Summary):** (`#3A86FF`) - Trustworthy, primary brand color. Used for general metrics and active states.
* **Revenue Green (Page 2 - Revenue):** (`#06D6A0`) - Success, growth, financial positive indicators.
* **Alert Red (Page 3 - Operations):** (`#EF476F`) - Cancellations, delays, negative financial impact.
* **Demand Purple (Page 4 - Demand):** (`#8338EC`) - Passenger volumes and booking patterns.
* **Warning Gold (Secondary Alerts):** (`#FFD166`) - Medium priority alerts, active filter indicators.

## 3. Typography Rules
* **Font Family:** `Segoe UI` (default Power BI) or a modern sans-serif like `Inter`.
* **Hierarchy:**
  - **Dashboard Title:** 28px, Bold, Crisp White.
  - **Section/Visual Headers:** 16px, Semi-Bold, Crisp White.
  - **KPI Values:** 32px-40px, Bold, Accent Color or Crisp White.
  - **Body/Labels:** 12px, Regular, Ash Gray.

## 4. Component Stylings
* **Cards/Containers (Dashboard Visual Slots):** 
  - **Shape:** Subtly rounded corners (`border-radius: 12px`).
  - **Appearance:** Solid or slightly translucent Dark Slate (`#1C2541`) with a whisper-soft `1px` border (`#2B375A`).
  - **Shadow:** Soft, diffused drop shadow (`box-shadow: 0 4px 20px rgba(0,0,0,0.2)`) to lift elements off the Midnight background.
* **Navigation & Slicers (Header/Sidebar):**
  - **Layout:** A dedicated top bar or left sidebar holding global filters (Month, Weekend/Weekday) and page navigation.
  - **Active State:** Highlighted with a pill-shaped background using the page's specific accent color at 20% opacity, with full-color text.

## 5. Layout Principles (Dashboard Patterns)
* **Grid Structure:** A 12-column layout with strict alignment.
* **Header Area:** The top 10-15% of the screen is reserved for the Dashboard Title, global slicers, and branding.
* **KPI Ribbon:** Directly below the header, a horizontal row of 3-4 primary KPI cards.
* **Whitespace (Padding):** Generous `16px` to `24px` gaps between visual containers (cards) to ensure breathing room and reduce visual clutter.

---

## 🛠️ Stitch Prompting Guide for Backgrounds

To generate these layouts in Google Stitch, use the following prompt structure based on the **Stitch UI Design** guidelines. You can copy/paste these directly into Stitch to generate the UI background layers for your Power BI pages.

### Prompt: Page 1 (Executive Summary)
```text
Dashboard layout background for a Train Rides Analytics platform (Executive Summary).

Key Features:
- Top header bar for title and global filters (slicers).
- Horizontal KPI ribbon below the header with 3 empty slots for KPI cards.
- Main content area split: 2/3 width for a large primary chart container, 1/3 width for a side chart container.
- Bottom area split into two equal-width containers for additional charts.

Visual Style:
- Dark mode aesthetic ("Command Center").
- Midnight Space background (#0B132B).
- Card containers should use Slate Glass (#1C2541) with 12px rounded corners and a subtle 1px border (#2B375A).
- Executive Blue accents (#3A86FF).
- Clean, data-focused, generous whitespace between cards (24px gap).

Platform: Desktop Web (16:9 aspect ratio, 1920x1080)
```

### Prompt: Page 2 (Revenue Deep Dive)
```text
Dashboard layout background for a Train Rides Analytics platform (Revenue).

Key Features:
- Top header bar for title and global filters (slicers).
- 2 KPI card slots on the top left, with a wide container on the top right for a trend chart.
- Middle area containing a large full-width container for a detailed data matrix.
- Bottom area split into 3 smaller equal-width containers for categorical charts.

Visual Style:
- Dark mode aesthetic ("Command Center").
- Midnight Space background (#0B132B).
- Slate Glass containers (#1C2541) with 12px rounded corners and subtle border.
- Revenue Green accents (#06D6A0) to emphasize financial data.
- Generous whitespace between containers.

Platform: Desktop Web (16:9 aspect ratio, 1920x1080)
```

### Prompt: Page 3 (Operations & Reliability)
```text
Dashboard layout background for a Train Rides Analytics platform (Operations).

Key Features:
- Top header bar for title and global filters.
- Center-aligned large container at the top for a main Gauge/KPI, flanked by 2 smaller KPI slots on each side.
- Middle area split 50/50 for a bar chart container and a waterfall chart container.
- Full-width container at the bottom for a detailed operations table.

Visual Style:
- Dark mode aesthetic.
- Midnight Space background (#0B132B).
- Slate Glass containers (#1C2541) with 12px rounded corners.
- Alert Red (#EF476F) and Success Green (#06D6A0) accents for operational status.

Platform: Desktop Web (16:9 aspect ratio, 1920x1080)
```

### Prompt: Page 4 (Demand & Booking Patterns)
```text
Dashboard layout background for a Train Rides Analytics platform (Demand).

Key Features:
- Top header bar for title and global filters.
- Main area split vertically: Left column (30% width) for 3 stacked chart containers, Right column (70% width) for 2 large stacked chart containers (Heatmap & Scatter plot).

Visual Style:
- Dark mode aesthetic.
- Midnight Space background (#0B132B).
- Slate Glass containers (#1C2541) with 12px rounded corners.
- Demand Purple accents (#8338EC) for passenger volume aesthetics.

Platform: Desktop Web (16:9 aspect ratio, 1920x1080)
```
