import json
import os

#Define specific path dynamically so that it works on any machine the project is cloned on 
__location__ = os.path.realpath(
    os.path.join(
        os.getcwd(), os.path.dirname(__file__)
    )
)

#We open the json file and load it into a dictionary. 
#Note that in this prototype, we are opening the file for READ ONLY purposes as specified in the paramenters 'r'
with open(os.path.join(__location__, 'raw_data.json'), 'r') as json_file:
    all_commands = json.load(json_file)

#The way in which python handles deep nested dictionaries is as follows
#nested_child_info = master_dictionary['sub_categories'][sub_cat_name]['attributes'][attribute_name]['special_type']['nested_children'][child_cat_name]
# So we can now display the data however we wish

def show_all_available_commands():
    print('Here are a list of all the available commands:- ')
    for comm in all_commands["list_of_commands"]:
        for key, value in comm.items():
            if key == "command":
                print("{} : {}".format(key, value))

show_all_available_commands()