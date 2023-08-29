mi = float(input('Massa inicial:'))
mf = mi
t = 0

while mf >= 0.5:
    mf = mf / 2
    t = t + 50

print('Massa inicial:', mi)
print('Massa final:', mf)
print('Tempo:', t,'s')
