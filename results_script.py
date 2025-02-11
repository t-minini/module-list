import os
import time
import json
import keyboard

import config
import main_script

def results_menu():
    os.system('clear')
    print("\n============== RESULTS MENU ==============\n")
    print("  >> Press [1] to Display Results")
    print("  >> Press [2] to Save Results as .txt file")
    print("\n  Press [R] to return to Main Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "1":
                results_list()
                break
            elif key == "2":
                save_txt()
                break
            elif key == "r":
                main_script.main()
                break
            else:
                print("Invalid key! Choose a number/letter from the Menu.")


def results_list():
    os.system('clear')

    with open("learners.json", "r") as file:
        learners = json.load(file)

    def get_grade(score):
        if isinstance(score, str):
            score = int(score)
        if score < 50:
            return "Unsuccessful"
        elif score >= 50 or score <= 64:
            return "Pass"
        elif score >= 65 or score <= 79:
            return "Merit"
        else:
            return "Distinction"

    def get_certification(results):
        grades = [get_grade(score) for score in results.values()]
        unsuccessful_count = grades.count("Unsuccessful")

        if unsuccessful_count == 0:
            return "Full Certification Achieved"
        elif unsuccessful_count == 4:
            return "No Certification Achieved"
        else:
            return "Partial Certification Achieved"

    print("\n======================================================== RESULTS ========================================================\n")
    print(f"{'Learner ID':<10} {'Name':<15} {'Module 1':<15} {'Module 2':<15} {'Module 3':<15} {'Module 4':<15} {'Certification':<35}")
    print("=" * 121)

    for learner in learners:
        learner_id = learner["learnerID"]
        name = f"{learner['firstName']} {learner['lastName']}"

        results = {
            "resultsModule1": int(learner["results"].get("resultsModule1", 0)),
            "resultsModule2": int(learner["results"].get("resultsModule2", 0)),
            "resultsModule3": int(learner["results"].get("resultsModule3", 0)),
            "resultsModule4": int(learner["results"].get("resultsModule4", 0)),
        }

        grades = [get_grade(score) for score in results.values()]
        certification = get_certification(results)

        print(f"{learner_id:<10} {name:<15} {grades[0]:<15} {grades[1]:<15} {grades[2]:<15} {grades[3]:<15} {certification:<35}")

    print("\nPress [R] to return to Results Menu.")
    while True:
        key_press = keyboard.read_event(suppress=True) 
    
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "r":
                results_menu()
                break
            else:
                print("Invalid key! Click [R] to return Learners Menu.")


# NOT WORKING!!!!
def save_txt():
    os.system('clear')

    # Reading learners data from the JSON file
    with open(config.RESULTS_TXT_PATH, "r") as file:
        learners = json.load(file)

    # Prepare the text file for saving results
    with open(config.RESULTS_TXT_PATH, "w") as txt_file:
        txt_file.write("\n======================================================== RESULTS ========================================================\n")
        txt_file.write(f"{'Learner ID':<10} {'Name':<15} {'Module 1':<15} {'Module 2':<15} {'Module 3':<15} {'Module 4':<15} {'Certification':<35}")
        txt_file.write("=" * 121 + "\n")

        for learner in learners:
            learner_id = learner["learnerID"]
            name = f"{learner['firstName']} {learner['lastName']}"

            # Gathering the results for the modules directly from JSON
            results = {
                "resultsModule1": learner["results"].get("resultsModule1", "0"),
                "resultsModule2": learner["results"].get("resultsModule2", "0"),
                "resultsModule3": learner["results"].get("resultsModule3", "0"),
                "resultsModule4": learner["results"].get("resultsModule4", "0"),
            }

            # Simply using the results data as is (no grade check here)
            certification = learner.get("certification", "Unknown Certification")

            # Write learner data to the file
            txt_file.write(f"{learner_id:<10} {name:<15} {results['resultsModule1']:<15} {results['resultsModule2']:<15} {results['resultsModule3']:<15} {results['resultsModule4']:<15} {certification:<35}\n")

    os.system('clear')
    print("\n==================== STATUS ====================\n")
    print(f"  >> Results list successfully saved to {config.RESULTS_TXT_PATH}")
    print("\n  Press [R] to return to Results Menu.")

    while True:
        key_press = keyboard.read_event(suppress=True)
        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "r":
                results_menu()  # Assuming you have this function to return to the menu
                break
            else:
                print("Invalid key! Press [R] to return to Results Menu.")


def results_script():
    results_menu()
    results_list()
    save_txt()