"""
=============================================================
  UK Train Rides Analysis — Member A: الهوية والتواريخ
=============================================================
المسؤولية:
  - الأعمدة: Transaction ID, Date of Purchase, Time of Purchase, Date of Journey
  - الـ Features الجديدة: Booking_Lead_Days, Month

الاستخدام:
    from clean_member_a import clean_member_a
    df = clean_member_a(df)
=============================================================
"""

import pandas as pd
import numpy as np


def clean_member_a(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 60)
    print("▶ Member A: بدء معالجة أعمدة الهوية والتواريخ")
    print("=" * 60)

    df = df.copy()

    # 1. Transaction ID
    print("\n[1/4] فحص Transaction ID...")
    assert df["Transaction ID"].notna().all(), "❌ توجد قيم فارغة في Transaction ID"
    assert df["Transaction ID"].duplicated().sum() == 0, "❌ توجد قيم مكررة"
    print(f"  ✅ {len(df):,} سجل | لا تكرار")

    # 2. Date of Purchase
    print("\n[2/4] تحويل Date of Purchase...")
    df["Date of Purchase"] = pd.to_datetime(df["Date of Purchase"], errors="coerce")
    assert df["Date of Purchase"].notna().all()
    print(f"  ✅ {df['Date of Purchase'].min().date()} → {df['Date of Purchase'].max().date()}")

    # 3. Time of Purchase
    print("\n[3/4] تحويل Time of Purchase...")
    df["Time of Purchase"] = pd.to_timedelta(df["Time of Purchase"])
    assert df["Time of Purchase"].notna().all()
    print("  ✅ تم التحويل إلى timedelta")

    # 4. Date of Journey
    print("\n[4/4] تحويل Date of Journey...")
    df["Date of Journey"] = pd.to_datetime(df["Date of Journey"], errors="coerce")
    assert df["Date of Journey"].notna().all()
    print(f"  ✅ {df['Date of Journey'].min().date()} → {df['Date of Journey'].max().date()}")

    # Feature Engineering
    print("\n[FE] إنشاء الـ Features...")
    df["Booking_Lead_Days"] = (df["Date of Journey"] - df["Date of Purchase"]).dt.days
    assert (df["Booking_Lead_Days"] >= 0).all()
    print(f"  ✅ Booking_Lead_Days — متوسط: {df['Booking_Lead_Days'].mean():.1f} يوم")

    df["Month"] = df["Date of Journey"].dt.month_name()
    print(f"  ✅ Month — {sorted(df['Month'].unique().tolist())}")

    print("\n✅ Member A: اكتمل!")
    return df


if __name__ == "__main__":
    df = pd.read_csv("UK Train Rides new.csv")
    df = clean_member_a(df)
    print(df[["Date of Journey", "Booking_Lead_Days", "Month"]].head())
