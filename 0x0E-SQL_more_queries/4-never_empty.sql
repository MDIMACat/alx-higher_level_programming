-- Check if the table 'id_not_null' already exists in the specified database
-- If the table doesn't exist, create it
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
