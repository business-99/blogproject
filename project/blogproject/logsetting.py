import os

def log_config(base_dir):
    lev = os.environ.get('LOG_LEVEL', None)
    if not lev:
        lev = 'INFO'
    log_path = os.path.join(os.path.dirname(base_dir), 'logfile')
    LOGGING = {
        'version': 1,
        'disable_existing_loggers': False,
        'handlers': {
            'file': {
                'level': lev,
                'class': 'logging.FileHandler',
                'filename': os.path.join(log_path, 'my.log'),
            },
        },
        'loggers': {
            'django.request': {
                'handlers': ['file'],
                'level': lev,
                'propagate': True,
            },
        },
    }
    return LOGGING