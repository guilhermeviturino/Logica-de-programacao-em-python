'''va = int(input('va:'))
vb = int(input('vb:'))
vc = int(input('vc:'))

if va < vb and va< vc:
    print(va)
    if vb < vc:
        print(vb)
        print(vc)
    else:
        print(vc)
        print(vb)
elif vb < va and vb < vc:
    print(vb)
    if va < vc:
        print(va)
        print(vc)
    else:
        print(vc)
        print(va)
elif vc < va and vc < vb:
    print(vc)
    if va < vb:
        print(va)
        print(vb)
    else:
        print(vb)
        print(va) '''


#De outra forma 
va = int(input('va:'))
vb = int(input('vb:'))
vc = int(input('vc:'))
maior = -1

if va > maior: maior = va
if vb > maior: maior = vb
if vc > maior: maior = vc

menor = 99999
if va < menor: menor = va
if vb < menor: menor = vb
if vc < menor: menor = vc

medio = (va + vb + vc) - (menor + maior)
print(menor, medio, maior)
