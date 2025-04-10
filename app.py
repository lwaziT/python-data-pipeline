import sys

from config import DB_DETAILS
from util import get_tables, load_db_details
from read import read_table

def main():
    env = sys.argv[1]
    db_details = DB_DETAILS[env]

    tables = get_tables('C:/Users/tobos/Desktop/PythonProject/table_list')
    table_name = 'departments'
    data, column_name = read_table(db_details,table_name)
    for record in data:
        print(record)


if __name__ == '__main__':
    main()