import gzip
import pandas as pd
import json


class DataManager:
    def __init__(self):
        self.jewels = {"Glorious Vanity" : {"type_no": 1, "minSeed": 100, "maxSeed": 8000, "seedIncrement": 1, "data": ""},
            "Lethal Pride" : {"type_no": 2, "minSeed": 10000, "maxSeed": 18000, "seedIncrement": 1, "data": ""},
            "Brutal Restraint" : {"type_no": 3, "minSeed": 500, "maxSeed": 8000, "seedIncrement": 1, "data": ""},
            "Militant Faith" : {"type_no": 4, "minSeed": 2000, "maxSeed": 10000, "seedIncrement": 1, "data": ""},
            "Elegant Hubris" : {"type_no": 5, "minSeed": 2000, "maxSeed": 160000, "seedIncrement": 20, "data": ""}
            }

        self.node_indices_name = pd.read_csv('jewel_data/node_indices.csv', index_col=1).to_dict('index')
        self.node_indices_graphid = pd.read_csv('jewel_data/node_indices.csv', index_col=0).to_dict('index')

        self.passive_additions = pd.read_json('jewel_data/alternate_passive_additions.json', orient='index').to_dict()
        self.passive_replacements = pd.read_json('jewel_data/alternate_passive_skills.json', orient='index').to_dict()

        f = open('jewel_data/jewel_node_link.json')
        self.jewel_node_link = json.load(f)

        for jewel in self.jewels:


            f=gzip.open(f'jewel_data/{jewel}.gz','rb')
            self.jewels[jewel]["data"]=f.read()


