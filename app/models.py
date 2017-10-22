class Dev():

    positions = []

    def __init__(self, name, email):

        self.name = name
        self.email = email

    def __repr__(self):
        return '<Developer %r>' % self.name
