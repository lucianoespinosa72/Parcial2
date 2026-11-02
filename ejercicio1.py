from random import shuffle

from pokemon_data import pokemons
from tree import BinaryTree


arbol_nombre = BinaryTree()
arbol_numero = BinaryTree()
arbol_tipo = BinaryTree()

# carga aleatoria de los pokemons
shuffle(pokemons)
print(f'cantidad de pokemons cargados: {len(pokemons)}')

for pokemon in pokemons:
    arbol_nombre.insert_node(pokemon['nombre'], pokemon)
    arbol_numero.insert_node(pokemon['numero'], pokemon)
    # en el arbol de tipos cada nodo guarda la lista de pokemons de ese tipo
    for tipo in pokemon['tipos']:
        node = arbol_tipo.search(tipo)
        if node is None:
            arbol_tipo.insert_node(tipo, [pokemon])
        else:
            node.other_values.append(pokemon)

# A - mostrar datos por numero y por nombre (busqueda por proximidad)
print()
numero = 94
node = arbol_numero.search(numero)
if node is not None:
    print(f'pokemon numero {numero}: {node.other_values}')
else:
    print(f'no existe el pokemon numero {numero}')

print()
search_str = 'bul'
print(f'pokemons que contienen "{search_str}":')
arbol_nombre.proxy_search_show_values(search_str)

# B - nombres de los pokemons de un determinado tipo
for tipo in ['fantasma', 'fuego', 'acero', 'electrico']:
    print()
    print(f'pokemons de tipo {tipo}:')
    node = arbol_tipo.search(tipo)
    if node is not None:
        for pokemon in node.other_values:
            print(pokemon['nombre'])

# C - listados ascendentes por numero y nombre, y por nivel por nombre
print()
print('listado por numero:')
arbol_numero.inorden_show_values()

print()
print('listado por nombre:')
arbol_nombre.inorden_show_values()

print()
print('listado por nivel por nombre:')
arbol_nombre.by_level_show_values()

# D - pokemons debiles frente a Jolteon, Lycanroc y Tyrantrum
for nombre in ['Jolteon', 'Lycanroc', 'Tyrantrum']:
    print()
    node = arbol_nombre.search(nombre)
    if node is not None:
        tipos = node.other_values['tipos']
        print(f'pokemons debiles frente a {nombre} ({", ".join(tipos)}):')
        arbol_nombre.inorden_weak_against(tipos)

# E - tipos de pokemons y cuantos hay de cada uno
print()
print('cantidad de pokemons por tipo:')
arbol_tipo.inorden_count_values()

# F - cantidad de pokemons con megaevolucion
print()
print(f'cantidad de pokemons con megaevolucion: {arbol_nombre.count_by_field("mega")}')

# G - cantidad de pokemons con forma gigamax
print(f'cantidad de pokemons con forma gigamax: {arbol_nombre.count_by_field("gigamax")}')
