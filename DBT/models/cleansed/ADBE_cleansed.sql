{{
  config(
    materialized = 'table',
    )
}}

WITH src_ADBE AS (
    SELECT * FROM {{ ref("src_ADBE") }}
)

SELECT 
    *, 'ADBE' AS ticker
FROM 
    src_ADBE
WHERE 
    (POST_TITLE ILIKE '%ADBE%'
    OR POST_TITLE ILIKE '%ADOBE%'
    OR COMMENT ILIKE '%ADBE%'
    OR COMMENT ILIKE '%ADOBE%')