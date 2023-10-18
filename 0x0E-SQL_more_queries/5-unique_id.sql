-- Check if the table 'unique_id' already exists in the specified database
-- If the table doesn't exist, create it
CREATE TABLE IF NOT EXISTS unique_id (
    id INT NOT NULL UNIQUE DEFAULT 1,
    name VARCHAR(256)
);