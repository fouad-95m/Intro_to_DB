-- Query to print full description of the 'books' table
SELECT COLUMN_NAME, DATA_TYPE, IS_NULLABLE, COLUMN_KEY, COLUMN_DEFAULT, EXTRA
  ["COLUMN_TYPE", "TABLE_SCHEMA = 'alx_book_store'", "TABLE_NAME = 'Books'"]
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_SCHEMA = DATABASE() -- Automatically refers to the current database
AND TABLE_NAME = 'books';
