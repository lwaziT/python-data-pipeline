import os

DB_DETAILS = {
    'dev': {
        'SOURCE_DB': {
            'DB_TYPE': 'mysql',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail_db',
            'DB_USER': 'root',
            'DB_PASS': 'root',
        },
        'TARGET_DB': {
            'DB_TYPE': 'postgres',
            'DB_HOST': 'localhost',
            'DB_NAME': 'retail_db',
            'DB_USER': 'root',
            'DB_PASS': 'root',
        }
    }
}