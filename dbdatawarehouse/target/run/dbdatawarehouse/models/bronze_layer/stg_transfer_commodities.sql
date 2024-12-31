
  create view "dbdatawarehouse"."public"."stg_transfer_commodities__dbt_tmp"
    
    
  as (
    WITH
    source AS (
        SELECT
            *
        FROM "dbdatawarehouse"."public"."transfer_commodities"
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
  );