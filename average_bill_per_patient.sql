select round(AVG(billing_amount ):: numeric,0)as average_bill_per_patient
from hospitaldata