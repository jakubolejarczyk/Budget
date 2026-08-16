-- Migration 4
-- Create budget table

USE budget;
GO

CREATE TABLE budget (
	budget_id INT IDENTITY(1, 1),
	budget_month INT NOT NULL,
	budget_year INT NOT NULL,
	budget_amount DECIMAL(18, 2) NOT NULL,
	budget_created_at DATETIME2 NOT NULL CONSTRAINT df_budget_created_at DEFAULT SYSDATETIME(),
	budget_updated_at DATETIME2 NOT NULL CONSTRAINT df_budget_updated_at DEFAULT SYSDATETIME(),
	CONSTRAINT pk_budget_id PRIMARY KEY (budget_id)
);
