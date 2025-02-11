import module_script
import learner_script
import results_script

import os
import keyboard


def main_menu():
    os.system('clear')
    print("\n============ MAIN MENU ============")
    print("\n  >> Press [1] to Modules Menu")
    print("  >> Press [2] to Learners Menu")
    print("  >> Press [3] to Results")
    print("\n  Press [X] to close app.")


    while True:
        key_press = keyboard.read_event(suppress=True) 
    

        if key_press.event_type == "down":
            key = key_press.name.lower()
            if key == "1":
                module_script.module_script()
                break
            elif key == "2":
                learner_script.learner_script()
                break
            elif key == "3":
                results_script.results_menu()
                break
            elif key == "x":
                close_app()
            else:
                print("Invalid key! Choose a number/letter from the Menu.")


def close_app():
    os.system('clear')
    exit()

def main():
    main_menu()


if __name__ == "__main__":
    main()