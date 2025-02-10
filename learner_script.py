import os
import time
import json
import keyboard

import config
import main_script

read_json = open(config.LEARNERS_JSON_PATH, "r")
read_data_json = json.load(read_json)

def learners_menu():
    os.system('clear')
    print("\n==================== LEARNERS MENU ====================\n")
    print("  >> Press [1] to Display List of Learners")
    print("  >> Press [2] to Add a New Learner")
    print("  >> Press [3] to Edit a Learner")
    print("  >> Press [4] to Delete a Learner")
    print("\n  Press [R] to return to Main Menu.")


    while True:
        key_press = keyboard.read_event(suppress=True) 
    

        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "1":
                learners_list()
                break
            elif key == "2":
                learners_add()
                break
            elif key == "3":
                learners_edit()
                break
            elif key == "4":
                learners_delete()
                break
            elif key == "r":
                main_script.main()
                break
            else:
                print("Invalid key! Choose a number/letter from the Menu.")

def learners_add():
    pass

def learners_edit():
    pass

def learners_delete():
    pass

def learners_list():
    os.system('clear')
    print("\n==================== LIST OF LEARNERS ====================\n")

    learnerID_width = 12
    learnerFName_width = 12
    learnerLName_width = 12
    learnerAge_width = 6

    # formarting table header
    print(f"{'Learner ID':<{learnerID_width}} {'First Name':<{learnerFName_width}} {'Last Name':<{learnerLName_width}} {'Age':<{learnerAge_width}}")
    print("-" * (learnerID_width + learnerFName_width + learnerLName_width + learnerAge_width))

    # display list of modules in a table format
    for index, learner in enumerate(read_data_json, start = 1):
        print(f"{learner['learnerID']:<{learnerID_width}} {learner['firstName']:<{learnerFName_width}} {learner['lastName']:<{learnerLName_width}} {learner['age']:<{learnerAge_width}}")

    print("\nPress [R] to return to Modules Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "r":
                learners_menu()
                break
            else:
                print("Invalid key! Click [R] to return Modules Menu.")



# new
# def modules_edit():
#     os.system('clear')
#     print("\n==================== CHOOSE A MODULE TO EDIT ====================\n")

#     # display list of modules
#     for index, module in enumerate(read_data_json, start = 1):
#         print(f"  >> Press [{index}] to update Module {index}: \"{module['module']}\"")

#     print("\n  Press [R] to return to Modules Menu.")

#     while True:
#         # this waits for user input
#         key_press = keyboard.read_event(suppress=True) 
    
#         if key_press.event_type == "down":
#             key = key_press.name.lower()
            
#             if key.isdigit():
#                 index = int(key) - 1

#                 if key == "r":
#                     learners_menu()
#                     return

#                 if index >= 0 and index < len(read_data_json):
#                     os.system('clear')
#                     print("\n==================== UPDATE A MODULE ====================\n")
#                     print(f"  >> Module to update: \"{read_data_json[index]['module']}\"\n")
                    
#                     update_mod_name = input("  >>> Please, enter a new module name: ")
#                     print(f"\n  >>> Confirm change to: \"{update_mod_name}\"? [Y/N]")

#                     while True:
#                         confirm_key = keyboard.read_event(suppress=True)

#                         if confirm_key.event_type == "down":
#                             confirm = confirm_key.name.lower()

#                             if confirm == "y":
#                                 read_data_json[index]['module'] = update_mod_name
#                                 with open(modules_json_path, "w") as write_json: # this opens and close the file
#                                     json.dump(read_data_json, write_json)

#                                 os.system('clear')
#                                 print("\n======================== STATUS =======================\n")
#                                 print(f"  >> Module name successfully updated to: \"{update_mod_name}\"")

#                             elif confirm == "n":
#                                 os.system('clear')
#                                 print("\n======================== STATUS =======================\n")
#                                 print("  >> Update cancelled.")
#                             else:
#                                 print("Invalid choice! Press [Y] to confirm or [N] to cancel.")
#                                 continue
                            
#                             print("\n  Press [R] to return to List of Modules.")
#                             time.sleep(0.1)
#                             while True:
#                                 key_press = keyboard.read_event(suppress=True) 
    
#                                 if key_press.event_type == "down":
#                                     key = key_press.name.lower()
#                                     if key == "r":
#                                         modules_list()
#                                         return
#                                 else:
#                                         print("Invalid key! Click [R] to return Modules Menu.")
#                 else:
#                     print("Invalid key! Choose a number/letter from the Menu.")

# new
# def modules_add():
#     os.system('clear')
#     print("\n==================== ADD NEW MODULE ====================\n")

#     new_module_name = input("  >>> Please, enter the name of the new module: ")
#     newID = "M" + f"{len(read_data_json) + 1}"
    
#     # create the new module structure
#     new_module = {
#         "moduleID": newID,
#         "module": new_module_name
#     }

#     # add the new module
#     read_data_json.append(new_module)

#     # save the updated data to the json file
#     with open(modules_json_path, "w") as write_json:
#         json.dump(read_data_json, write_json, indent=4)

#     os.system('clear')
#     print("\n======================== STATUS =======================\n")
#     print(f"  >> New module \"{new_module_name}\" successfully added!")

#     print("\n  Press [R] to return to Modules Menu.")
#     while True:
#         key_press = keyboard.read_event(suppress=True) 
    
#         if key_press.event_type == "down":
#             key = key_press.name.lower()
#             if key == "r":
#                 modules_menu()
#                 break
#             else:
#                 print("Invalid key! Press [R] to return Modules Menu.")


# def modules_delete():
#     os.system('clear')
#     print("\n==================== CHOOSE A MODULE TO DELETE ====================\n")

#     # display list of modules
#     for index, module in enumerate(read_data_json, start=1):
#         print(f"  >> Press [{index}] to delete Module {index}: \"{module['module']}\"")

#     print("\n  Press [R] to return to Modules Menu.")

#     while True:
#         key_press = keyboard.read_event(suppress=True) 
        
#         if key_press.event_type == "down":
#             key = key_press.name.lower()

#             if key.isdigit():
#                 index = int(key) - 1

#                 if index >= 0 and index < len(read_data_json):
#                     os.system('clear')
#                     print(f"\n==================== DELETE MODULE ====================\n")
#                     print(f"  >> Module to delete: \"{read_data_json[index]['module']}\"\n")
                    
#                     # ssk for confirmation before deleting
#                     print(f"  >>> Are you sure you want to delete the \"{read_data_json[index]['module']}\" module? [Y/N]")
                    
#                     while True:
#                         confirm_key = keyboard.read_event(suppress=True)
#                         if confirm_key.event_type == "down":
#                             confirm = confirm_key.name.lower()

#                             if confirm == "y":
#                                 deleted_module = read_data_json.pop(index)
#                                 with open(modules_json_path, "w") as write_json:
#                                     json.dump(read_data_json, write_json)

#                                 os.system('clear')
#                                 print("\n======================== STATUS =======================\n")
#                                 print(f"  >> Module \"{deleted_module['module']}\" successfully deleted.")
#                                 break
#                             elif confirm == "n":
#                                 os.system('clear')
#                                 print("\n======================== STATUS =======================\n")
#                                 print("  >> Deletion cancelled.")
#                                 break
#                             else:
#                                 print("Invalid choice! Press [Y] to confirm or [N] to cancel.")
#                                 continue
                    
#                     print("\n  Press [R] to return to List of Modules.")
#                     time.sleep(0.1)
#                     while True:
#                         key_press = keyboard.read_event(suppress=True) 
#                         if key_press.event_type == "down":
#                             key = key_press.name.lower()
#                             if key == "r":
#                                 modules_list()
#                                 return
#                         else:
#                             print("Invalid key! Press [R] to return to List of Modules.")
#                 else:
#                     print("Invalid number! Choose a number corresponding to a module.")
#             else:
#                 print("Invalid key! Choose a number/letter from the Menu.")


def learner_script():
    learners_menu()
    learners_list


learner_script()