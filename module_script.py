import os
import time
import json
import keyboard

import config
import main_script

read_modules_json = open(config.MODULES_JSON_PATH, "r")
read_data_modules = json.load(read_modules_json)

def modules_menu():
    os.system('clear')
    print("\n============== MODULES MENU ==============\n")
    print("  >> Press [1] to Display List of Modules")
    print("  >> Press [2] to Add a New Module")
    print("  >> Press [3] to Edit a Module")
    print("  >> Press [4] to Delete a Module")
    print("  >> Press [5] to Save Module List as .txt")
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
            elif key == "5":
                modules_save_txt()
                break
            elif key == "r":
                main_script.main()
                break
            else:
                print("Invalid key! Choose a number/letter from the Menu.")


def modules_list():
    os.system('clear')
    print("\n============ LIST OF MODULES ===========\n")

    moduleID_width = 10
    moduleName_width = 30

    # formarting table header
    print(f"{'Module ID':<{moduleID_width}} {'Module Name':<{moduleName_width}}")
    print("-" * (moduleID_width + moduleName_width))

    # display list of modules in a table format
    for index, module in enumerate(read_data_modules, start = 1):
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


def modules_add():
    os.system('clear')
    print("\n============ ADD NEW MODULE ============\n")

    if len(read_data_modules) >= 4:
        os.system('clear')
        print("\n==================== WARNING ====================\n")
        print("  >> You cannot add more modules.")
        print("  >> The maximum number of modules is 4.\n")
        print("  Press [R] to return to Modules Menu.")
        
        while True:
            key_press = keyboard.read_event(suppress=True)
            if key_press.event_type == "down":
                key = key_press.name.lower()
                if key == "r":
                    modules_menu()
                    break
                else:
                    print("Invalid key! Press [R] to return to Modules Menu.")
        return

    new_module_name = input("  >>> Module name: ")
    newID = "M" + f"{len(read_data_modules) + 1}"
    
    # create the new module structure
    new_module = {
        "moduleID": newID,
        "module": new_module_name
    }

    # add the new module
    read_data_modules.append(new_module)

    # save the updated data to the json file
    with open(config.MODULES_JSON_PATH, "w") as write_json:
        json.dump(read_data_modules, write_json, indent=4)

    os.system('clear')
    print("\n================== STATUS ==================\n")
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


def modules_edit():
    os.system('clear')
    print("\n========== CHOOSE A MODULE TO EDIT ==========\n")

    # display list of modules
    for index, module in enumerate(read_data_modules, start = 1):
        print(f"  >> Press [{index}] to edit: {module['module']} (M{index})")

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

                if index >= 0 and index < len(read_data_modules):
                    os.system('clear')
                    print("\n=============== EDIT A MODULE ===============\n")
                    print(f"  >> Module to update: \"{read_data_modules[index]['module']}\"\n")
                    
                    update_mod_name = input("  >>> New module name: ")
                    print(f"\n  >>> Confirm change to: \"{update_mod_name}\"? [Y/N]")

                    while True:
                        confirm_key = keyboard.read_event(suppress=True)

                        if confirm_key.event_type == "down":
                            confirm = confirm_key.name.lower()

                            if confirm == "y":
                                read_data_modules[index]['module'] = update_mod_name
                                with open(config.MODULES_JSON_PATH, "w") as write_json: # this opens and close the file
                                    json.dump(read_data_modules, write_json)

                                os.system('clear')
                                print("\n===================== STATUS =====================\n")
                                print(f"  >> Module name successfully updated to: \"{update_mod_name}\"")

                            elif confirm == "n":
                                os.system('clear')
                                print("\n================== STATUS ==================\n")
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


def modules_delete():
    os.system('clear')
    print("\n============ CHOOSE A MODULE TO DELETE ============\n")

    # display list of modules
    for index, module in enumerate(read_data_modules, start=1):
        print(f"  >> Press [{index}] to delete: {module['module']} (M{index})")

    print("\n  Press [R] to return to Modules Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True) 
        
        if key_press.event_type == "down":
            key = key_press.name.lower()

            if key.isdigit():
                index = int(key) - 1

                if index >= 0 and index < len(read_data_modules):
                    os.system('clear')
                    print(f"\n================== DELETE MODULE ==================\n")
                    print(f"  >> Module to delete: {read_data_modules[index]['module']} (M{index + 1})\n")
                    
                    # ssk for confirmation before deleting
                    print(f"  >>> Confirm deletion of \"{read_data_modules[index]['module']}\" (M{index + 1}) module? [Y/N]")
                    
                    while True:
                        confirm_key = keyboard.read_event(suppress=True)
                        if confirm_key.event_type == "down":
                            confirm = confirm_key.name.lower()

                            if confirm == "y":
                                deleted_module = read_data_modules.pop(index)
                                with open(config.MODULES_JSON_PATH, "w") as write_json:
                                    json.dump(read_data_modules, write_json)

                                os.system('clear')
                                print("\n====================== STATUS =====================\n")
                                print(f"  >> Module \"{deleted_module['module']}\" successfully deleted.")
                                break
                            elif confirm == "n":
                                os.system('clear')
                                print("\n====================== STATUS =====================\n")
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


def modules_save_txt():
    os.system('clear')

    moduleID_width = 10
    moduleName_width = 20

    with open(config.MODULES_TXT_PATH, "w") as txt_file:
        txt_file.write("======= List of Modules =======\n")
        txt_file.write(f"\n{'Module ID':<{moduleID_width}} {'Module Name':<{moduleName_width}}\n")
        txt_file.write("-" * (moduleID_width + moduleName_width) + "\n")
        
        for module in read_data_modules:
            txt_file.write(f"{module['moduleID']:<{moduleID_width}} {module['module']:<{moduleName_width}}\n")

    os.system('clear')
    print("\n==================== STATUS ====================\n")
    print(f"  >> Module list successfully saved to {config.MODULES_TXT_PATH}")
    print("\n  Press [R] to return to Modules Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True)
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "r":
                modules_menu()
                break
            else:
                print("Invalid key! Press [R] to return to Modules Menu.")


def module_script():
    modules_menu()
    modules_add()
    modules_edit()
    modules_delete()
    modules_save_txt()