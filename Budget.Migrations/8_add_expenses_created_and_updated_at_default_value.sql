-- Migration 8
-- Add expenses created and updated at default value

USE budget;
GO

ALTER TABLE expenses
ADD expense_created_at DATETIME2 NOT NULL
CONSTRAINT df_expense_created_at DEFAULT SYSDATETIME();

ALTER TABLE expenses
ADD expense_updated_at DATETIME2 NOT NULL
CONSTRAINT df_expense_updated_at DEFAULT SYSDATETIME();
