import datetime
import math
import uuid
from models.bank_model import Loan




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