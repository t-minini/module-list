import json
import keyboard
import os
import time


modules_json_path = r"C:\Users\TulioMinini(Tallaght\Desktop\procedural-programming\module_list\modules.json"
read_json = open(modules_json_path, "r")
read_data_json = json.load(read_json)

# write_json = open(modules_json_path, 'w')
# write_data_json = json.dump(read_data_json, write_json)


def main_menu():
    os.system('clear')
    print("\n==================== MAIN MENU ====================")
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


def modules_menu():
    os.system('clear')
    print("\n==================== MODULES MENU ====================\n")
    print("  >> Press [1] to Display List of Modules")
    print("  >> Press [2] to Add a New Module")
    print("  >> Press [3] to Edit a Module")
    print("  >> Press [4] to Delete a Module")
    print("\n  Press [R] to return to Main Menu.")


    while True:
        key_press = keyboard.read_event(suppress=True) 
    

        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "1":
                modules_list()
                break
            elif key == "2":
                modules_add()
                break
            elif key == "3":
                modules_edit()
                break
            elif key == "4":
                modules_delete()
                break
            elif key == "r":
                main_menu()
                break
            else:
                print("Invalid key! Choose a number/letter from the Menu.")


def modules_list():
    os.system('clear')
    print("\n==================== LIST OF MODULES ====================\n")

    moduleID_width = 10
    moduleName_width = 30

    # formarting table header
    print(f"{'Module ID':<{moduleID_width}} {'Module Name':<{moduleName_width}}")
    print("-" * (moduleID_width + moduleName_width))

    # display list of modules in a table format
    for index, module in enumerate(read_data_json, start = 1):
        print(f"{module['moduleID']:<{moduleID_width}} {module['module']:<{moduleName_width}}")

    print("\nPress [R] to return to Modules Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "r":
                modules_menu()
                break
            else:
                print("Invalid key! Click [R] to return Modules Menu.")

# new
def modules_edit():
    os.system('clear')
    print("\n==================== CHOOSE A MODULE TO EDIT ====================\n")

    # display list of modules
    for index, module in enumerate(read_data_json, start = 1):
        print(f"  >> Press [{index}] to update Module {index}: \"{module['module']}\"")

    print("\n  Press [R] to return to Modules Menu.")

    while True:
        # this waits for user input
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            
            if key.isdigit():
                index = int(key) - 1

                if key == "r":
                    modules_menu()
                    return

                if index >= 0 and index < len(read_data_json):
                    os.system('clear')
                    print("\n==================== UPDATE A MODULE ====================\n")
                    print(f"  >> Module to update: \"{read_data_json[index]['module']}\"\n")
                    
                    update_mod_name = input("  >>> Please, enter a new module name: ")
                    print(f"\n  >>> Confirm change to: \"{update_mod_name}\"? [Y/N]")

                    while True:
                        confirm_key = keyboard.read_event(suppress=True)

                        if confirm_key.event_type == "down":
                            confirm = confirm_key.name.lower()

                            if confirm == "y":
                                read_data_json[index]['module'] = update_mod_name
                                with open(modules_json_path, "w") as write_json: # this opens and close the file
                                    json.dump(read_data_json, write_json)

                                os.system('clear')
                                print("\n======================== STATUS =======================\n")
                                print(f"  >> Module name successfully updated to: \"{update_mod_name}\"")

                            elif confirm == "n":
                                os.system('clear')
                                print("\n======================== STATUS =======================\n")
                                print("  >> Update cancelled.")
                            else:
                                print("Invalid choice! Press [Y] to confirm or [N] to cancel.")
                                continue
                            
                            print("\n  Press [R] to return to List of Modules.")
                            time.sleep(0.1)
                            while True:
                                key_press = keyboard.read_event(suppress=True) 
    
                                if key_press.event_type == "down":
                                    key = key_press.name.lower()
                                    if key == "r":
                                        modules_list()
                                        return
                                else:
                                        print("Invalid key! Click [R] to return Modules Menu.")
                else:
                    print("Invalid key! Choose a number/letter from the Menu.")

# new
def modules_add():
    os.system('clear')
    print("\n==================== ADD NEW MODULE ====================\n")

    new_module_name = input("  >>> Please, enter the name of the new module: ")
    newID = "M" + f"{len(read_data_json) + 1}"
    
    # create the new module structure
    new_module = {
        "moduleID": newID,
        "module": new_module_name
    }

    # add the new module
    read_data_json.append(new_module)

    # save the updated data to the json file
    with open(modules_json_path, "w") as write_json:
        json.dump(read_data_json, write_json, indent=4)

    os.system('clear')
    print("\n======================== STATUS =======================\n")
    print(f"  >> New module \"{new_module_name}\" successfully added!")

    print("\n  Press [R] to return to Modules Menu.")
    while True:
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "r":
                modules_menu()
                break
            else:
                print("Invalid key! Press [R] to return Modules Menu.")


def modules_delete():
    os.system('clear')
    print("\n==================== CHOOSE A MODULE TO DELETE ====================\n")

    # display list of modules
    for index, module in enumerate(read_data_json, start=1):
        print(f"  >> Press [{index}] to delete Module {index}: \"{module['module']}\"")

    print("\n  Press [R] to return to Modules Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True) 
        
        if key_press.event_type == "down":
            key = key_press.name.lower()

            if key.isdigit():
                index = int(key) - 1

                if index >= 0 and index < len(read_data_json):
                    os.system('clear')
                    print(f"\n==================== DELETE MODULE ====================\n")
                    print(f"  >> Module to delete: \"{read_data_json[index]['module']}\"\n")
                    
                    # ssk for confirmation before deleting
                    print(f"  >>> Are you sure you want to delete the \"{read_data_json[index]['module']}\" module? [Y/N]")
                    
                    while True:
                        confirm_key = keyboard.read_event(suppress=True)
                        if confirm_key.event_type == "down":
                            confirm = confirm_key.name.lower()

                            if confirm == "y":
                                deleted_module = read_data_json.pop(index)
                                with open(modules_json_path, "w") as write_json:
                                    json.dump(read_data_json, write_json)

                                os.system('clear')
                                print("\n======================== STATUS =======================\n")
                                print(f"  >> Module \"{deleted_module['module']}\" successfully deleted.")
                                break
                            elif confirm == "n":
                                os.system('clear')
                                print("\n======================== STATUS =======================\n")
                                print("  >> Deletion cancelled.")
                                break
                            else:
                                print("Invalid choice! Press [Y] to confirm or [N] to cancel.")
                                continue
                    
                    print("\n  Press [R] to return to List of Modules.")
                    time.sleep(0.1)
                    while True:
                        key_press = keyboard.read_event(suppress=True) 
                        if key_press.event_type == "down":
                            key = key_press.name.lower()
                            if key == "r":
                                modules_list()
                                return
                        else:
                            print("Invalid key! Press [R] to return to List of Modules.")
                else:
                    print("Invalid number! Choose a number corresponding to a module.")
            else:
                print("Invalid key! Choose a number/letter from the Menu.")



# new
def learners_menu():
    os.system('clear')
    print("\n==================== LEARNERS ====================\n")
    print("  >> Press [1] to Display List of Students")
    print("  >> Press [2] to Add a New Student")
    print("  >> Press [3] to Edit a Student")
    print("  >> Press [4] to Delete a Student")
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


# OLD 

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