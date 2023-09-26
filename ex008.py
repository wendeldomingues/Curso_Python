met = float(input('Uma distância em metros: '))
km = met * 0.001
hm = met * 0.01
dam = met * 0.1
dm = met * 10
cm = met * 100
mm = met * 1000
print(f'A medida de {met}m corresponde a \n{km}km \n{hm}hm \n{dam}dam \n{dm:.0f}dm \n{cm:.0f}cm \n{mm:.0f}mm')