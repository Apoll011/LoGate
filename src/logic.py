from general import Graph, Id, PropositionType, Quality
from match import Prositions

def logic(graph:Graph, input, exclude=[], index=0) -> list:
    
    Types = []
    
    i = Id()
    i.create(input.lower())
    node = graph.get(i)
    
    assert node is not None
    
    if node.id in exclude:
        return []
    for n in graph.conection:
        
        accepted = False
        text = ""
        
        prefix = Prositions.PREFIX_MAP.get(n.type, "")
        
        
        if node.id == n.A.key.id:
            
            text = n.P.name
            Types = Types + logic(graph=graph, input=n.P.name, exclude=exclude+[node.id], index=index+1)
            
            Types.append((prefix, text, index))
            
        elif node.id == n.P.key.id:
            if graph.get(n.A.key) is node:
                text = n.A.name
                Types = Types + logic(graph=graph, input=n.A.name, exclude=exclude+[node.id], index=index+1)
                Types.append((prefix, text, index))
        
    return filtrar_lista(Types)
        

def filtrar_lista(lista):
    filtrados = {}
    
    for item in lista:
        P, T, priority = item

        if (T, P) not in filtrados or priority < filtrados[(T, P)][2]:
            filtrados[(T, P)] = item

    resultado_filtrado = list(filtrados.values())
    return resultado_filtrado


