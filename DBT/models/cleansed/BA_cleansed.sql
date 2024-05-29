{{
  config(
    materialized = 'table',
    )
}}

WITH src_BA AS (
    SELECT * FROM {{ ref("src_BA") }}
)

SELECT 
    *, 'BA' AS ticker
FROM 
    src_BA
WHERE 
    (POST_TITLE ILIKE '%BA%'
    OR POST_TITLE ILIKE '%BOEING%'
    OR COMMENT ILIKE '%BA%'
    OR COMMENT ILIKE '%BOEING%')