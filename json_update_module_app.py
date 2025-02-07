import json
import keyboard
import os


modules_json_path = r"C:\Users\TulioMinini(Tallaght\Desktop\procedural-programming\module_list\modules.json"
read_json = open(modules_json_path, "r")
read_data_json = json.load(read_json)

# write_json = open(modules_json_path, 'w')
# write_data_json = json.dump(read_data_json, write_json)


def main_menu():
    os.system('clear')
    print("\n==================== MENU ====================")
    print("\n  >> Press [1] to Modules")
    print("  >> Press [2] to Learners")
    print("  >> Press [3] to Results")
    print("\n  Press [X] to close application.")

    

    while True:
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "1":
                modules_menu()
                break
            elif key == "2":
                learners_menu()
                break
            elif key == "3":
                results_menu()
                break
            elif key == "x":
                close_app()
            else:
                print("Invalid key! Choose a number/letter from the Menu.")

# new
def modules_menu():
    os.system('clear')
    print("\n==================== MODULES ====================\n")
    print("  >> Press [1] to Display List of Modules")
    print("  >> Press [2] to Display Edit a Module")
    print("  >> Press [3] to Display Add a New Module")
    print("\n  Press [M] to return to Main Menu.")


# new
def modules_list():
    pass

# new
def learners_menu():
    os.system('clear')
    print("\n==================== LEARNERS ====================\n")
    print("  >> Press [1] to Display List of Students")
    print("  >> Press [2] to Display Edit a Student")
    print("  >> Press [3] to Display Add a New Student")
    print("\n  Press [M] to return to Main Menu.")


# new
def learners_list():
    pass

# new
def results_menu():
    os.system('clear')
    print("\n==================== RESULTS ====================\n")
    print("  >> RESULTS 1")
    print("  >> RESULTS 2")
    print("  >> RESULTS 3")
    print("\n  Press [M] to return to Main Menu.")

# new
def close_app():
    os.system('clear')
    exit()


# new
def return_main_menu():
    os.system('clear')
    main_menu()






def print_json():
    os.system('clear')
    print("\n==================== MODULES ====================\n")
    print("  >> Press [1] to Display List of Modules")
    print("  >> Press [2] to Display Edit a Module")
    print("  >> Press [3] to Display Add a New Module")
    print("\n  Press [M] to return to Main Menu.")
    for index, module in enumerate(read_data_json):
        print(f"  >> {index}: {module['module']}")

    return_or_close()

def return_or_close():
    print("\n  Press [M] to return to Main Menu.")
    print("  Press [X] to close application.")

    while True:
        key_press = keyboard.read_event(suppress=True) 

        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "m":
                main_menu()
            elif key == "x":
                os.system('clear')
                exit()
            else:
                print("Invalid key! Choose a letter from the Menu.")


def update_json():
    os.system('clear')
    print("\n==================== CHOOSE MODULE ====================\n")
    
    for index, module in enumerate(read_data_json):
        print(f"  >> Press [{index}] to update \"{module['module']}\" module.")
    
    print("\n  Press [M] to return to Main Menu.")

    # return_or_close()

    while True:
        key_press = keyboard.read_event(suppress=True)
        # print("\n  Press [R] to return.")

        if key_press.event_type == "down":
            key = key_press.name
            

            if key.isdigit():
                index = int(key)
                # print("\n  Press [R] to return.")

                if index >= 0 and index < len(read_data_json):
                    os.system('clear')
                    print("\n  Press [R] to return.")
                    print("\n==================== UPDATE MODULE ====================\n")
                    print(f"  >> Module to update: \"{read_data_json[index]['module']}\"\n")
                    
                    update_mod_name = input("  >>> Please, enter a new module name: ")
                    print(f"\n  >>> Confirm change to: \"{update_mod_name}\"? [Y/N]")

                    
                    

                    while True:
                        confirm_key = keyboard.read_event(suppress=True)

                        if confirm_key.event_type == "down":
                            confirm = confirm_key.name.lower()

                            if confirm == "y":
                                read_data_json[index]['module'] = update_mod_name
                                write_json = open(modules_json_path, "w")
                                json.dump(read_data_json, write_json)
                                write_json.close()

                                os.system('clear')
                                print("\n==================== STATUS ====================\n")
                                print(f"  >> Module name successfully updated to: \"{update_mod_name}\"\n")
                                return_or_close()
                                return
                            
                            elif confirm == "n":
                                print("\n==================== STATUS ====================\n")
                                print("  >> Update cancelled.")
                                return_or_close()
                                return
                            elif confirm == "r":
                                print("\nReturning to the module list...")
                                update_json()  # Go back to the module selection screen
                                return
                            else:
                                print("Invalid choice! Press [Y] to confirm or [N] to cancel.")
                else:
                    print("\nINVALID CHOICE!! Pleas,e select a number from the list above.")
            elif key == "r":
                update_json()
            elif key == "m":
                main_menu()
            else:
                print("\nINVALID CHOICE!!! Please, enter a number from the list above.")



def delete_json():
    pass


def main():
    main_menu()


main()