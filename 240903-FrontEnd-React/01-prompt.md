# Front-End Tech Screen — Payment Progress Bar (React)

## Type
Frontend coding — UI component implementation

## Task

Build a payment progress bar component that displays an outstanding balance, paid amount, and total.

## Visual Design

```
         Outstanding balance
              $3,468.79
[████████████░░░░░░░░░░░░░░░░░░░░░░]
Paid                           Total
$1,616.21                   $5,085.00
```

## Specs

- Progress bar fill color: `#ff0000` (red)
- Progress bar background color: `#e8e8e8` (light grey)
- Progress bar height: `16px`
- Space above and below progress bar: `16px`
- Space between label and value: `4px` in all cases

## Data

- `paid`: amount paid so far
- `total`: total amount owed
- `outstanding`: total - paid (derived)

## Requirements

- Fill width = `(paid / total) * 100%`
- Display outstanding balance prominently at top
- Display paid (bottom left) and total (bottom right)
- Labels and values stacked vertically with 4px gap
