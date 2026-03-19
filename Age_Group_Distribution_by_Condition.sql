select medical_condition,
sum(case when age between 0 and 17 then 1 else 0 end) as "Adolescents(0-17)",
sum(case when age between 18 and 39 then 1 else 0 end) as "Young_Adults(18-39)",
sum(case when age between 40 and 64 then 1 else 0 end) as "Middle_aged_Adults(40-64)",
sum(case when age >=65 then 1 else 0 end) as "older_adults(65+)"
from hospitaldata
group by medical_condition 