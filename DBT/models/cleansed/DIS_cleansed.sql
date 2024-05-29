{{
  config(
    materialized = 'table',
    )
}}

WITH src_DIS AS (
    SELECT * FROM {{ ref("src_DIS") }}
)

SELECT 
    *, 'DIS' AS ticker
FROM 
    src_DIS
WHERE 
    (POST_TITLE ILIKE '%DIS%'
    OR POST_TITLE ILIKE '%DISNEY%'
    OR COMMENT ILIKE '%DIS%'
    OR COMMENT ILIKE '%DISNEY%')
