SELECT 
    insurance_provider,
    SUM(billing_amount) AS total_billing
FROM hospitaldata
GROUP BY insurance_provider
ORDER BY total_billing DESC
