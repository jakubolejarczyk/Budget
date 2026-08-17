USE budget;
GO

SELECT
	b.budget_month,
	b.budget_year,
	cb.category_budget_amount,
	e.expense_amount,
	SUM(e.expense_amount) AS expense_amount_sum,
	cb.category_budget_amount - SUM(e.expense_amount) AS expense_amount_remains
FROM category_budgets AS cb
INNER JOIN budgets AS b
ON cb.budget_id = b.budget_id
LEFT JOIN expenses AS e
ON cb.category_id = e.category_id
WHERE b.budget_month = 8 AND b.budget_year = 2026
GROUP BY b.budget_month, b.budget_year, cb.category_budget_amount, e.expense_amount;
