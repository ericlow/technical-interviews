import sys
from collections import defaultdict

def main():
    by_date = defaultdict(lambda: [0.0, 0.0])   # [G_total, P_total]
    by_month = defaultdict(lambda: [0.0, 0.0])

    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        parts = [p.strip() for p in line.split(",")]
        month, day, txn_type, amount = parts[0], parts[1], parts[2], float(parts[3])

        idx = 0 if txn_type == "G" else 1
        by_date[(int(month), int(day))][idx] += amount
        by_month[int(month)][idx] += amount

    print("By Date:")
    for (m, d) in sorted(by_date):
        g, p = by_date[(m, d)]
        print(f"{m:02d}/{d:02d}: G={g:.2f}, P={p:.2f}")

    print()
    print("By Month:")
    for m in sorted(by_month):
        g, p = by_month[m]
        print(f"{m:02d}: G={g:.2f}, P={p:.2f}")


if __name__ == "__main__":
    main()
