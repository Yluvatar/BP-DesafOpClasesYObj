class Te:
    tipos_te = ['negro', 'verde', 'hierbas']
    tiempos_te = [3, 5, 6]
    recomendaciones_te = ['desayuno', 'medio día', 'atardecer']
    formatos_te = ['300', '500']
    valores_te = [3000, 5000]

    @staticmethod
    def obtener_descripcion(tipo):
        datos_te = [(tevalor, tivalor, rvalor) for (tei, tevalor), (tii, tivalor), (ti, rvalor) in
                    zip(enumerate(Te.tipos_te), enumerate(Te.tiempos_te), enumerate(Te.recomendaciones_te))
                    if tei == tipo]
        return datos_te

    @staticmethod
    def obtener_formato_valor(formato):
        return [(fvalor, vvalor) for (fi, fvalor), (vi, vvalor) in zip(enumerate(Te.formatos_te),
                                                                       enumerate(Te.valores_te)) if fi == formato]


if __name__ == '__main__':

    print("\nTipos de Té Disponibles:\n")

    for t in range(3):
        te, tiempo, recomendacion = Te.obtener_descripcion(t)[0]
        print(f"{t+1}. Té {te}, tiempo de preparación {tiempo} minutos, se recomienda consumir al {recomendacion} \n")

    print("Formatos Disponibles para cada tipo de Té\n")
    for f in range(2):
        formato, valor = Te.obtener_formato_valor(f)[0]
        print(f"{f+1}. Formato de {formato} gr $ {valor} \n")
