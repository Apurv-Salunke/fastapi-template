```sql
-- ===========================================
-- File: init.sql
-- Purpose: Initialize PostgreSQL Database with Schema, Seed Data, Query Monitoring, and Performance Insights
-- ===========================================

-- ===========================================
-- Step 1: Enable Extensions for Monitoring
-- ===========================================
-- pg_stat_statements extension allows tracking query statistics
-- Required for monitoring query performance and usage insights
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Example: To view query statistics after running queries
SELECT * FROM pg_stat_statements;

-- ===========================================
-- Step 2: Schema Definition
-- ===========================================
-- Creating the main schema for the database
CREATE SCHEMA IF NOT EXISTS app_schema;

-- Switch to the newly created schema
SET search_path TO app_schema;

-- Creating a sample table `users`
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Creating a sample table `products`
CREATE TABLE IF NOT EXISTS products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    price NUMERIC(10, 2) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ===========================================
-- Step 3: Seed Initial Data
-- ===========================================
-- Populate the `users` table with initial records
INSERT INTO users (name, email) VALUES
('Alice', 'alice@example.com'),
('Bob', 'bob@example.com');

-- Populate the `products` table with initial records
INSERT INTO products (name, price) VALUES
('Product A', 49.99),
('Product B', 99.99);

-- ===========================================
-- Step 4: Logging Configuration (Optional)
-- ===========================================
-- Enable detailed logging of SQL statements (requires PostgreSQL configuration updates)
-- These settings should be added in `postgresql.conf` if not already present:
--
-- shared_preload_libraries = 'pg_stat_statements'
-- pg_stat_statements.max = 5000
-- pg_stat_statements.track = 'all'
-- log_statement = 'all'
-- log_duration = on
--
-- After enabling, you can analyze query durations in the logs:
-- Example Log Entry:
-- LOG:  duration: 0.123 ms  statement: SELECT * FROM users;

-- ===========================================
-- Step 5: Query Monitoring Insights
-- ===========================================
-- Use pg_stat_statements to gain insights into query performance:
-- Find the top 5 slowest queries:
SELECT query, total_time, calls
FROM pg_stat_statements
ORDER BY total_time DESC
LIMIT 5;

-- Find the most frequently executed queries:
SELECT query, calls
FROM pg_stat_statements
ORDER BY calls DESC
LIMIT 5;

-- ===========================================
-- Notes:
-- 1. This script is executed only on the first initialization of the database.
-- 2. Modify the schema and seed data as per your application requirements.
-- 3. To make logging changes effective, restart the PostgreSQL server after updating `postgresql.conf`.
-- ===========================================

-- End of init.sql
```
