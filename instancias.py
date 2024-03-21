import te as t

Te = t.Te()
Precios = t.Te()

if type(Te.tipos_te) == type(Precios.formatos_te):
    for te in Te.tipos_te:
        print("Tipo de te: ", te, "\n")
    for precio in Precios.formatos_te:
        print("Tipo de formato: ", precio, "gr.\n")
else:
    print("Los objetos no son del mismo tipo")
