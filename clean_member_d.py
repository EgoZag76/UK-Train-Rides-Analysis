"""
=============================================================
  UK Train Rides Analysis — Member D: التوقيت والتأخير
=============================================================
المسؤولية:
  - الأعمدة: Departure Time, Arrival Time, Actual Arrival Time, Journey Status
  - الـ Features الجديدة: Delay_Minutes, Delay_Category, Journey_Duration_Min, Departure_Hour

الاستخدام:
    from clean_member_d import clean_member_d
    df = clean_member_d(df)
=============================================================
"""

import pandas as pd
import numpy as np


def _parse_time(series, col_name):
    result = pd.to_timedelta(series, errors="coerce")
    failed = result.isna().sum()
    if failed > 0:
        print(f"  ⚠️  {col_name}: {failed} قيمة فشل تحويلها")
    return result


def clean_member_d(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 60)
    print("▶ Member D: بدء معالجة أعمدة التوقيت والتأخير")
    print("=" * 60)

    df = df.copy()

    # 1. Journey Status
    print("\n[1/4] فحص Journey Status...")
    valid = {"On Time", "Delayed", "Cancelled"}
    assert set(df["Journey Status"].dropna().unique()) == valid
    assert df["Journey Status"].isna().sum() == 0
    for s, pct in (df["Journey Status"].value_counts(normalize=True)*100).items():
        print(f"  ✅ {s}: {pct:.1f}%")

    # 2-4. تحويل أعمدة الوقت
    for col in ["Departure Time", "Arrival Time", "Actual Arrival Time"]:
        print(f"\n تحويل {col}...")
        df[col] = _parse_time(df[col], col)
        assert df[col].isna().sum() == 0
        print(f"  ✅ تم التحويل بنجاح")

    # Feature Engineering
    print("\n[FE] إنشاء الـ Features...")

    # Delay_Minutes
    delay_sec = (df["Actual Arrival Time"] - df["Arrival Time"]).dt.total_seconds()
    df["Delay_Minutes"] = np.where(
        df["Journey Status"] == "Delayed",
        (delay_sec / 60).clip(lower=0).round().astype(int), 0
    )
    delayed = df[df["Journey Status"] == "Delayed"]
    print(f"  ✅ Delay_Minutes — متوسط: {delayed['Delay_Minutes'].mean():.1f} دقيقة")

    # Delay_Category
    def delay_cat(row):
        if row["Journey Status"] == "Cancelled": return "Cancelled"
        elif row["Delay_Minutes"] == 0: return "On Time"
        elif row["Delay_Minutes"] <= 15: return "Minor (<=15min)"
        else: return "Major (>15min)"
    df["Delay_Category"] = df.apply(delay_cat, axis=1)
    print(f"  ✅ Delay_Category:\n{df['Delay_Category'].value_counts().to_string()}")

    # Journey_Duration_Min
    dur = (df["Arrival Time"] - df["Departure Time"]).dt.total_seconds()
    dur = dur.where(dur >= 0, dur + 24*3600)
    df["Journey_Duration_Min"] = (dur / 60).round().astype(int)
    assert (df["Journey_Duration_Min"] > 0).all()
    print(f"  ✅ Journey_Duration_Min — Min: {df['Journey_Duration_Min'].min()} | Max: {df['Journey_Duration_Min'].max()}")

    # Departure_Hour
    df["Departure_Hour"] = df["Departure Time"].dt.components["hours"].astype(int)
    print(f"  ✅ Departure_Hour — أكثر ساعة: {df['Departure_Hour'].mode()[0]}:00")

    print("\n✅ Member D: اكتمل!")
    return df


if __name__ == "__main__":
    df = pd.read_csv("UK Train Rides new.csv")
    df = clean_member_d(df)
    print(df[["Journey Status", "Delay_Minutes", "Delay_Category", "Journey_Duration_Min"]].head())
