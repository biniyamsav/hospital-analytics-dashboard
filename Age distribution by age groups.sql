SELECT 
       SUM(CASE WHEN age BETWEEN 0 AND 17 THEN 1 ELSE 0 END) AS "Adolescents(0-17)",
       SUM(CASE WHEN age BETWEEN 18 AND 39 THEN 1 ELSE 0 END) AS "Young_Adults(18-39)",
       SUM(CASE WHEN age BETWEEN 40 AND 64 THEN 1 ELSE 0 END) AS "Middle_aged_Adults(40-64)",
       SUM(CASE WHEN age >= 65 THEN 1 ELSE 0 END) AS "Older_Adults(65+)"
FROM hospitaldata;