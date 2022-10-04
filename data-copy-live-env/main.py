# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from config import DB_DETAILS
from util import get_tables
def systemm():
    env=sys.argv[1]
    dbdetails=DB_DETAILS[env]
    tables=get_tables('table_list.txt')
    for table in tables["table_name"]:
        print(table)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    systemm()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
