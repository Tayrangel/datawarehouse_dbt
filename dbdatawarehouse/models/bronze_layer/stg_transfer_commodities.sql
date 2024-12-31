WITH
    source AS (
        SELECT
            *
        FROM {{ source('dbdatawarehouse', 'transfer_commodities') }}
    )

    ,transformed AS (
        SELECT
            CAST(date AS date) AS extract_dt
            ,symbol
            ,action
            ,quantity
        FROM source
    )

SELECT
    *
FROM transformed