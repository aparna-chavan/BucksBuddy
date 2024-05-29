{{
  config(
    materialized = 'table',
    )
}}

WITH src_TSLA AS (
    SELECT * FROM {{ ref("src_TSLA") }}
)

SELECT 
    *, 'TSLA' AS ticker
FROM 
    src_TSLA
WHERE 
    (POST_TITLE ILIKE '%TSLA%'
    OR POST_TITLE ILIKE '%TESLA%'
    OR COMMENT ILIKE '%TSLA%'
    OR COMMENT ILIKE '%TESLA%')