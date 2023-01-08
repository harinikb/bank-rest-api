from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

rest_api_app = Flask(__name__)
rest_api_app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:admin@localhost:5432/banks_dump"
db_handler = SQLAlchemy(rest_api_app)
migrate = Migrate(rest_api_app, db_handler)


class Bank(db_handler.Model):
    __tablename__ = 'banks'

    id = db_handler.Column(db_handler.Integer, primary_key=True)
    name = db_handler.Column(db_handler.String())


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
    session = db_handler.session()
    cursor = session.execute(
        f"SELECT * FROM bank_branches WHERE bank_id = {bank_id};", ).cursor
    branches = cursor.fetchall()
    print(branches)

    return [{
        "ifsc": branch[0],
        "bank_id": branch[1],
        "branch": branch[2],
        "address": branch[3],
        "city": branch[4],
        "district": branch[5],
        "state": branch[6],
        "bank_name": branch[7]
    } for branch in branches]


@rest_api_app.route("/banks/<bank_id>/branches/<branch_id>", methods=["GET"])
def bank_branch(bank_id, branch_id):
    session = db_handler.session()
    cursor = session.execute(
        f"SELECT * FROM bank_branches WHERE bank_id = {bank_id} AND ifsc = '{branch_id}';", ).cursor
    b = cursor.fetchall()

    return [{
        "ifsc": row[0],
        "bank_id": row[1],
        "branch": row[2],
        "address": row[3],
        "city": row[4],
        "district": row[5],
        "state": row[6],
        "bank_name": row[7]
    } for row in b]


if __name__ == "__main__":
    rest_api_app.run(debug=True)
