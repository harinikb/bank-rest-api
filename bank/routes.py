from bank import app
from bank.models import Bank, BankBranches
from bank import db_handler


@app.route("/banks", methods=["GET"])
def banks_list():
    banks = Bank.query.all()
    response = [{
        "name": bank.name,
        "id": bank.id
    } for bank in banks]

    return response


@app.route("/banks/<bank_id>", methods=["GET"])
def bank_details(bank_id):
    bank = Bank.query.get_or_404(bank_id)

    return {
        "name": bank.name,
        "id": bank.id
    }


@app.route("/banks/<bank_id>/branches", methods=["GET"])
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


@app.route("/banks/<bank_id>/branches/<branch_id>", methods=["GET"])
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
