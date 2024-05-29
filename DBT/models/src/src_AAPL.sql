

WITH raw_AAPL AS (
    SELECT *
    FROM {{ source('BUCKSBUDDY', 'raw_AAPL') }}
)
SELECT 
    TITLE AS POST_TITLE,
    ID AS POST_ID,
    AUTHOR AS POST_AUTHOR,
    SCORE AS POST_SCORE,
    COMMENT_AUTHOR AS COMMENT_AUTHOR,
    COMMENT AS COMMENT
FROM 
    raw_AAPL