
  create view "dbdatawarehouse"."public"."fct_commodities__dbt_tmp"
    
    
  as (
    WITH
    commodities AS (
        SELECT
            *
        FROM "dbdatawarehouse"."public"."stg_commodities"
    )

    ,transfer_commodities AS (
        SELECT
            *
        FROM "dbdatawarehouse"."public"."stg_transfer_commodities"
    )

    ,join_tables AS (
        SELECT
            c.extract_dt
            ,c.symbol
            ,c.close_vl
            ,tc.action
            ,tc.quantity
        FROM commodities AS c
            LEFT JOIN transfer_commodities AS tc
                ON c.extract_dt = tc.extract_dt
                AND tc.symbol = c.symbol
    )

    ,aggregation AS (
        SELECT
            *
            ,(quantity * close_vl) AS total_vl
            ,CASE
                WHEN action = 'sell' THEN (quantity * close_vl)
                ELSE (quantity * close_vl) * -1
            END AS profit_vl
        FROM join_tables
    )

SELECT
    *
FROM aggregation
  );