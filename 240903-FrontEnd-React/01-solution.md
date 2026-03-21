# Solution — Payment Progress Bar

## Approach

Single React component. Derive `outstanding` from `total - paid`. Fill width is a percentage.

## Component

```tsx
interface PaymentProgressProps {
  paid: number;
  total: number;
}

function formatCurrency(amount: number): string {
  return amount.toLocaleString('en-US', { style: 'currency', currency: 'USD' });
}

export function PaymentProgress({ paid, total }: PaymentProgressProps) {
  const outstanding = total - paid;
  const fillPercent = (paid / total) * 100;

  return (
    <div style={{ fontFamily: 'sans-serif' }}>
      <div style={{ textAlign: 'center', marginBottom: 4 }}>Outstanding balance</div>
      <div style={{ textAlign: 'center', fontSize: 32, fontWeight: 'bold', marginBottom: 4 }}>
        {formatCurrency(outstanding)}
      </div>

      <div style={{
        height: 16,
        backgroundColor: '#e8e8e8',
        borderRadius: 8,
        margin: '16px 0',
        overflow: 'hidden',
      }}>
        <div style={{
          width: `${fillPercent}%`,
          height: '100%',
          backgroundColor: '#ff0000',
        }} />
      </div>

      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
        <div style={{ display: 'flex', flexDirection: 'column', gap: 4 }}>
          <span>Paid</span>
          <span>{formatCurrency(paid)}</span>
        </div>
        <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'flex-end', gap: 4 }}>
          <span>Total</span>
          <span>{formatCurrency(total)}</span>
        </div>
      </div>
    </div>
  );
}
```

## Key decisions

- `gap: 4` between label and value (not margin, to keep it consistent)
- `margin: '16px 0'` on the bar container satisfies 16px above and below
- `overflow: hidden` on container clips the fill to rounded corners
- `outstanding` is derived, not a prop — prevents inconsistent state
