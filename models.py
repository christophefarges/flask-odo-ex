from app import db


class Test(db.Model):
    __tablename__ = 'tests'

    id = db.Column(db.Integer, primary_key=True)
    mydata = db.Column(db.String())

    def __init__(self, mydata):
        self.mydata = mydata

    def __repr__(self):
        return '<id:{} mydata:{}>'.format(self.id, self.mydata)