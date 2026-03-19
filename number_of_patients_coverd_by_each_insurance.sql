select insurance_provider,count(insurance_provider ) as number_of_patients_coverd
from hospitaldata
group by insurance_provider 
order by number_of_patients_coverd desc
