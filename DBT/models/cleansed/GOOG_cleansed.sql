{{
  config(
    materialized = 'table',
    )
}}

WITH src_GOOG AS (
    SELECT * FROM {{ ref("src_GOOG") }}
)

SELECT 
    *, 'GOOG' AS ticker
FROM 
    src_GOOG
WHERE 
    (POST_TITLE ILIKE '%GOOG%'
    OR POST_TITLE ILIKE '%GOOGLE%'
    OR COMMENT ILIKE '%GOOG%'
    OR COMMENT ILIKE '%GOOGLE%')