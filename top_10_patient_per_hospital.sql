select hospital,count(*) as patient_per_hospital
from hospitaldata
group by hospital 
order by patient_per_hospital desc 
limit 10