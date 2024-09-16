def ordenamiento_fusion(lista):
    if len(lista) > 1:
        mitad = len(lista) // 2
        izq = lista[:mitad]
        der = lista[mitad:]

        ordenamiento_fusion(izq)
        ordenamiento_fusion(der)

        i = j = k = 0
        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k] = der[j]
                j += 1
            k += 1

        while i < len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1

        while j < len(der):
            lista[k] = der[j]
            j += 1
            k += 1

    return lista

lista = [64, 34, 25, 12, 22, 11, 90]
lista_ordenada = ordenamiento_burbuja(lista)
print(lista_ordenada)