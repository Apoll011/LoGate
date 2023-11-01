from general import *

class Prositions:
    
    PREFIX_MAP = {
        PropositionType.Simple: "é",
        PropositionType.Categoric: "sou",
        PropositionType.Conditional: "se",
        PropositionType.Bicondicional: "se e somente se",
        PropositionType.Disjunctive: "ou",
        PropositionType.Conjunct: "e",
        PropositionType.Negative: "não é",
    }
    
    @staticmethod
    def simple(NodeDict, phrase):
        if Prositions.valid(phrase):
            nod = Node()
            nod.define(phrase, PropositionType.Simple, "é", quality=get_quality(phrase))
            NodeDict.convert(nod)

    @staticmethod
    def conditional(NodeDict, phrase):
        if Prositions.valid(phrase):
            nod = Node()
            nod.define(phrase, PropositionType.Conditional, "se", quality=get_quality(phrase))
            NodeDict.convert(nod)

    @staticmethod
    def biconditional(NodeDict, phrase):
        if Prositions.valid(phrase):
            nod = Node()
            nod.define(phrase, PropositionType.Bicondicional, "se e somente se", quality=get_quality(phrase))
            NodeDict.convert(nod)

    @staticmethod
    def disjunctive(NodeDict, phrase):
        if Prositions.valid(phrase):
            nod = Node()
            nod.define(phrase, PropositionType.Disjunctive, "ou", quality=get_quality(phrase))
            NodeDict.convert(nod)

    @staticmethod
    def conjunct(NodeDict, phrase):
        if Prositions.valid(phrase):
            nod = Node()
            nod.define(phrase, PropositionType.Conjunct, "e", quality=get_quality(phrase))
            NodeDict.convert(nod)
    
    @staticmethod
    def categoric(NodeDict:Graph, phrase:Phrase):
        if Prositions.valid(phrase):
            phrase.text = remove_stopWords(phrase.text, ["são"])
            nod = Node()
            nod.define(phrase, PropositionType.Simple, " ", quantity=get_quantity(text=phrase))
            NodeDict.convert(nod)
    
    @staticmethod
    def negative(NodeDict:Graph, phrase:Phrase):
        if Prositions.valid(phrase):
            nod = Node()
            nod.define(phrase, PropositionType.Negative, "não", quality=Quality.Negatives)
            NodeDict.convert(nod)
    
    @staticmethod
    def valid(phrase:Phrase) -> bool:
        if phrase is not None and phrase.text is not None and phrase.text != "":
            return True
        return False 
