{{
  config(
    materialized = 'table',
    )
}}

WITH src_DHLGY AS (
    SELECT * FROM {{ ref("src_DHLGY") }}
)

SELECT 
    *, 'DHLGY' AS ticker
FROM 
    src_DHLGY
WHERE 
    (POST_TITLE ILIKE '%DHLGY%'
    OR POST_TITLE ILIKE '%DHL%'
    OR COMMENT ILIKE '%DHLGY%'
    OR COMMENT ILIKE '%DHL%')
