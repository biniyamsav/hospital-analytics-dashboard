SELECT hospital,
       ROUND(AVG(EXTRACT(discharge_date - date_of_admission)), 2) AS top_10_lowest_stay_per_hospital
FROM hospitaldata
GROUP BY hospital
ORDER BY top_10_lowest_stay_per_hospital ASC
LIMIT 10;
