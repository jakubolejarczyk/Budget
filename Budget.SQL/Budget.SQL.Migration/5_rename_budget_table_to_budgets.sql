-- Migration 5
-- Rename budget table to budgets

USE budget;
GO

EXEC sp_rename 'budget', 'budgets';
