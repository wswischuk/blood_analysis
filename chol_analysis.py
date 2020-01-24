def interface():
    choice = 0
    while true:
        print("Cholesterol Calc")
        print("options")
        print("  9 - Quit")
        choice = input("Enter your option: ")
        if choice == '9':
            return

if __name__ == "__main__":
    interface()