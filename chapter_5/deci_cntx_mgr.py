import decimal

print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

with decimal.localcontext() as ctx:
    ctx.prec = 2
    print(decimal.Decimal('1.00') / decimal.Decimal('3.00'))

