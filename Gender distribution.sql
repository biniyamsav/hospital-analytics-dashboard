SELECT 
       SUM(CASE WHEN gender = 'Male' THEN 1 ELSE 0 END) AS Male_Patients,
       SUM(CASE WHEN gender = 'Female' THEN 1 ELSE 0 END) AS Female_Patients,
       SUM(CASE WHEN gender NOT IN ('Male','Female') THEN 1 ELSE 0 END) AS Other_Patients
FROM hospitaldata;