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

#show_all_available_commands()

#initiate list for storing all the main keywords
main_keywords = {}

def add_new_command(new_command_name):
    main_keywords[new_command_name] = []

def store_all_keywords():
    #make a list of all the keywords
    for comm in all_commands["list_of_commands"]:
        
        #To keep track of the current command so we can attach the keywords to them. Look at structure of JSON to understand why.
        new_command = None

        for key, value in comm.items():

            def update_command(para):
                #The way scopes work in Python, we need to pull in the global variable by declaring it as nonlocal
                #so it does not initiate it as a new local variable
                nonlocal new_command
                new_command = para

            if key == "command":
                #Update local scope
                update_command(value);
                print("Setting up new command => " , new_command)
                #Add to main_keywords dictionary using the function we made above
                add_new_command(new_command)

            if key == "keywords":
                word_length = len(value)
                for word in range(word_length):
                    print("adding ", value[word], " to the command...")
                    main_keywords[new_command].append(value[word])

store_all_keywords()

print("Here are ALL the keywords:- ", main_keywords)