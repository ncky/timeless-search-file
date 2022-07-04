from DataManager import DataManager

class NotableSearch:
    def __init__(self):
        self.data = DataManager()


    def search(self, jewel_to_search, desired_node, jewel_seed):

        # jewel_to_search = "Elegant Hubris"#"Elegant Hubris"#"Lethal Pride"
        # desired_node = "Beef"
        # jewel_seed = 2000
        # print(f"jewel_seed {jewel_seed}")
        # print(f"jewel_to_search {jewel_to_search}")

        if type(desired_node) is str:
            node_id = self.data.node_indices_name[desired_node]['Datafile Parsing Index']
        if type(desired_node) is int: 
            node_id = self.data.node_indices_graphid[desired_node]['Datafile Parsing Index']
        # print(f"node_id_INDEX {node_id} ({desired_node})")

        js_size = int(((self.data.jewels[jewel_to_search]["maxSeed"] - self.data.jewels[jewel_to_search]["minSeed"])/self.data.jewels[jewel_to_search]["seedIncrement"])) + 1
        # print(f"jewel_seed_Size {js_size}")

        js_offset = int((jewel_seed - self.data.jewels[jewel_to_search]["minSeed"])/self.data.jewels[jewel_to_search]["seedIncrement"])
        # print(f"jewel_seed_offset {js_offset}")

        # print(f"array_index {node_id*js_size+js_offset}")
        output_id = self.data.jewels[jewel_to_search]["data"][node_id*js_size+js_offset]
        # print(f"index_of_Change {output_id}")



        if output_id == 249:
            print("No change")
        elif output_id > 93: 
            # print(f"index_of_Change {output_id}-94 ({passive_replacements[output_id - 94]['Id']})")
            # print(passive_replacements[output_id - 94]['Id'])
            return self.data.passive_replacements[output_id - 94]
        else:
            # print(f"index_of_Change {output_id} ({passive_additions[output_id]['Id']})")
            # print({passive_additions[output_id]['Id']})
            return self.data.passive_additions[output_id]



