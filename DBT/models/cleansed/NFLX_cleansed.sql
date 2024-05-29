{{
  config(
    materialized = 'table',
    )
}}

WITH src_NFLX AS (
    SELECT * FROM {{ ref("src_NFLX") }}
)

SELECT 
    *, 'NFLX' AS ticker
FROM 
    src_NFLX
WHERE 
    (POST_TITLE ILIKE '%NFLX%'
    OR POST_TITLE ILIKE '%NETFLIX%'
    OR COMMENT ILIKE '%NFLX%'
    OR COMMENT ILIKE '%NETFLIX%')
