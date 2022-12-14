import os

DB_DETAILS = {
    'dev':{
        'SOURCE_DB':{
            'DB_TYPE':'mysql',
            'DB_HOST':'localhost',
            'DB_NAME':'retail',
            'DB_USER':os.environ.get('SOURCE_DB_USER'),
            'DB_PASS':os.environ.get('SOURCE_DB_PASS')
        },
        'TRAGET_DB':{
            'DB_TYPE':'postgres',
            'DB_HOST':'localhost',
            'DB_NAME':'retail',
            'DB_USER':os.environ.get('TARGET_DB_USER'),
            'DB_PASS':os.environ.get('TARGET_DB_PASS')
        }
    }

}