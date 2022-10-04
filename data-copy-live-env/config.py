import os

DB_DETAILS = {
    'dev':{
        'SOURCE_DB':{
            'DB_TYPE':'mysql',
            'DB_HOST':'192.168.1.119',
            'DB_NAME':'retail_db',
            'DB_USER':os.environ.get('SOURCE_DB_USER'),
            'DB_PASS':os.environ.get('SOURCE_sourceDB_PASS')
        },
        'TRAGET_DB':{
            'DB_TYPE':'postgres',
            'DB_HOST':'192.168.1.119',
            'DB_NAME':'retail_db',
            'DB_USER':os.environ.get('TARGET_DB_USER'),
            'DB_PASS':os.environ.get('TARGET_DB_PASS')
        }
    }

}