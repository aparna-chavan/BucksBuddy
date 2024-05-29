{{
  config(
    materialized = 'table',
    )
}}

WITH src_DE AS (
    SELECT * FROM {{ ref("src_DE") }}
)

SELECT 
    *, 'DE' AS ticker
FROM 
    src_DE
WHERE 
    (POST_TITLE ILIKE '%DE%'
    OR POST_TITLE ILIKE '%JOHN DEERE%'
    OR POST_TITLE ILIKE '%JOHN%'
    OR POST_TITLE ILIKE '%DEERE%'
    OR POST_TITLE ILIKE '%DEER%'
    OR COMMENT ILIKE '%DE%'
    OR COMMENT ILIKE '%DE%'
    OR COMMENT ILIKE '%JOHN DEERE%'
    OR COMMENT ILIKE '%JOHN%'
    OR COMMENT ILIKE '%DEERE%'
    OR COMMENT ILIKE '%DEER%')
    
