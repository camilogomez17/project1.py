def show_menu():
    is_running = True
    while is_running:
        print("\nMenu: ")
        print("1. Play rock, paper, scissors!")
        print("2. View Statistics")
        print("3. Exit")
        
        choice = input("Please choose an option!")
        
        print(f"You chose: {choice}")
        
        if choice == "1":
            print("You chose option 1")
        elif choice == "2":
            print("You chose option 2")
        elif choice == "3":
            is_running = False
            break
        else:
            print("Invalid choice. Please try again.")
            continue