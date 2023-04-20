from menu import MenuItem, Connector


class MenuEditor:
    def __init__(self):
        self.menu = MenuItem()
        self.show_user_menu()

    def print_menu(self):
        print("—" * 21)
        print("  -> MENU")
        print("—" * 21)
        print(" (a) Add an item")
        print(" (d) Delete an item")
        print(" (v) View the menu")
        print(" (x) Exit")
        print("—" * 21)

    def show_user_menu(self):
        while True:
            self.print_menu()
            choice = input("Enter your choice: ")
            if choice.lower() == 'x':
                print("Bye-bye!")
                self.show_restaurant_menu()
                break
            elif choice.lower() == 'a':
                self.add_item_to_menu()
            elif choice.lower() == 'd':
                self.remove_item_from_menu()
            elif choice.lower() == 'v':
                self.show_restaurant_menu()

    def add_item_to_menu(self):
        tmp_name = input("Enter the name: ")
        tmp_price = input("Enter the price: ")
        if tmp_price.isnumeric() and tmp_name != 0:
            if self.menu.save_item(tmp_name, tmp_price):
                print("The item is added: ")
                print(self.menu.get_item_by_name(tmp_name))
            else:
                print("Your item is not added. Please, try again later")
        else:
            print("Your input data is incorrect")

    def remove_item_from_menu(self):
        self.menu.delete_item(input("Enter the name: "))

    def show_restaurant_menu(self):
        for item in self.menu.all_items():
            print("=" * 30)
            for i, j in enumerate(item):
                print(self.menu.constants['columns'][i] + ': ' + str(j))
            print("=" * 30)


test_menu = MenuEditor()
