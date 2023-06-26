print("Ingrse la cantidad que va a invertir")
inversion=float(input())
print("Ingrese la tasade interes anual")
tasainteres=float(input())
print("ingrese la cantidad de annos de la invercion")
annos=float(input())
intereses= tasainteres / 100
capitalobtenido= inversion*(1+intereses)**annos
print(F"El capital obtenido en la invercion de de {capitalobtenido}")