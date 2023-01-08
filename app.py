from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.ext.declarative import declarative_base

rest_api_app = Flask(__name__)
rest_api_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost:5432/banks_dump"
db_handler = SQLAlchemy(rest_api_app)
migrate = Migrate(rest_api_app, db_handler)
Base = declarative_base()
Column = db_handler.Column


class Bank(db_handler.Model):
    __tablename__ = 'banks'

    id = db_handler.Column(db_handler.Integer, primary_key=True)
    name = db_handler.Column(db_handler.String())


class BankBranches(db_handler.Model):
    __tablename__ = 'bank_branches'

    ifsc = Column(db_handler.Integer, primary_key=True)
    bank_id = Column(db_handler.Integer)
    branch = Column(db_handler.String(300))
    address = Column(db_handler.String(300))
    city = Column(db_handler.String(300))
    district = Column(db_handler.String(300))
    state = Column(db_handler.String(300))
    bank_name = Column(db_handler.String(300))


@rest_api_app.route("/banks", methods=["GET"])
def banks_list():
    banks = Bank.query.all()
    response = [{
        "name": bank.name,
        "id": bank.id
    } for bank in banks]

    return response


@rest_api_app.route("/banks/<bank_id>", methods=["GET"])
def bank_details(bank_id):
    bank = Bank.query.get_or_404(bank_id)

    return {
        "name": bank.name,
        "id": bank.id
    }


@rest_api_app.route("/banks/<bank_id>/branches", methods=["GET"])
def bank_branches(bank_id):
    branches = BankBranches.query.filter_by(bank_id=bank_id).all()

    return [{
        "ifsc": branch.ifsc,
        "bank_id": branch.bank_id,
        "branch": branch.branch,
        "address": branch.address,
        "city": branch.city,
        "district": branch.district,
        "state": branch.state,
        "bank_name": branch.bank_name
    }for branch in branches

    ]


@rest_api_app.route("/banks/<bank_id>/branches/<branch_id>", methods=["GET"])
def bank_branch(bank_id, branch_id):
    branch = BankBranches.query.filter_by(
        bank_id=bank_id, ifsc=branch_id).first_or_404()

    return {
        "ifsc": branch.ifsc,
        "bank_id": branch.bank_id,
        "branch": branch.branch,
        "address": branch.address,
        "city": branch.city,
        "district": branch.district,
        "state": branch.state,
        "bank_name": branch.bank_name
    }


if __name__ == "__main__":
    rest_api_app.run(debug=True)
