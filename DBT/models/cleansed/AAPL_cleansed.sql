{{
  config(
    materialized = 'table',
    )
}}

WITH src_AAPL AS (
    SELECT * FROM {{ ref("src_AAPL") }}
)

SELECT 
    *, 'AAPL' AS ticker
FROM 
    src_AAPL
WHERE 
    (POST_TITLE ILIKE '%AAPL%'
    OR POST_TITLE ILIKE '%APPLE%'
    OR COMMENT ILIKE '%AAPL%'
    OR COMMENT ILIKE '%APPLE%')
