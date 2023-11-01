import spacy
from general import PropositionType, Phrase, Graph
from logic import Prositions
import re

nlp = spacy.load("pt_core_news_sm")

def classify_proposition_spacy(phrase:Phrase):
    doc = nlp(phrase.text)

    for token in doc:
        if token.dep_ == "cop":
            if token.text == "é":
                return PropositionType.Simple
            elif token.text == "sou":
                return PropositionType.Categoric
        elif token.dep_ == "acl:relcl":
            if token.text == "é":
                return PropositionType.Bicondicional
        elif token.dep_ == "nsubj":
            if token.text == "é":
                return PropositionType.Conditional
        elif token.dep_ == "conj":
            if token.text == "é":
                return PropositionType.Disjunctive
        elif token.dep_ == "cc":
            if token.text == "e":
                return PropositionType.Conjunct
        elif token.dep_ == "neg" or token.dep_ == "advmod":
            if token.text == "não":
                return PropositionType.Negative

    return None



def classify_proposition(phrase:Phrase):
    text = phrase.text.lower()

    # Padrões de regex para diferentes tipos de proposições
    simple_pattern = r"(?i)\b(é)\b"
    categoric_pattern = r"(?i)\b(sou)\b"
    conditional_pattern = r"(?i)\b(se)\b"
    biconditional_pattern = r"(?i)\b(se e somente se)\b"
    disjunctive_pattern = r"(?i)\b(ou)\b"
    conjunct_pattern = r"(?i)\b(e)\b"
    negative_pattern = r"(?i)\b(não é)\b"

    if re.search(simple_pattern, text):
        return PropositionType.Simple
    elif re.search(categoric_pattern, text):
        return PropositionType.Categoric
    elif re.search(conditional_pattern, text):
        return PropositionType.Conditional
    elif re.search(biconditional_pattern, text):
        return PropositionType.Bicondicional
    elif re.search(disjunctive_pattern, text):
        return PropositionType.Disjunctive
    elif re.search(conjunct_pattern, text):
        return PropositionType.Conjunct
    elif re.search(negative_pattern, text):
        return PropositionType.Negative

    return None  # Retorna None se a frase não corresponder a nenhuma proposição aceita


def classify(pharse:Phrase, algorityhm = classify_proposition_spacy):
    return algorityhm(pharse)

def analyse_list(graph:Graph, list:list):
    index = 0
    for frase in list:
        result = classify(Phrase(frase, index, "main"))
        if result == PropositionType.Simple:
            Prositions.simple(graph, Phrase(frase, index, "main"))
        elif result == PropositionType.Categoric:
            Prositions.categoric(graph, Phrase(frase, index, "main"))
        elif result == PropositionType.Conditional:
            Prositions.conditional(graph, Phrase(frase, index, "main"))
        elif result == PropositionType.Bicondicional:
            Prositions.biconditional(graph, Phrase(frase, index, "main"))
        elif result == PropositionType.Disjunctive:
            Prositions.disjunctive(graph, Phrase(frase, index, "main"))
        elif result == PropositionType.Conjunct:
            Prositions.conjunct(graph, Phrase(frase, index, "main"))
        elif result == PropositionType.Negative:
            Prositions.negative(graph, Phrase(frase, index, "main"))
        index += 1