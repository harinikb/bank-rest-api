from bank import db_handler

Column, Model = db_handler.Column, db_handler.Model


class Bank(Model):
    __tablename__ = 'banks'

    id = Column(db_handler.Integer, primary_key=True)
    name = Column(db_handler.String())


class BankBranches(Model):
    __tablename__ = 'bank_branches'

    ifsc = Column(db_handler.Integer, primary_key=True)
    bank_id = Column(db_handler.Integer)
    branch = Column(db_handler.String(300))
    address = Column(db_handler.String(300))
    city = Column(db_handler.String(300))
    district = Column(db_handler.String(300))
    state = Column(db_handler.String(300))
    bank_name = Column(db_handler.String(300))
