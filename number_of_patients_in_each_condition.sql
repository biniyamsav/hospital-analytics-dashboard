SELECT Medical_Condition,
       COUNT(*) AS number_of_patients
FROM hospitaldata
GROUP BY Medical_Condition
ORDER BY number_of_patients DESC; 
