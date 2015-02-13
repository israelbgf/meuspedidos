import os

if os.environ.get('DELIVERY_MECHANISM', 'FLASK') == 'FLASK':
    print '****', 'Using FLASK', '*****'
    from webflask.entrypoint import app
else:
    print '****', 'Using DJANGO', '*****'
    from webdjango.wsgi import app

if __name__ == "__main__":
    app.run()
