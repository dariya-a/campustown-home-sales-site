"""Make data/city_median_sale_price.json from data/college_town_home_sales.csv.

For each city, the median sale price of sales of $10,000 or more, plus the number of
sales that rule kept and the number it dropped. Every value is computed from the CSV;
nothing is typed in by hand.

Run from the repository root:

    python3 scripts/city_median_sale_price.py

Rule: sales under $10,000 are left out of the median (the description sheet lists 40
such sales, including one at $0). Blank prices, if any, are also left out.
"""

import csv
import json
import statistics
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCE = ROOT / "data" / "college_town_home_sales.csv"
OUTPUT = ROOT / "data" / "city_median_sale_price.json"
MIN_PRICE = 10_000


def main():
    kept = {}     # (city, state) -> list of prices
    dropped = {}  # (city, state) -> count of prices under MIN_PRICE or blank
    total_rows = 0

    # Read every column as text, so ZIP codes, FIPS codes and parcel numbers keep their zeros.
    with SOURCE.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            total_rows += 1
            key = (row["city"], row["state"])
            raw = (row["sale_price"] or "").strip()
            if not raw:
                dropped[key] = dropped.get(key, 0) + 1
                continue
            price = int(raw)
            if price < MIN_PRICE:
                dropped[key] = dropped.get(key, 0) + 1
                continue
            kept.setdefault(key, []).append(price)
            dropped.setdefault(key, 0)

    cities = []
    for (city, state), prices in kept.items():
        cities.append({
            "city": city,
            "state": state,
            "median_sale_price": statistics.median(prices),
            "sales_counted": len(prices),
            "sales_under_rule": dropped.get((city, state), 0),
        })
    cities.sort(key=lambda c: c["median_sale_price"], reverse=True)

    output = {
        "source": "data/college_town_home_sales.csv",
        "rule": f"Sales with sale_price under ${MIN_PRICE:,} (and blank prices) are left out.",
        "total_rows": total_rows,
        "cities": cities,
    }
    with OUTPUT.open("w", encoding="utf-8") as f:
        json.dump(output, f, indent=2)
        f.write("\n")

    for c in cities:
        print(f'{c["city"]:<22}{c["state"]}  median ${c["median_sale_price"]:>11,.0f}  '
              f'counted {c["sales_counted"]:>5}  under rule {c["sales_under_rule"]:>3}')
    print(f"Wrote {OUTPUT.relative_to(ROOT)} ({len(cities)} cities, {total_rows} rows read)")


if __name__ == "__main__":
    main()
