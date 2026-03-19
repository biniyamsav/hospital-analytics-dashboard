select hospital,round(avg(discharge_date -date_of_admission ),2) as top_10_highst_stay_per_hospital
from hospitaldata
group by hospital 
order by top_10_highst_stay_per_hospital  desc 
limit 10;

