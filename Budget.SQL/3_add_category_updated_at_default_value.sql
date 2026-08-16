-- Migration 3
-- Add category updated at default value

USE budget;
GO

ALTER TABLE categories
ADD CONSTRAINT df_category_updated_at
DEFAULT SYSDATETIME() FOR category_updated_at;
