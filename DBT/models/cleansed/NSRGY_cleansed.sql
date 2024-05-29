{{
  config(
    materialized = 'table',
    )
}}

WITH src_NSRGY AS (
    SELECT * FROM {{ ref("src_NSRGY") }}
)

SELECT 
    *, 'NSRGY' AS ticker
FROM 
    src_NSRGY
WHERE 
    (POST_TITLE ILIKE '%NSRGY%'
    OR POST_TITLE ILIKE '%NESTLE%'
    OR COMMENT ILIKE '%NSRGY%'
    OR COMMENT ILIKE '%NESTLE%')
