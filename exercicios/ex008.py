medida = float(input('Digite uma distância em METROS: '))

km = medida / 1000
hm = medida / 100
dam = medida / 10
dm = medida * 10
cm = medida * 100
mm = medida * 1000

print(f'KM: {km}')
print(f'HM: {hm}')
print(f'DAM: {dam}')
print(f'DM: {dm}')
print(f'CM: {cm}')
print(f'MM: {mm}')