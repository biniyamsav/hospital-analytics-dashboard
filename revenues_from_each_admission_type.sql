SELECT 
    admission_type,
    SUM(billing_amount) AS total_revenue
FROM hospitaldata
GROUP BY admission_type
ORDER BY total_revenue DESC
LIMIT 3;