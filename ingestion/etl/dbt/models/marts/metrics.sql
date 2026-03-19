WITH base AS (
    SELECT *
    FROM staging_events
),

aggregated AS (
    SELECT
        DATE(timestamp) AS event_date,
        COUNT(DISTINCT user_id) AS dau,
        SUM(watch_time) AS total_watch_time,
        COUNT(*) AS total_events
    FROM base
    GROUP BY 1
)

SELECT * FROM aggregated
