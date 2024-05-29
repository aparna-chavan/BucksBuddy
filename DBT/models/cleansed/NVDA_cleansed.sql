{{
  config(
    materialized = 'table',
    )
}}

WITH src_NVDA AS (
    SELECT * FROM {{ ref("src_NVDA") }}
)

SELECT 
    *, 'NVDA' AS ticker
FROM 
    src_NVDA
WHERE 
    (POST_TITLE ILIKE '%NVDA%'
    OR POST_TITLE ILIKE '%NVIDIA%'
    OR COMMENT ILIKE '%NVDA%'
    OR COMMENT ILIKE '%NVIDIA%')