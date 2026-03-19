select medical_condition,sum(billing_amount) as total_bill_per_condition
from hospitaldata
group by medical_condition
order by total_bill_per_condition desc
limit 6;

