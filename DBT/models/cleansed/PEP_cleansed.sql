{{
  config(
    materialized = 'table',
    )
}}

WITH src_PEP AS (
    SELECT * FROM {{ ref("src_PEP") }}
)

SELECT 
    *, 'PEP' AS ticker
FROM 
    src_PEP
WHERE 
    (POST_TITLE ILIKE '%PEP%'
    OR POST_TITLE ILIKE '%PEPSI%'
    OR COMMENT ILIKE '%PEP%'
    OR COMMENT ILIKE '%PEPSI%')
