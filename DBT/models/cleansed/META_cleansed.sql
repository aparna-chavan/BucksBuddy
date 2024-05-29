{{
  config(
    materialized = 'table',
    )
}}

WITH src_META AS (
    SELECT * FROM {{ ref("src_META") }}
)

SELECT 
    *, 'META' AS ticker
FROM 
    src_META
WHERE 
    (POST_TITLE ILIKE '%META%'
    OR POST_TITLE ILIKE '%META%'
    OR COMMENT ILIKE '%META%'
    OR COMMENT ILIKE '%META%')