import psycopg2

HOSTNAME = 'localhost'
USERNAME = 'mvchalov'
PASSWORD = 'rukivnogi'
DATABASE = 'dvdrental'

connection = psycopg2.connect(host=HOSTNAME, user=USERNAME, password=PASSWORD, dbname=DATABASE )
cursor = connection.cursor()
query = "SELECT * FROM customer LIMIT 20;"
# cursor.execute(query)
cursor.execute("SELECT column_name FROM information_schema.columns WHERE table_name = 'customer'")

results = cursor.fetchall()
connection.close()
for item in results:
    print(item[0])