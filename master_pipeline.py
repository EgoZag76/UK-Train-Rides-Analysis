"""
=============================================================
  UK Train Rides Analysis — TL: Master Pipeline
=============================================================
يدمج سكربتات الأعضاء الأربعة بالترتيب الصحيح ويُصدر:
  - Cleaned_Data_Final.csv
  - cleaning_report.md

ترتيب التنفيذ:
  A (Dates) → D (Times) → B (Payment) → C (Pricing) → TL Features

الاستخدام:
    python master_pipeline.py
=============================================================
"""

import pandas as pd
import numpy as np
from pathlib import Path
import sys, time

from clean_member_a import clean_member_a
from clean_member_b import clean_member_b
from clean_member_c import clean_member_c
from clean_member_d import clean_member_d

INPUT_FILE  = "UK Train Rides new.csv"
OUTPUT_FILE = "Cleaned_Data_Final.csv"
REPORT_FILE = "cleaning_report.md"


def run_pipeline(input_path=INPUT_FILE):
    start = time.time()
    print("\n" + "="*60)
    print("  🚆 UK Train Rides — Master Cleaning Pipeline")
    print("="*60)

    df = pd.read_csv(input_path)
    n = len(df)
    print(f"📥 تم تحميل: {n:,} سجل | {df.shape[1]} عمود")

    df = clean_member_a(df)
    df = clean_member_d(df)
    df = clean_member_b(df)
    df = clean_member_c(df)
    df = add_tl_features(df)
    df = validate(df, n)

    df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8-sig")
    generate_report(df)

    print(f"\n✅ اكتمل في {time.time()-start:.1f}s | {OUTPUT_FILE} | {df.shape[1]} عمود")
    return df


def add_tl_features(df):
    print("\n▶ TL Features...")

    # Route
    df["Route"] = df["Departure Station"] + " -> " + df["Arrival Destination"]
    print(f"  ✅ Route — {df['Route'].nunique()} مسار فريد | أكثر: {df['Route'].value_counts().index[0]}")

    # Day_of_Week & Is_Weekend
    day_map = {0:"Monday",1:"Tuesday",2:"Wednesday",3:"Thursday",4:"Friday",5:"Saturday",6:"Sunday"}
    df["Day_of_Week"] = df["Date of Journey"].dt.dayofweek.map(day_map)
    df["Is_Weekend"]  = df["Date of Journey"].dt.dayofweek >= 5
    print(f"  ✅ Day_of_Week + Is_Weekend — عطلة: {df['Is_Weekend'].mean()*100:.1f}%")

    # Time_Period
    def time_period(h):
        if 6 <= h <= 9: return "Morning Peak"
        elif 10 <= h <= 15: return "Midday"
        elif 16 <= h <= 19: return "Evening Peak"
        else: return "Off-Peak"
    df["Time_Period"] = df["Departure_Hour"].apply(time_period)
    print(f"  ✅ Time_Period:\n{df['Time_Period'].value_counts().to_string()}")

    # Booking_Window
    def booking_window(d):
        if d == 0: return "Same Day"
        elif d <= 3: return "Short (1-3d)"
        elif d <= 7: return "Medium (4-7d)"
        elif d <= 14: return "Long (8-14d)"
        else: return "Very Long (>14d)"
    df["Booking_Window"] = df["Booking_Lead_Days"].apply(booking_window)
    print(f"  ✅ Booking_Window:\n{df['Booking_Window'].value_counts().to_string()}")

    # Revenue_Lost_Flag (final)
    df["Revenue_Lost_Flag"] = (
        (df["Journey Status"] == "Cancelled") & (df["Refund Request"] == "Yes")
    )
    rev_lost = df.loc[df["Revenue_Lost_Flag"], "Price"].sum()
    print(f"  ✅ Revenue_Lost_Flag — {df['Revenue_Lost_Flag'].sum():,} حالة | £{rev_lost:,.0f}")

    return df


def validate(df, n):
    print("\n▶ التحقق النهائي...")
    assert len(df) == n
    critical = ["Transaction ID","Date of Purchase","Date of Journey",
                "Ticket Class","Ticket Type","Price","Journey Status",
                "Railcard","Refund Request"]
    for col in critical:
        assert df[col].isna().sum() == 0, f"❌ nulls في {col}"

    new_cols = ["Booking_Lead_Days","Month","Route","Delay_Minutes",
                "Delay_Category","Journey_Duration_Min","Departure_Hour",
                "Day_of_Week","Is_Weekend","Time_Period","Price_Band",
                "Booking_Window","Ticket_Combo","Revenue_Lost_Flag"]
    missing = [c for c in new_cols if c not in df.columns]
    assert not missing, f"❌ مفقودة: {missing}"

    print(f"  ✅ {len(df):,} سجل | {df.shape[1]} عمود | إيرادات: £{df['Price'].sum():,.0f}")
    return df


def generate_report(df):
    rev_lost = df.loc[df["Revenue_Lost_Flag"], "Price"].sum()
    report = f"""# Cleaning Report
**Date:** {pd.Timestamp.now().strftime('%Y-%m-%d %H:%M')}

## Summary
| Property | Value |
|----------|-------|
| Total Records | {len(df):,} |
| Original Columns | 17 |
| New Feature Columns | 14 |
| Total Columns | {df.shape[1]} |

## Cleaning Actions
| Column | Issue | Fix |
|--------|-------|-----|
| Railcard | 20,918 nulls (66%) | Filled with "None" |
| Date of Purchase | String | Converted to datetime64 |
| Date of Journey | String | Converted to datetime64 |
| Time of Purchase | String | Converted to timedelta |
| Departure/Arrival Times | String | Converted to timedelta |

## New Features (14)
`Booking_Lead_Days`, `Month`, `Route`, `Delay_Minutes`, `Delay_Category`,
`Journey_Duration_Min`, `Departure_Hour`, `Day_of_Week`, `Is_Weekend`,
`Time_Period`, `Price_Band`, `Booking_Window`, `Ticket_Combo`, `Revenue_Lost_Flag`

## Key Stats
- **Total Revenue:** £{df['Price'].sum():,.0f}
- **Revenue Lost (cancelled + refunded):** £{rev_lost:,.0f}
- **On Time Rate:** {(df['Journey Status']=='On Time').mean()*100:.1f}%
- **Top Route:** {df['Route'].value_counts().index[0]}

*Auto-generated by master_pipeline.py*
"""
    with open(REPORT_FILE, "w", encoding="utf-8") as f:
        f.write(report)
    print(f"  📄 {REPORT_FILE}")


if __name__ == "__main__":
    if not Path(INPUT_FILE).exists():
        print(f"❌ الملف غير موجود: {INPUT_FILE}")
        sys.exit(1)
    run_pipeline()
