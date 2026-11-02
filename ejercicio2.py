from graph import Graph


# episodios (I a IX) en los que aparece cada personaje
personajes = {
    'Luke Skywalker': [4, 5, 6, 7, 8, 9],
    'Darth Vader': [3, 4, 5, 6],
    'Yoda': [1, 2, 3, 5, 6, 8, 9],
    'Boba Fett': [2, 5, 6],
    'C-3PO': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'Leia': [4, 5, 6, 7, 8, 9],
    'Rey': [7, 8, 9],
    'Kylo Ren': [7, 8, 9],
    'Chewbacca': [3, 4, 5, 6, 7, 8, 9],
    'Han Solo': [4, 5, 6, 7, 9],
    'R2-D2': [1, 2, 3, 4, 5, 6, 7, 8, 9],
    'BB-8': [7, 8, 9],
    'Obi-Wan Kenobi': [1, 2, 3, 4, 5, 6],
    'Palpatine': [1, 2, 3, 5, 6, 9],
}

g = Graph(is_dir=False)

# A - cada vertice guarda el nombre, las aristas la cantidad de episodios compartidos
for nombre, episodios in personajes.items():
    g.add_vertex(nombre, {'episodes': episodios})

nombres = list(personajes.keys())
for i in range(len(nombres)):
    for j in range(i + 1, len(nombres)):
        compartidos = len(set(personajes[nombres[i]]) & set(personajes[nombres[j]]))
        if compartidos > 0:
            g.add_edge(compartidos, nombres[i], nombres[j])

# B - arbol de expansion minimo desde C-3PO, Yoda y Leia
for origen in ['C-3PO', 'Yoda', 'Leia']:
    min_tree = g.kruskal(origen)
    print(f'arbol de expansion minimo desde {origen}:')
    peso_total = 0
    for edge in min_tree.split(';'):
        origin, destination, weight = edge.split('|')
        print(f'  {origin} - {destination} ({weight})')
        peso_total += int(weight)
    print(f'peso total: {peso_total}')
    print()

# C - numero maximo de episodios compartidos y los pares que lo cumplen
max_episodios, pares = g.max_weight_edges()
print(f'numero maximo de episodios compartidos: {max_episodios}')
for origin, destination in pares:
    print(f'  {origin} - {destination}')
print()


# D - camino mas corto desde C-3PO a R2-D2 y desde Yoda a Darth Vader
def camino_mas_corto(origen, destino):
    if not g.exist_path(origen, destino):
        print(f'no existe camino entre {origen} y {destino}')
        return

    paths = g.dijkstra(origen)
    peso_total = None
    camino_completo = []
    while paths.size() > 0:
        value = paths.pop()
        if value[0] == destino:
            if peso_total is None:
                peso_total = value[1]
            camino_completo.append(value[0])
            destino = value[2]
    camino_completo.reverse()
    print(f'el camino mas corto es: {" -> ".join(camino_completo)} con un costo de {peso_total}')


camino_mas_corto('C-3PO', 'R2-D2')
camino_mas_corto('Yoda', 'Darth Vader')
print()

# E - personajes que aparecieron en los nueve episodios
print('personajes que aparecieron en los nueve episodios:')
for vertex in g:
    if len(vertex.other_values['episodes']) == 9:
        print(f'  {vertex.value}')
