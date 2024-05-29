{{
  config(
    materialized = 'table',
    )
}}

WITH src_PFE AS (
    SELECT * FROM {{ ref("src_PFE") }}
)

SELECT 
    *, 'PFE' AS ticker
FROM 
    src_PFE
WHERE 
    (POST_TITLE ILIKE '%PFE%'
    OR POST_TITLE ILIKE '%PFIZER%'
    OR COMMENT ILIKE '%PFE%'
    OR COMMENT ILIKE '%PFIZER%')