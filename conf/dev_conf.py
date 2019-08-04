# DB
DATABASE_URI = ""

# Log
LOGGER_DICT = {
    'version': 1,
    'formatters': {
        'default': {'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',}
    },
    'handlers': {
        'wsgi': {
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout',
            'formatter': 'default',
            'level': 'DEBUG'
                }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    },
    'loggers': {
        'test':
            {'level': 'DEBUG',
             'handlers':['wsgi'],
             'propagate':0}
    }
}