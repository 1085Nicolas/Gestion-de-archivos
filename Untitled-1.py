pais = input("Ingresar nombre del país en ingles: ").strip()
contador = 0

with open("SalesJan2009.csv", "r", encoding="utf-8") as f:

  for linea in f:
      dato = linea.strip().split(",")
      print (dato)
      if dato[7].strip() == pais:
          contador += 1

print(f"{pais}: {contador}")
