{{
  config(
    materialized = 'table',
    )
}}

WITH src_FDX AS (
    SELECT * FROM {{ ref("src_FDX") }}
)

SELECT 
    *, 'FDX' AS ticker
FROM 
    src_FDX
WHERE 
    (POST_TITLE ILIKE '%FDX%'
    OR POST_TITLE ILIKE '%FEDEX%'
    OR COMMENT ILIKE '%FDX%'
    OR COMMENT ILIKE '%FEDEX%')
