a = 500
b = 100240.759834772
c = "Hello, World!"
d = False

s = '{0}: {1:d}\t{2}\t{3}\t{4}'.format(d, d, a, b, c)
print(s)

print('%s %s' % (True, False))
print('%i %i' % (True, False))
print()

t = f'{a} {b:,.2f}\n{c[:5]}\n{d}'
print(t)
