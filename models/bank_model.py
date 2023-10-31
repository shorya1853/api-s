from db import db
from datetime import datetime





class Loan(db.Model):
    loan_id = db.Column(db.String(36), primary_key=True)
    principal_amount = db.Column(db.Integer)
    term_months = db.Column(db.Integer)
    collateral_brand = db.Column(db.String(50))
    collateral_model = db.Column(db.String(50))
    collateral_manufacturing_year = db.Column(db.Integer) 
    customer_name = db.Column(db.String(50))
    customer_birth_date = db.Column(db.DateTime)
    customer_monthly_income = db.Column(db.Integer)
    customer_id_number = db.Column(db.String(50))
    created_by = db.Column(db.String(50))
    status = db.Column(db.String(50))
    loan_interest = db.Column(db.Integer)
    monthly_installment = db.Column(db.Integer)


    def to_dict(self):
        collateral = {}
        collateral['brand'] = self.collateral_brand
        collateral['model'] = self.collateral_model
        collateral['manufacturing_year'] = self.collateral_manufacturing_year
        
        customer = {}
        customer['id_number'] = self.customer_id_number
        customer['birth_date'] = datetime.datetime.strftime(self.customer_birth_date, '%Y-%m-%d')
        customer['monthly_income'] = self.customer_monthly_income
        customer['name'] = self.customer_name
        
        return {
            'loan_id': self.loan_id,
            'principal_amount': self.principal_amount, 
            'term_months': self.term_months,
            'collateral': collateral,
            'customer': customer,
            'status': self.status,
            'interest': self.loan_interest,
            'monthly_installment': self.monthly_installment
        }