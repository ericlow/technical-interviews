Transaction Ledger

Input is a series of comma-separated lines read from stdin. Each line has four fields: month (zero-padded two-digit integer), day (zero-padded two-digit integer), type (single character, either G for pay-in or P for pay-out), and amount (float).

Example input:
12,01, G, 0.25
12,01, P, 1.50
12,15, G, 3.00
10,04, P, 1.12
10,04, G, 0.50

Output two reports. First, a daily report sorted by date (month then day), showing the total G and total P for each unique date. Second, a monthly report sorted by month, showing the total G and total P for each unique month. All amounts should be formatted to two decimal places.

Example output:
By Date:
10/04: G=0.50, P=1.12
12/01: G=0.25, P=1.50
12/15: G=3.00, P=0.00

By Month:
10: G=0.50, P=1.12
12: G=3.25, P=1.50
