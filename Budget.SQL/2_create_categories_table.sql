-- Migration 2
-- Create categories table

USE budget;
GO

CREATE TABLE categories (
	category_id INT IDENTITY(1,1),
	category_name VARCHAR(255) NOT NULL,
	category_created_at DATETIME2 NOT NULL CONSTRAINT df_category_created_at DEFAULT SYSDATETIME(),
	category_updated_at DATETIME2 NOT NULL,
	CONSTRAINT pk_category_id PRIMARY KEY (category_id),
);
