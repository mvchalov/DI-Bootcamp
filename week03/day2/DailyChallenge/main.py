import string


class Pagination:
    def __init__(self, items="", pagesize=10.0):
        self.pagesize = round(pagesize)
        self.items = []
        for i in range(len(items)):
            if i % self.pagesize == 0:
                self.items.append([])
            self.items[-1].append(items[i])
        self.curr_page = 0

    def get_visible_items(self):
        return self.items[self.curr_page]

    def prev_page(self):
        if self.curr_page - 1 >= 0:
            self.curr_page -= 1

    def next_page(self):
        if self.curr_page + 1 < len(self.items):
            self.curr_page += 1

    def first_page(self):
        self.curr_page = 0

    def last_page(self):
        self.curr_page = len(self.items) - 1

    def go_to_page(self, number):
        if number - 1 > -1:
            if number - 1 < len(self.items):
                self.curr_page = number - 1
            else:
                self.curr_page = len(self.items) - 1
        else:
            self.curr_page = 0


p = Pagination(string.ascii_lowercase, 4.1)
print("Start:", p.get_visible_items())
p.next_page()
print("-> next page:", p.get_visible_items())
p.prev_page()
print("<- prev page:", p.get_visible_items())
p.last_page()
print("jump to the last page:", p.get_visible_items())
p.go_to_page(3)
print("jump to page 3:", p.get_visible_items())
p.first_page()
print("jump to the first page:", p.get_visible_items())
