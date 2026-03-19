SELECT 
    medical_condition,
    round(AVG(discharge_date - date_of_admission),2) AS average_stay
FROM hospitaldata
GROUP BY medical_condition
ORDER BY average_stay DESC;