class SafeForm(object):
    
    def __init__(self, form):
        self.form = form
        
    def int(self, field):
        try:
            return int(self.form.get(field))
        except:
            return None

    def str(self, field):
        return self.form.get(field)