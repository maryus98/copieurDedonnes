from mysql import connector as mc

from config import DB_DETAILS
env='dev'
dbdetails=DB_DETAILS[env]
source_db=dbdetails['SOURCE_DB']
connection = mc.connect(user=source_db['DB_USER'],password=source_db['DB_PASS'],host=source_db['DB_HOST'],database=source_db['DB_NAME'])
