# Ejercicios de tuplas: búsqueda del tesoro pirata


def get_coordinate(registro):
    return registro[1]


def convert_coordinate(coordenada):
    c1 = coordenada[0]
    c2 = coordenada[1]
    tupla = (c1, c2)
    return tupla


def create_record(registro_azara, registro_rui):
    coordenada_rui = registro_rui[1][0] + registro_rui[1][1]
    if registro_azara[1] == coordenada_rui:
        return registro_azara + registro_rui
    else:
        return "not a match"


def sum_tuple(numeros):
    suma = 0
    for num in numeros:
        suma += num
    return suma



def count_occurrences(tupla, elemento):
    veces = 0
    for elem in tupla:
        if elem == elemento:
            veces += 1
    return veces


def find_index(tupla, elemento):
    posicion = 0
    for elem in tupla:
        if elem == elemento:
            return posicion
        else:
            posicion += 1
    return -1
print(find_index((10, 20, 30, 40), 40))


def filter_positives(numeros):
    lista = []
    for num in numeros:
        if num > 0:
            lista.append(num)
    tupla = tuple(lista)
    return tupla

