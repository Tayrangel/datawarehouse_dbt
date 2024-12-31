WITH
    source AS (
        SELECT
            *
        FROM "dbdatawarehouse"."public"."commodities"
    )

    ,transformed AS (
        SELECT
            CAST(TO_CHAR(date, 'YYYY-MM-DD') AS date) AS extract_dt
            ,ROUND(CAST("Close" AS NUMERIC), 2) AS close_vl
            ,symbol
        FROM source
    )

SELECT
    *
FROM transformed