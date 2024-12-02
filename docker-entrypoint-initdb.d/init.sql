-- =============================================
-- File: docker-entrypoint-initdb.d/init.sql
-- Purpose: Initialize PostgreSQL for Percona PMM
-- =============================================

-- Enable the pg_stat_statements extension
CREATE EXTENSION IF NOT EXISTS pg_stat_statements;

-- Create a dedicated monitoring user
CREATE USER pmm_monitor WITH PASSWORD 'G#4JrLpM8B$eJ#N';

-- Grant necessary permissions to the monitoring user
GRANT pg_monitor TO pmm_monitor;
GRANT SELECT ON pg_stat_statements TO pmm_monitor;

-- Optional: Grant access to additional system views for deeper monitoring
GRANT SELECT ON pg_stat_activity TO pmm_monitor;
GRANT SELECT ON pg_stat_database TO pmm_monitor;

-- Query examples for performance monitoring (pg_stat_statements)
-- View the top 5 most time-consuming queries
-- SELECT query, total_time, calls
-- FROM pg_stat_statements
-- ORDER BY total_time DESC
-- LIMIT 5;

-- =============================================
-- Additional Notes
-- =============================================
-- To complete the configuration, ensure the following lines are added to
-- your PostgreSQL configuration file (postgresql.conf):
--
-- shared_preload_libraries = 'pg_stat_statements'
-- track_io_timing = on
-- log_statement = 'all'
-- log_duration = on
--
-- After editing postgresql.conf, restart the PostgreSQL server for changes
-- to take effect.
