USE budget;
GO

SELECT
	b.budget_month,
	b.budget_year,
	b.budget_amount,
	SUM(cb.category_budget_amount) AS amount_of_all_categories,
	b.budget_amount - SUM(cb.category_budget_amount) AS amount_to_be_distributed
FROM budgets AS b
INNER JOIN category_budgets AS cb
ON b.budget_id = cb.budget_id
INNER JOIN categories AS c
ON c.category_id = cb.category_id
WHERE b.budget_month = 8 AND b.budget_year = 2026
GROUP BY b.budget_month, b.budget_year, b.budget_amount;
