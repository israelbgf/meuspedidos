import os

FLASK_CONFIGURATION = {
    'MAIL_SERVER': os.environ.get('MAIL_SERVER', 'localhost'),
    'MAIL_PORT': int(os.environ.get('MAIL_PORT', 1025)),
    'MAIL_USERNAME': os.environ.get('MAIL_USERNAME'),
    'MAIL_PASSWORD': os.environ.get('MAIL_PASSWORD'),
    'DEBUG': os.environ.get('DEBUG', 'true') in ('true', 'TRUE')
}