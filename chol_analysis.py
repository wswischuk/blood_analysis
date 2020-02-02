def HDL_analysis(HDL_level):
    if HDL_level >= 60:
        return "Normal"
    elif 40 <= HDL_level < 60:
        return "Borderline low"
    else:
        return "Low"


def LDL_analysis(LDL_level):
    if LDL_level >= 190:
        return "Very High"
    elif 160 <= LDL_level < 190:
        return "High"
    elif 130 <= LDL_level < 160:
        return "Borderline"
    else:
        return "Normal"


def cholesterol_analysis():
    print("Cholesterol Analysis")
    typetest = input("Enter test result: ")
    test_info = typetest.split("=")
    if test_info[0] == "HDL":
        answer = HDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))
    if test_info[0] == "LDL":
        answer = LDL_analysis(int(test_info[1]))
        print("The level is {}".format(answer))


def new_feature():
    pass


def name_function():
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    full_name = [first_name, last_name]


def interface():
    while True:
        print("Cholesterol Calc")
        print("Options")
        print("  1 - Cholesterol Analysis")
        print("  9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return
        elif choice == "1":
            cholesterol_analysis()


def fever_check(test_list):
    fever = False
    for temperature in temp_list:
        if temperature > 98.6:
            fever = True
    return Fever


if __name__ == "__main__":
    interface()
