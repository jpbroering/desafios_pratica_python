a,b,c = [float(num) for num in input().split()]

triangulo = (a*c)/2
circulo = 3.14159*c**2
trapezio = ((a+b)*c)/2
quadrado = b**2
retangulo = a*b

print(f"TRIANGULO: {triangulo:.3f}\nCIRCULO: {circulo:.3f}\nTRAPEZIO: {trapezio:.3f}\nQUADRADO: {quadrado:.3f}\nRETANGULO: {retangulo:.3f}")