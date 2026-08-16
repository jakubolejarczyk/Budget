-- Migration 6
-- Create badtegory budget table

CREATE TABLE category_budgets (
	category_budget_id INT IDENTITY(1, 1),
	budget_id INT NOT NULL,
	category_id INT NOT NULL,
	category_budget_amount DECIMAL(18, 2) NOT NULL,
	category_budget_created_at DATETIME2 NOT NULL CONSTRAINT df_category_budget_created_at DEFAULT SYSDATETIME(),
	category_budget_updated_at DATETIME2 NOT NULL CONSTRAINT df_category_budget_updated_at DEFAULT SYSDATETIME(),
	CONSTRAINT pk_category_budget_id PRIMARY KEY (category_budget_id),
	CONSTRAINT fk_category_budgets_budgets FOREIGN KEY (budget_id) REFERENCES budgets(budget_id),
	CONSTRAINT fk_category_budgets_categories FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
