select admission_type,round(avg(discharge_date - date_of_admission ),2) as "average_stay"
from hospitaldata
group by admission_type 