"""
=============================================================
  UK Train Rides Analysis — Member C: التذاكر والتسعير
=============================================================
المسؤولية:
  - الأعمدة: Ticket Class, Ticket Type, Price
  - الـ Features الجديدة: Price_Band, Ticket_Combo

الاستخدام:
    from clean_member_c import clean_member_c
    df = clean_member_c(df)
=============================================================
"""

import pandas as pd
import numpy as np


def clean_member_c(df: pd.DataFrame) -> pd.DataFrame:
    print("=" * 60)
    print("▶ Member C: بدء معالجة أعمدة التذاكر والتسعير")
    print("=" * 60)

    df = df.copy()

    # 1. Ticket Class
    print("\n[1/3] فحص Ticket Class...")
    assert set(df["Ticket Class"].dropna().unique()) == {"Standard", "First Class"}
    assert df["Ticket Class"].isna().sum() == 0
    for cls, pct in (df["Ticket Class"].value_counts(normalize=True)*100).items():
        print(f"  ✅ {cls}: {pct:.1f}%")

    # 2. Ticket Type
    print("\n[2/3] فحص Ticket Type...")
    assert set(df["Ticket Type"].dropna().unique()) == {"Advance", "Off-Peak", "Anytime"}
    assert df["Ticket Type"].isna().sum() == 0
    for t, pct in (df["Ticket Type"].value_counts(normalize=True)*100).items():
        print(f"  ✅ {t}: {pct:.1f}%")

    # 3. Price
    print("\n[3/3] فحص Price...")
    assert df["Price"].isna().sum() == 0
    assert (df["Price"] > 0).all()
    assert df["Price"].max() <= 500
    print(f"  ✅ Min: £{df['Price'].min()} | Max: £{df['Price'].max()} | Mean: £{df['Price'].mean():.2f}")

    # Feature Engineering
    print("\n[FE] إنشاء الـ Features...")

    def price_band(p):
        if p <= 10: return "Budget"
        elif p <= 30: return "Standard"
        elif p <= 60: return "Premium"
        else: return "Luxury"

    df["Price_Band"] = df["Price"].apply(price_band)
    print(f"  ✅ Price_Band:\n{df['Price_Band'].value_counts().to_string()}")

    df["Ticket_Combo"] = df["Ticket Class"] + " / " + df["Ticket Type"]
    print(f"  ✅ Ticket_Combo — {df['Ticket_Combo'].nunique()} تركيبة فريدة")

    print("\n✅ Member C: اكتمل!")
    return df


if __name__ == "__main__":
    df = pd.read_csv("UK Train Rides new.csv")
    df = clean_member_c(df)
    print(df[["Price", "Price_Band", "Ticket_Combo"]].head())
