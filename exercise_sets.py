# Ejercicios de sets: catering del club de cocina

ALCOHOLS = {
    "whiskey", "whisky", "white rum", "dark rum", "bourbon", "rye", "scotch",
    "vodka", "tequila", "gin", "dry vermouth", "sweet vermouth", "prosecco",
    "aperol", "brandy", "mezcal", "triple sec", "coffee liqueur",
    "almond liqueur", "champagne", "orange curacao", "rum"
}


def clean_ingredients(nombre_plato, ingredientes):
    return (nombre_plato, set(ingredientes))


def check_drinks(nombre_bebida, ingredientes):
    for ingrediente in ingredientes:
        if ingrediente in ALCOHOLS:
            return f"{nombre_bebida} Cocktail"
    return f"{nombre_bebida} Mocktail"


def unique_chars(texto):
    return set(texto)


def sum_set(numeros):
   suma = 0
   for num in numeros:
       suma += num
   return suma


def common_elements(set_a, set_b):
    comunes = set()
    for elemento in set_a:
        if elemento in set_b:
            comunes.add(elemento)
    return comunes
