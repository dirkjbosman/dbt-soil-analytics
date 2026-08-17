{{ config(materialized='table') }}
select distinct
    location_code,
    region,
    latitude,
    longitude
from {{ ref('stg_soil_samples') }}
