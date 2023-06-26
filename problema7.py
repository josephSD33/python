print("Ingrese la cantidad de barras de pan NO frescas vendidas")
nofrescas = int(input())
precioregular = 3000
descuento= precioregular * 0.6
preciodescuento = nofrescas * descuento
print(F"El precio regular de una barra de pan es {precioregular}")
print(F"El descuento aplicado por no ser fresca es de {descuento}")
print(F"El costo final es de {preciodescuento}")