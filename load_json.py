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
    print("############################ Starting copy of all keywords into local dictionary!")
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
                    #print("adding ", value[word], " to the command...")
                    main_keywords[new_command].append(value[word])
    print("############################ Copy Finished!")

store_all_keywords()

#print("Here are ALL the keywords:- ", main_keywords)

def parse_search(query):
    print("")
    #Splits query words and also strips the whitespace
    query_words = [q.strip() for q in query.split(",")]
    #print(query_words)

    for command in main_keywords:
        for command_words in main_keywords[command]:
            for user_word in query_words:
                #print("comparing", user_word, " with ", command_words)
                if user_word == command_words:
                    #print("MATCHED the word ", user_word, " with command => ", command)
                    print(f"Command: \"{command}\":\nKeywords: {main_keywords[command]}\n")
                    query_words.remove(user_word)
    if len(user_word) > 0:
        print(f"Unfortunately {', '.join(query_words)}, did not match any results in the database.\n")



def start_search():
    while True:
        query = str(input("What would you like to do today?\n > "))

        if query == "":
            print("You have not searched for anything")
        elif query in ["exit","q","quit"]:
            print("Goodbye!")
            break
        else:
            parse_search(query)

print (main_keywords)
start_search()