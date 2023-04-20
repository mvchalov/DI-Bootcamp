import psycopg2


class Connector:
    def __init__(self, host=None, user=None, password=None, database=None):
        self.host = host or 'localhost'
        self.user = user or 'mvchalov'
        self.password = password or 'rukivnogi'
        self.database = database or 'day4'

    def run_queue(self, queue=''):
        if queue != '':
            try:
                connection = psycopg2.connect(
                    host=self.host,
                    user=self.user,
                    password=self.password,
                    dbname=self.database
                )
                if connection is not None:
                    curr = connection.cursor()
                    curr.execute(queue)
                    if 'select' in queue:
                        fetched_data = curr.fetchall()
                    else:
                        connection.commit()
                        fetched_data = True
                    connection.close()
                    return fetched_data
            except psycopg2.OperationalError as e:
                print("We experience connection issues. Try again later", e)
        return False


class MenuItem:
    def __init__(self, item_name=None, item_price=None):
        self.constants = {
            'table': 'menu_items',
            'columns': (),
        }
        self.connector = Connector()
        self.constants['columns'] = tuple(map(lambda e: e[0], self.connector.run_queue("select column_name from information_schema.columns where table_name = '"+self.constants['table']+"' order by column_name asc")))
        self.item_name = item_name
        self.item_price = item_price
        if self.item_name is not None:
            self.save_item(item_name, item_price)

    def save_item(self, curr_name='', curr_price=0):
        if curr_name != '':
            try:
                self.connector.run_queue("insert into " + self.constants['table'] + " (" + ", ".join(self.constants['columns'][1:]) + ") values ('" + curr_name + "', " + str(curr_price) + ");")
                return True
            except psycopg2.OperationalError:
                return False

    def delete_item(self, curr_name=""):
        if curr_name != "":
            try:
                self.connector.run_queue("delete from " + self.constants['table'] + " where " + self.constants['columns'][1] + "='" + curr_name + "';")
                return True
            except psycopg2.OperationalError:
                return False

    def update_item(self, curr_name="", curr_price=0):
        if curr_name != "":
            try:
                self.connector.run_queue(
                    "update " + self.constants['table'] + " set " + self.constants['columns'][1] + "=" + str(curr_price) + ", " + self.constants['columns'][2] + "='" + curr_name + "' where " + self.constants['columns'][1] + "=" + str(curr_price) + " or " + self.constants['columns'][2] + "='" + curr_name + "';")
            except psycopg2.OperationalError:
                return False

    def all_items(self):
        try:
            return self.connector.run_queue("select * from " + self.constants['table'])
        except psycopg2.OperationalError:
            return False

    def get_item_by_name(self, curr_name=""):
        if curr_name != "":
            try:
                return self.connector.run_queue("select * from " + self.constants['table'] + " where " + self.constants['columns'][1] + "='" + curr_name + "' limit 1;")
            except psycopg2.OperationalError:
                return False
        return False

