import os

FLASK_CONFIGURATION = {
    'DEBUG': True,
    'MAIL_PORT': 1025
}

if os.environ.get('PRODUCTION') in ('true', 'TRUE'):
    FLASK_CONFIGURATION = {
        'MAIL_SERVER': os.environ['MAIL_SERVER'],
        'MAIL_PORT': int(os.environ.get('MAIL_PORT', 25)),
        'MAIL_USERNAME': os.environ['MAIL_USERNAME'],
        'MAIL_PASSWORD': os.environ['MAIL_PASSWORD'],
        'DEBUG': os.environ.get('DEBUG', 'true') in ('true', 'TRUE')
    }