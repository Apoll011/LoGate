from enum import Enum 
from random import randint
import hashlib

class PropositionType(Enum):
    Simple = 0
    Categoric = 1
    Conditional = 2
    Bicondicional = 3
    Disjunctive = 4
    Conjunct = 5
    Negative = 6
    
class Quantity(Enum):
    nothing = 0
    Universal = 1
    Particular = 2

class Quality(Enum):
    nothing = -1
    Afirmatives = True
    Negatives = False

class Id:
    id:str = ""
    def create(self, name):
        # Use SHA-256 para criar um ID único a partir do nome
        sha256 = hashlib.sha256()
        sha256.update(name.encode('utf-8'))
        self.id = sha256.hexdigest()
    
    def __repr__(self) -> str:
        return self.id

class Point:
    
    key:Id
    
    def __init__(self, name: str):
        self.name = name
        self.key=Id()
        self.key.create(name)
    def __repr__(self) -> str:
        return f"Point of name: {self.name}"

class Phrase:
    def __init__(self, text, line, file) -> None:
        self.text = text.lower()
        
    def split(self, splitter):
        return self.text.split(splitter)


class Node:
    A:Point
    P:Point
    
    text:Phrase
    
    def define(self, pharse:Phrase, Ptype:PropositionType, splitter:str, entry = [0, -1], quantity:Quantity = Quantity.nothing, quality:Quality = Quality.nothing):
        self.type = Ptype
        Nlist = pharse.split(splitter)
        self.A = Point(procces_sentence(Nlist[entry[0]]))
        self.P = Point(procces_sentence(Nlist[entry[-1]]))
        self.quantity = quantity
        self.quality = quality
        self.text = pharse
        if quality == Quality.Negatives:
            self.type = PropositionType.Negative
    
    def __repr__(self) -> str:
        return  f"{self.A.name} --------{'-' if self.quality != Quality.Negatives else '!'}-------- {self.P.name}"

class Graph:
    points:dict[Id, Point] = {}
    conection:list[Node] = [] 
    
    def add(self, point:Point):
        for d in self.points:
            if point.key.id == d.id:
                return
        self.points[point.key] = point
        
        
    def get(self, id:Id):
        for item in self.points:
            if id.id == item.id:
                return item
        return None
            
    def create(self, node:Node):
        self.conection.append(node)
    
    def convert(self, node:Node):
        self.add(node.A)
        self.add(node.P)
        self.create(node)
    
    def __repr__(self) -> str:
        full_text = ""
        for item in self.conection:
            full_text += f"{item.A.name} --------{'-' if item.quality != Quality.Negatives else '!'}-------- {item.P.name}\n"
        
        return f"=============== The Points =================\n{self.points}\n============================================\n{full_text}"
        


def procces_sentence(text)-> str:
    s = remove_stopWords(text)
    return s

def remove_stopWords(text, StopWord = ["o", "a", "não", "sim", "alguns", "todos", "um", "uma", "é"]) -> str:
    return " ".join((list(filter(lambda x: x.lower() not in StopWord, text.split())))) # type: ignore

def get_quantity(text:Phrase) -> Quantity:
    listw = text.split(" ")
    u = ["todos"]
    p = ["alguns"]
    for item in listw:
        if item.lower() in u:
            return Quantity.Universal
        elif item.lower() in p:
            return Quantity.Particular
    return Quantity.nothing

def get_quality(text:Phrase) -> Quality:
    listw = text.split(" ")
    u = ["sim"]
    p = ["não"]
    for item in listw:
        if item.lower() in u:
            return Quality.Afirmatives
        if item.lower() in p:
            return Quality.Negatives
    return Quality.Afirmatives