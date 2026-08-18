USE budget;
GO

SELECT
	b.budget_id,
	b.budget_month,
	b.budget_year,
	c.category_id,
	c.category_name,
	cb.category_budget_id,
	cb.category_budget_amount
FROM budgets AS b
LEFT JOIN category_budgets AS cb
ON b.budget_id = cb.budget_id
LEFT JOIN categories AS c
ON c.category_id = cb.category_id
WHERE b.budget_month = 8 AND b.budget_year = 2026;
