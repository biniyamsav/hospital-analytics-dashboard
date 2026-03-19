SELECT doctor,
       ROUND(SUM(billing_amount)::numeric, 0) AS total_revenue_per_doctor
FROM hospitaldata
GROUP BY doctor
ORDER BY total_revenue_per_doctor DESC
LIMIT 10;