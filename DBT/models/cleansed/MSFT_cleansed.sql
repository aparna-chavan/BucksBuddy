{{
  config(
    materialized = 'table',
    )
}}

WITH src_MSFT AS (
    SELECT * FROM {{ ref("src_MSFT") }}
)

SELECT 
    *, 'MSFT' AS ticker
FROM 
    src_MSFT
WHERE 
    (POST_TITLE ILIKE '%MSFT%'
    OR POST_TITLE ILIKE '%MICROSOFT%'
    OR COMMENT ILIKE '%MSFT%'
    OR COMMENT ILIKE '%MICROSOFT%')