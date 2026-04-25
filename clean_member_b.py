"""
=============================================================
  UK Train Rides Analysis — Member B: الركاب والدفع
=============================================================
المسؤولية:
  - الأعمدة: Purchase Type, Payment Method, Railcard, Refund Request
  - الـ Features الجديدة: Revenue_Lost_Flag
  - معالجة Railcard Nulls (20,918 قيمة فارغة → "None")

الاستخدام:
    from clean_member_b import clean_member_b
    df = clean_member_b(df)
=============================================================
"""

import pandas as pd
import numpy as np


def clean_member_b(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 60)
    print("▶ Member B: بدء معالجة أعمدة الركاب والدفع")
    print("=" * 60)

    df = df.copy()

    # 1. Purchase Type
    print("\n[1/4] فحص Purchase Type...")
    valid = {"Online", "Station"}
    assert set(df["Purchase Type"].dropna().unique()) == valid
    dist = df["Purchase Type"].value_counts(normalize=True) * 100
    print(f"  ✅ Online: {dist.get('Online',0):.1f}% | Station: {dist.get('Station',0):.1f}%")

    # 2. Payment Method
    print("\n[2/4] فحص Payment Method...")
    valid = {"Contactless", "Credit Card", "Debit Card"}
    assert set(df["Payment Method"].dropna().unique()).issubset(valid)
    print(f"  ✅ التوزيع:\n{df['Payment Method'].value_counts().to_string()}")

    # 3. Railcard — معالجة 20,918 قيمة فارغة
    print("\n[3/4] معالجة Railcard...")
    nulls = df["Railcard"].isna().sum()
    print(f"  📊 قيم فارغة: {nulls:,} ({nulls/len(df)*100:.1f}%)")
    df["Railcard"] = df["Railcard"].fillna("None")
    assert df["Railcard"].isna().sum() == 0
    print(f"  ✅ بعد المعالجة:\n{df['Railcard'].value_counts().to_string()}")

    # 4. Refund Request
    print("\n[4/4] فحص Refund Request...")
    assert set(df["Refund Request"].dropna().unique()) == {"Yes", "No"}
    refund = (df["Refund Request"] == "Yes").sum()
    print(f"  ✅ طلبات الاسترداد: {refund:,} ({refund/len(df)*100:.1f}%)")

    # Feature Engineering
    print("\n[FE] إنشاء Revenue_Lost_Flag...")
    if "Journey Status" in df.columns:
        df["Revenue_Lost_Flag"] = (
            (df["Journey Status"] == "Cancelled") & (df["Refund Request"] == "Yes")
        )
        print(f"  ✅ Revenue_Lost_Flag: {df['Revenue_Lost_Flag'].sum():,} حالة")
    else:
        df["Revenue_Lost_Flag"] = pd.NA
        print("  ⚠️  ستُحسب في master_pipeline.py بعد Member D")

    print("\n✅ Member B: اكتمل!")
    return df


if __name__ == "__main__":
    df = pd.read_csv("UK Train Rides new.csv")
    df = clean_member_b(df)
    print(df[["Railcard", "Payment Method", "Refund Request"]].head())
