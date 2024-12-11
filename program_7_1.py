d = int(input())
x = int(input())
a = int((((365 - (75 / (d**3))) / (3 * (d**2) - d)) * 5)*x)
b = int((((412 - (125 / (d**3))) / (2 * (d**2) - d)) * 4)*x)
r = a + b
print(r)
