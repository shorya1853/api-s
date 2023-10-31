from flask import jsonify, request
from flask_smorest import Blueprint
from flask.views import MethodView
from models.bank_model import Loan
from methods import save_loan_to_database
from sqlalchemy import and_
import datetime
import math
import uuid
from db import db


blp = Blueprint("user_loan", __name__, description='user requesting api')

def save_loan_to_database(loan_request, partner_secret):
    parsed_birth_date = datetime.datetime.strptime(loan_request['customer']['birth_date'], '%Y-%m-%d')
    parsed_principal_amount = loan_request['principal_amount']
    parsed_term_months = loan_request['term_months']

    loan_interest = math.ceil( parsed_principal_amount * parsed_term_months * 0.01 )
    monthly_installment = math.ceil( (parsed_principal_amount + loan_interest) / parsed_term_months )
    
    loan = Loan(
            loan_id = str(uuid.uuid4()),
            principal_amount = parsed_principal_amount,
            term_months = parsed_term_months,
            collateral_brand = loan_request['collateral']['brand'],
            collateral_model = loan_request['collateral']['model'],
            collateral_manufacturing_year = loan_request['collateral']['manufacturing_year'],
            customer_id_number = loan_request['customer']['id_number'],
            customer_name = loan_request['customer']['name'],
            customer_monthly_income = loan_request['customer']['monthly_income'],
            customer_birth_date = parsed_birth_date,
            created_by = partner_secret,
            status = 'PENDING',
            loan_interest = loan_interest,
            monthly_installment = monthly_installment
        )
    return loan

@blp.route("/api/loan")
class LoanApis(MethodView):
    def post(self):
        saved_loan = save_loan_to_database(
            request.json, request.headers['partner_secret']
        )
        db.session.add()
        db.session.commit()
    
        return jsonify(
                customer_name = saved_loan.customer_name,
                loan_id = saved_loan.loan_id,
                status = saved_loan.status
            ), 201
        

    
    def get(self):
        filter_loan = Loan.query.filter( \
            and_( \
                Loan.loan_id == request.args['loan_id'], \
                Loan.created_by == request.headers['partner_secret']
            )
        )
    
        existing_loan = filter_loan.first()
    
        return jsonify(
            existing_loan.to_dict()
        ), 200

