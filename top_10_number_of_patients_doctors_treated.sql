select doctor,count(*) as number_of_patients_doctor_treated
from hospitaldata
group by doctor 
order by number_of_patients_doctor_treated desc 
limit 10
