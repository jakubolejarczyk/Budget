-- Migration 7
-- Create expenses table

USE budget;
GO

CREATE TABLE expenses (
	expense_id INT IDENTITY(1,1),
	budget_id INT NOT NULL,
	category_id INT NOT NULL,
	expense_amount INT NOT NULL,
	CONSTRAINT pk_expense_id PRIMARY KEY (expense_id),
	CONSTRAINT fk_expenses_budgets FOREIGN KEY (budget_id) REFERENCES budgets(budget_id),
	CONSTRAINT fk_expenses_categories FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
