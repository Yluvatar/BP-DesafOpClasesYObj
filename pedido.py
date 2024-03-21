from te import Te


def valida_opciones(opciones, eleccion):
    while eleccion not in opciones:
        eleccion = input("Elección no válida, por favor seleccione su opción: ")

    return eleccion


def eleccion_tipo_te(eleccion):

    te_eleg, tiempo, descripcion = Te.obtener_descripcion(eleccion - 1)[0]

    print(f"\nTé {te_eleg}, el tiempo de preparación es {tiempo} minutos, se recomienda al {descripcion}\n")

    return [te_eleg, tiempo, descripcion]


def eleccion_formato_te(eleccion):

    formato, valor = Te.obtener_formato_valor(eleccion - 1)[0]

    print(f"\nFormato {formato} grs., valor $ {valor}")

    return [formato, valor]


te = Te.tipos_te
formato = Te.formatos_te

print("\nBienvenido a la tienda de Té\n")

for i, te_desc in enumerate(te):
    print(f"{i + 1}. {te_desc}")

eleccion = input("\nQue tipo de té desea? > ")

eleccion = valida_opciones(['1', '2', '3'], eleccion)

te_elegido, tiempo, descripcion = eleccion_tipo_te(int(eleccion))

for i, f in enumerate(formato):
    print(f"{i + 1}. {f}")

eleccion = input("\nQue formato desea? > ")
eleccion = valida_opciones(['1', '2'], eleccion)

formato_elegido, valor = eleccion_formato_te(int(eleccion))

cantidad = input("\nCantidad requerida (max. 10)? > ")
print("\n")
cantidad = valida_opciones(['1', '2', '3', '4', '5', '6', '7', '8', '9', '10'], cantidad)
total = valor * int(cantidad)

print(f"Su pedido es:\n")
print(f"Té {te_elegido}, el tiempo de preparación es {tiempo} minutos, se recomienda al {descripcion}")
print(f"Formato {formato_elegido} grs., valor $ {valor}")
print(f"Cantidad: {cantidad}")
print(f"Total: $ {total}\n")

print(f"Gracias por su compra!!!\n")
