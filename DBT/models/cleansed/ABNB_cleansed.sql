{{
  config(
    materialized = 'table',
    )
}}

WITH src_ABNB AS (
    SELECT * FROM {{ ref("src_ABNB") }}
)

SELECT 
    *, 'ABNB' AS ticker
FROM 
    src_ABNB
WHERE 
    (POST_TITLE ILIKE '%ABNB%'
    OR POST_TITLE ILIKE '%AIRBNB%'
    OR COMMENT ILIKE '%ABNB%'
    OR COMMENT ILIKE '%AIRBNB%')