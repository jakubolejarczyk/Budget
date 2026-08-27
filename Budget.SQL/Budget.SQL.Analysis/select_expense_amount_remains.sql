USE budget;
GO

SELECT
	c.category_id,
	c.category_name,
	b.budget_month,
	b.budget_year,
	cb.category_budget_amount,
	SUM(e.expense_amount) AS expense_amount_sum,
	cb.category_budget_amount - SUM(e.expense_amount) AS expense_amount_remains
FROM category_budgets AS cb
LEFT JOIN budgets AS b
ON cb.budget_id = b.budget_id
LEFT JOIN expenses AS e
ON cb.category_id = e.category_id
LEFT JOIN categories AS c
ON c.category_id = cb.category_id
WHERE b.budget_month = 8 AND b.budget_year = 2026
GROUP BY c.category_id, c.category_name, b.budget_month, b.budget_year, cb.category_budget_amount
ORDER BY c.category_id ASC;

--SELECT * FROM expenses;

--INSERT INTO expenses (budget_id, category_id, expense_amount)
--VALUES (1, 1, 10);