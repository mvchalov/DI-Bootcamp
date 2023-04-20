import requests
import json
import random
import psycopg2


class DataCollector:
    def __init__(self, url="https://restcountries.com/v3.1/all?fields=name,capital,flag,subregion,population"):
        self.in_data = self.get_data(url)
        self.choose_data()

    def get_data(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return json.loads(response.text)
        else:
            return False

    def choose_data(self, count=10):
        random_items = []
        for _ in range(count):
            while True:
                tmp_idx = random.randint(0, len(self.in_data) - 1)
                if self.in_data[tmp_idx] not in random_items:
                    random_items.append(self.in_data[tmp_idx])
                    break
        return random_items


class Connector:
    def __init__(self, host=None, user=None, password=None, database=None):
        self.host = host or 'localhost'
        self.user = user or 'mvchalov'
        self.password = password or 'rukivnogi'
        self.database = database or 'day4'
        self.table = ''

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

    def get_data(self):
        return self.run_queue("select * from " + self.table)

    def create_table(self, table="countries"):
        if self.table != table:
            self.table = table
        self.run_queue(
            "CREATE TABLE IF NOT EXISTS " + table + " (id SERIAL PRIMARY KEY, name VARCHAR(50), capital VARCHAR(30), flag VARCHAR(50), subregion VARCHAR(50), population int)")


class DBPopulate:
    def __init__(self):
        self.data = DataCollector()
        self.connector = Connector()
        self.connector.create_table()
        self.populate_table()
        print("The data has inserted to the database")
        self.show_result(self.connector.get_data())

    def populate_table(self):
        values = []
        for item in self.data.choose_data():
            values.append([])
            values[-1].append(item['name']['common'])
            if len(item['capital']) > 0:
                values[-1].append(item['capital'][0])
            else:
                values[-1].append('')
            values[-1].append(item['flag'])
            values[-1].append(item['subregion'])
            values[-1].append(item['population'])
        values = list(map(lambda e: list(map(lambda x: str(x).replace("'", "''"), e)), values))
        values_for_query = ''
        for i, item in enumerate(values):
            values_for_query += '('
            for k, j in enumerate(item):
                if str(j).isnumeric():
                    values_for_query += str(j)
                else:
                    values_for_query += "'" + j + "'"
                if k < len(item) - 1:
                    values_for_query += ', '
            values_for_query += ')'
            if i < len(values) - 1:
                values_for_query += ', '
        self.connector.run_queue(
            "insert into " + self.connector.table + " (name, capital, flag, subregion, population) values " + values_for_query)

    def show_result(self, fetched_data):
        for item in fetched_data:
            print("=" * 30)
            print("Country:", item[1])
            print("Capital:", item[2])
            print("Flag:", item[3])
            print("Subregion:", item[4])
            print("Population:", item[5])
            print("=" * 30)

a = DBPopulate()
