import functools


class MenuManager:
    def __init__(self):
        self.menu = []

    def add_item(self, name, price, spice, gluten):
        self.menu.append({
            'Name': name,
            'Price': price,
            'Spice': spice,
            'Gluten': gluten
        })

    def is_name(self, name):
        return functools.reduce(lambda a, e: e if e is True else a, list(name in e.values() for e in self.menu), False)

    def update_item(self, name, price, spice, gluten):
        if self.is_name(name):
            self.menu[self.menu.index(*(filter(lambda e: e['Name'] == name, self.menu)))] = {
                'Name': name,
                'Price': price,
                'Spice': spice,
                'Gluten': gluten
            }

    def remove_item(self, name):
        if self.is_name(name):
            self.menu.remove(*(filter(lambda e: e['Name'] == name, self.menu)))

    def print_menu(self):
        print('*'*75)
        for e in self.menu:
            print(e)
        print('*' * 75)


menu = MenuManager()
result = [menu.add_item(*i) for i in [
    ['Soup', 10, 'B', True],
    ['Hamburger', 15, 'A', True],
    ['Salad', 18, 'A', False],
    ['French Fries', 18, 'A', False],
    ['Beef bourguignon', 25, 'B', True]
]]
menu.print_menu()
menu.remove_item('Toast')
menu.remove_item('Soup')
menu.print_menu()
menu.update_item('Soup', 10, 'B', True)
menu.update_item('French Fries', 25, 'B', False)
menu.print_menu()
