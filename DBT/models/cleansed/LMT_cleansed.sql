{{
  config(
    materialized = 'table',
    )
}}

WITH src_LMT AS (
    SELECT * FROM {{ ref("src_LMT") }}
)

SELECT 
    *, 'LMT' AS ticker
FROM 
    src_LMT
WHERE 
    (POST_TITLE ILIKE '%LMT%'
    OR POST_TITLE ILIKE '%LOCKHEED%'
    OR POST_TITLE ILIKE '%MARTIN%'
    OR COMMENT ILIKE '%LMT%'
    OR COMMENT ILIKE '%LOCKHEED%'
    OR COMMENT ILIKE '%MARTIN%')
