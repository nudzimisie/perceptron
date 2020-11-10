# from faker import Faker
from random import randint, choice
from importlib import import_module as get_module
from abc import ABC
import os, json, requests, csv

class NamesPrototype(ABC):
    def __init__(self):
        self.names = []
        self.names_popularity = []

    def load_csv(self, csv_file):
        with open(f'resources/{csv_file}', encoding='utf8') as csvfile:
            file_reader = csv.DictReader(csvfile)
            # print(len(list(file_reader)))
            for row in file_reader:
                name, popularity = tuple(row.values())
                self.names.append(name)
                self.names_popularity.append(popularity)

    def get_random(self, limit=None, start_index=0, reverse=False):
        if limit:
            name_index = randint(start_index, start_index + limit)
        else:
            name_index = randint(start_index, len(self.names))
        if reverse:
            name_index = -name_index
        return self.names[name_index]

class MaleNames(NamesPrototype):
    def __init__(self):
        super().__init__()
        self.load_csv('lista_imion_męskich.csv')

class FemaleNames(NamesPrototype):
    def __init__(self):
        super().__init__()
        self.load_csv('lista_imion_żeńskich.csv')

class MaleSurnames(NamesPrototype):
    def __init__(self):
        super().__init__()
        self.load_csv('wykaz_nazwisk_męskich.csv')

class FemaleSurnames(NamesPrototype):
    def __init__(self):
        super().__init__()
        self.load_csv('wykaz_nazwisk_żeńskich.csv')

data = {
    'Male': {
        'names': MaleNames(),
        'surnames': MaleSurnames()
    },
    'Female': {
        'names': FemaleNames(),
        'surnames': FemaleSurnames()
    }
}

class Person:
    def __init__(self):
        self.sex = choice([0, 1])
        self.sex_name = 'Male' if self.sex else 'Female'
        self.name = data[self.sex_name]['names'].get_random(100)
        self.surname = data[self.sex_name]['surnames'].get_random(100)

    def __str__(self):
        return f'{self.name} {self.surname}'
        

class Scenario:
    def __init__(self, associated, seen, acquaintance, positive, negative, possession, benefits, dna, fingerprints, traces, statements, others, guiltlessness):
        # powiązany z miejscem zbrodni
        self.associated = associated
        # widziany w pobliżu miejsca zbrodni
        self.seen = seen
        # znajomość z ofiarą
        self.acquaintance = acquaintance
        # pozytywne relacje z ofiarą (skala 0-10)
        self.positive = positive
        # negatywne relacje z ofiarą (skala 0-10)
        self.negative = negative
        # posiadanie rzeczy ofiary
        self.possession = possession
        # wymierne korzyści ze zdarzenia
        self.benefits = benefits
        # ślady dna na ciele ofiary
        self.dna = dna
        # odciski na narzędziu zbrodni
        self.fingerprints = fingerprints
        # ślady obecności na miejscu zbrodni
        self.traces = traces
        # obciążające zeznania świadków
        self.statements = statements
        # inne poszlaki dowodowe (liczba poszlak)
        self.others = others
        # poszlaki mogące świadczyć o niewinności (liczba poszlak)
        self.guiltlessness = guiltlessness

class CaseFiles:
    def __init__(self, scenarios, guilty):
        self.person = Person()
        self.scenario = choice(scenarios)
        self.guilty = guilty

guilty_scenarios = [
    Scenario(False, True, False, 0, 0, True, False, True, True, True, False, 3, 1),
    Scenario(False, True, True, 7, 0, True, False, True, True, True, True, 5, 2),
    Scenario(True, True, True, 9, 3, True, False, True, True, True, False, 3, 2),
    Scenario(True, True, True, 10, 4, True, True, True, True, True, False, 5, 2),
    Scenario(False, False, False, 0, 0, False, False, True, True, True, False, 1, 2),
    Scenario(False, False, False, 0, 0, False, False, False, False, True, False, 10, 1),
    Scenario(False, False, True, 0, 9, False, True, False, False, True, False, 1, 0),
    Scenario(True, True, False, 0, 0, True, False, True, True, True, False, 1, 0),
    Scenario(False, False, True, 0, 10, False, True, False, True, False, True, 0, 0),
    Scenario(True, True, True, 0, 7, True, True, True, True, True, True, 6, 0)
]

guiltlessness_scenarios = [
    Scenario(False, False, True, 7, 3, False, False, False, False, False, False, 3, 5),
    Scenario(False, True, True, 10, 1, True, False, True, True, True, True, 0, 5),
    Scenario(False, False, False, 0, 0, False, True, False, False, False, False, 0, 0),
    Scenario(False, True, False, 0, 0, False, False, False, False, False, True, 3, 2),
    Scenario(False, True, True, 5, 0, False, False, False, False, False, False, 0, 0),
    Scenario(True, True, True, 7, 0, True, False, False, False, False, True, 0, 4),
    Scenario(True, True, True, 10, 0, True, False, True, True, True, False, 0, 2),
    Scenario(True, False, True, 5, 2, False, False, False, False, False, False, 0, 0),
    Scenario(True, False, False, 0, 0, False, False, False, False, False, False, 0, 1),
    Scenario(True, True, True, 3, 0, True, False, False, True, True, False, 2, 4)
]

