# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import sys
from config import DB_DETAILS
def system():
    env=sys.argv[1]
    dbdetails=DB_DETAILS[env]
    print(dbdetails)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    system()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
