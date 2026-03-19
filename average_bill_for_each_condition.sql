SELECT Medical_Condition,
      round(AVG(Billing_Amount)::numeric,0) AS avg_billing
FROM hospitaldata
GROUP BY Medical_Condition
ORDER BY avg_billing DESC;