{{
  config(
    materialized = 'ephemeral',
    )
}}

WITH raw_META AS (
    SELECT *
    FROM {{ source('BUCKSBUDDY', 'raw_META') }}
)
SELECT 
    TITLE AS POST_TITLE,
    ID AS POST_ID,
    AUTHOR AS POST_AUTHOR,
    SCORE AS POST_SCORE,
    COMMENT_AUTHOR AS COMMENT_AUTHOR,
    COMMENT AS COMMENT
FROM 
    raw_META
