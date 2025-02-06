import json
import keyboard
import os


modules_json_path = r"C:\Users\TulioMinini(Tallaght\Desktop\procedural-programming\module_list\modules.json"
read_json = open(modules_json_path, "r")
read_data_json = json.load(read_json)


def menu():
    os.system('clear')
    print("\n==================== MENU ====================")
    print("\n  >> Press [1] to display a list of modules.")
    print("  >> Press [2] to update a module.")
    print("\n  Press [X] to close application.")

    

    while True:
        key_event = keyboard.read_event(suppress=True) 
    
        if key_event.event_type == "down":
            key = key_event.name
            if key == "1":
                print_json()
                break
            elif key == "2":
                update_json()
                break
            elif key == "x":
                os.system('clear')
                exit()
            else:
                print("Invalid key! Choose a number/letter from the Menu.")



def print_json():
    os.system('clear')
    print("\n==================== LIST OF MODULES ====================\n")
    for index, module in enumerate(read_data_json):
        print(f"  >> {index}: {module['module']}")

    return_or_close()

def return_or_close():
    print("\n  Press [M] to return to Menu.")
    print("  Press [X] to close application.")

    while True:
        key_event = keyboard.read_event(suppress=True) 

        if key_event.event_type == "down":
            key = key_event.name
            if key == "m":
                menu()
            elif key == "x":
                os.system('clear')
                exit()
            else:
                print("Invalid key! Choose a letter from the Menu.")


def update_json():
    os.system('clear')
    print("\n==================== CHOOSE MODULE ====================")
    # print("\n  Please, select the module number you want to update:\n")
    
    key_event = keyboard.read_event(suppress=True) 

    for index, module in enumerate(read_data_json):
        print(f"  >> Press [{index}] to update \"{module['module']}\" module.")
        if key_event.event_type == "down":
            key = key_event.name
            if key == index:
                print("WELL DONE!")
            elif key == "x":
                os.system('clear')
                exit()
            else:
                print("ATTENTION! Invalid choice. Please, select a number from the list above.")

    # select_index = int(input())

    return_or_close()


def delete_json():
    pass


def main():
    menu()


main()