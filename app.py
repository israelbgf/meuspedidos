import os

if os.environ.get('DELIVERY_MECHANISM', 'FLASK'):
    from webflask.entrypoint import app
else:
    from webdjango.wsgi import app

if __name__ == "__main__":
    app.run()
