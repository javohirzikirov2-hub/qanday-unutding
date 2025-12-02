""" O'zgaruvchi va arifmetik amallar f string"""
ism = "Javohir"
familiya = "Zikirov"
ism_familiya = ism + " " + familiya
ism_familiya2 = f"{ism} {familiya}"

# print(ism)
# print(familiya)
# print(ism_familiya)
# print(ism_familiya2)

a = 12 
b = 4

qushish = a + b
ayirish = a - b 
kopaytirish= a * b
bolish= a / b
bolish2= a // b
daraja = a ** b
qoldiq = a % b

print(f"{a} + {b} = {qushish}")
print(f"{a} - {b} = {ayirish}")
print(f"{a} * {b} = {kopaytirish}")
print(f"{a} / {b} = {bolish}")
print(f"{a} // {b} = {bolish2}")
print(f"{a} ** {b} = {daraja}")
print(f"{a} % {b} = {qoldiq}")