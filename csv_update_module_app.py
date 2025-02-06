modules_csv_path = r"C:\Users\TulioMinini(Tallaght\Desktop\procedural-programming\module_list\modules.csv"
read_csv = open(modules_csv_path, "r")
read_data_csv = read_csv.read()


def print_csv():
    print(f"All data from csv file: \n {read_data_csv}")
    print(f"All data from csv file: \n {read_data_csv[0]}")
    # print(f"All specific data from csv file: \n {read_data_csv["module"]}")

    # for i in read_data_csv:
    #     print(f"All specific data from csv file: \n {read_data_csv["module"]}")


def update_csv():
    pass


def main():
    print_csv()


main()