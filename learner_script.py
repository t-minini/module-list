import os
import time
import json
import keyboard

import config
import main_script

read_learners_json = open(config.LEARNERS_JSON_PATH, "r")
read_data_learners = json.load(read_learners_json)

read_modules_json = open(config.MODULES_JSON_PATH, "r")
read_data_modules = json.load(read_modules_json)

def learners_menu():
    os.system('clear')
    print("\n============== LEARNERS MENU ==============\n")
    print("  >> Press [1] to Display List of Learners")
    print("  >> Press [2] to Add a New Learner")
    print("  >> Press [3] to Delete a Learner")
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
                learners_delete()
                break
            elif key == "r":
                main_script.main()
                break
            else:
                print("Invalid key! Choose a number/letter from the Menu.")


def learners_list():
    os.system('clear')
    print("\n============= LIST OF LEARNERS =============\n")

    learnerID_width = 12
    learnerFName_width = 12
    learnerLName_width = 12
    learnerAge_width = 7

    # formarting table header
    print(f"{'Learner ID':<{learnerID_width}} {'First Name':<{learnerFName_width}} {'Last Name':<{learnerLName_width}} {'Age':<{learnerAge_width}}")
    print("-" * (learnerID_width + learnerFName_width + learnerLName_width + learnerAge_width))

    # display list of learners in a table format
    for learner in read_data_learners:
        print(f"{learner['learnerID']:<{learnerID_width}} {learner['firstName']:<{learnerFName_width}} {learner['lastName']:<{learnerLName_width}} {learner['age']:<{learnerAge_width}}")

    print("\nPress [R] to return to Learners Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "r":
                learners_menu()
                break
            else:
                print("Invalid key! Click [R] to return Learners Menu.")


def learners_add():
    os.system('clear')
    print("\n==================== ADD NEW LEARNER ====================\n")

    if len(read_data_learners) >= 8:
        os.system('clear')
        print("\n==================== WARNING ====================\n")
        print("  >> You cannot add more learners.")
        print("  >> The maximum number of learners is 8.\n")
        print("  Press [R] to return to Learners Menu.")
        
        while True:
            key_press = keyboard.read_event(suppress=True)
            if key_press.event_type == "down":
                key = key_press.name.lower()
                if key == "r":
                    learners_menu()
                    break
                else:
                    print("Invalid key! Press [R] to return to Learners Menu.")
        return
    
    newID = "L" + f"{len(read_data_learners) + 1}"
    new_learner_FName = input("  >>> Learner's First Name: ")
    new_learner_LName = input("  >>> Learner's Last Name: ")
    new_learner_age = int(input("  >>> Learner's Age: "))
    
    def get_valid_grade(module, moduleID):
        while True:
            try:
                grade = int(input(f"  >>> Results for {module} ({moduleID}): "))
                if grade >= 0 and grade <= 100:
                    return grade
                else:
                    print("  >>> Invalid grade! Please enter a grade between 0 and 100.")
            except:
                print("  >>> Invalid input! Please enter a number.")

    # Get valid grades for each module
    new_learner_res1 = get_valid_grade(read_data_modules[0]['module'], read_data_modules[0]['moduleID'])
    new_learner_res2 = get_valid_grade(read_data_modules[1]['module'], read_data_modules[1]['moduleID'])
    new_learner_res3 = get_valid_grade(read_data_modules[2]['module'], read_data_modules[2]['moduleID'])
    new_learner_res4 = get_valid_grade(read_data_modules[3]['module'], read_data_modules[3]['moduleID'])
    
    # create the new learner structure
    new_learner = {
        "learnerID": newID,
        "firstName": new_learner_FName,
        "lastName": new_learner_LName,
        "age": new_learner_age,
        "results": {
            "resultsModule1": new_learner_res1,
            "resultsModule2": new_learner_res2,
            "resultsModule3": new_learner_res3,
            "resultsModule4": new_learner_res4,
        }
    }

    # add the new learner
    read_data_learners.append(new_learner)

    # save the updated data to the json file
    with open(config.LEARNERS_JSON_PATH, "w") as write_json:
        json.dump(read_data_learners, write_json, indent=4)

    os.system('clear')
    print("\n======================== STATUS =======================\n")
    print(f"  >> New learner \"{new_learner_FName} {new_learner_LName}\" successfully added!")

    print("\n  Press [R] to return to Learners Menu.")
    while True:
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "r":
                learners_menu()
                break
            else:
                print("Invalid key! Press [R] to return Learners Menu.")



def learners_delete():
    os.system('clear')
    print("\n============ CHOOSE A LEARNER TO DELETE ============\n")

    # display list of modules
    for index, learner in enumerate(read_data_learners, start=1):
        print(f"  >> Press [{index}] to delete: {learner['firstName']} {learner['lastName']} ({learner['learnerID']})")

    print("\n  Press [R] to return to Learners Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True) 
        
        if key_press.event_type == "down":
            key = key_press.name.lower()

            if key.isdigit():
                index = int(key) - 1

                if index >= 0 and index < len(read_data_learners):
                    os.system('clear')
                    print(f"\n================== DELETE LEARNER ==================\n")
                    print(f"  >> Learner to delete: {read_data_learners[index]['firstName']} {read_data_learners[index]['lastName']} ({read_data_learners[index]['learnerID']})\n")
                    
                    # ssk for confirmation before deleting
                    print(f"  >>> Confirm deletion of \"{read_data_learners[index]['firstName']} {read_data_learners[index]['lastName']} ({read_data_learners[index]['learnerID']})\" learner? [Y/N]")
                    
                    while True:
                        confirm_key = keyboard.read_event(suppress=True)
                        if confirm_key.event_type == "down":
                            confirm = confirm_key.name.lower()

                            if confirm == "y":
                                deleted_learner = read_data_learners.pop(index)
                                with open(config.LEARNERS_JSON_PATH, "w") as write_json:
                                    json.dump(read_data_learners, write_json)

                                os.system('clear')
                                print("\n====================== STATUS =====================\n")
                                print(f"  >> Learner \"{deleted_learner['firstName']} {deleted_learner['lastName']}\" successfully deleted.")
                                break
                            elif confirm == "n":
                                os.system('clear')
                                print("\n====================== STATUS =====================\n")
                                print("  >> Deletion cancelled.")
                                break
                            else:
                                print("Invalid choice! Press [Y] to confirm or [N] to cancel.")
                                continue
                    
                    print("\n  Press [R] to return to List of Learners.")
                    time.sleep(0.1)
                    while True:
                        key_press = keyboard.read_event(suppress=True) 
                        if key_press.event_type == "down":
                            key = key_press.name.lower()
                            if key == "r":
                                learners_list()
                                return
                        else:
                            print("Invalid key! Press [R] to return to List of Learners.")
                else:
                    print("Invalid number! Choose a number corresponding to a Learner.")
            else:
                print("Invalid key! Choose a number/letter from the Menu.")


def learner_script():
    learners_menu()
    learners_list()
    learners_add()
    learners_delete()
