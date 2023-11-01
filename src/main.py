from general import Graph
from logic import logic
from classify import *
from display import display

graph = Graph()

frases = [
    "O tiago é um ser Humano",
    "A Fibi é uma Gata",
    "Gata é um Gato fêmea",
    "Gato fêmea é um Gato",
    "Gato é um Animal de estimação",
    "Eu sou o Tiago",
    "Animal de Estimação é um Animal",
    "Fibi é Siames",
    "Fibi não é cão",
    "Siames é gato",
    "Fibi é a gata do Tiago",
    "Cão é um Animal",
    "Eu não gosto de Cebola",
    "A Programação não é biologica",
]

analyse_list(graph, frases)

print(graph)

while True:
    inpu = input("Point: ")
    for d in logic(graph=graph, input=inpu):
        display(inpu, d)