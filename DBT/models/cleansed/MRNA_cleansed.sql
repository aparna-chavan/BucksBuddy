{{
  config(
    materialized = 'table',
    )
}}

WITH src_MRNA AS (
    SELECT * FROM {{ ref("src_MRNA") }}
)

SELECT 
    *, 'MRNA' AS ticker
FROM 
    src_MRNA
WHERE 
    (POST_TITLE ILIKE '%MRNA%'
    OR POST_TITLE ILIKE '%MODERNA%'
    OR COMMENT ILIKE '%MRNA%'
    OR COMMENT ILIKE '%MODERNA%')