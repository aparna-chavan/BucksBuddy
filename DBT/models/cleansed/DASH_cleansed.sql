{{
  config(
    materialized = 'table',
    )
}}

WITH src_DASH AS (
    SELECT * FROM {{ ref("src_DASH") }}
)

SELECT 
    *, 'DASH' AS ticker
FROM 
    src_DASH
WHERE 
    (POST_TITLE ILIKE '%DASH%'
    OR POST_TITLE ILIKE '%DOORDASH%'
    OR COMMENT ILIKE '%DASH%'
    OR COMMENT ILIKE '%DOORDASH%')