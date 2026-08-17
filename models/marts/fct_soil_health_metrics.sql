{{ config(materialized='table') }}
with base as (
    select * from {{ ref('stg_soil_samples') }}
)
select
    sample_id,
    location_code,
    collection_date,
    ph_level,
    acidity_class,
    organic_matter_pct,
    case 
        when nitrogen_g_kg < 1.0 then 'Deficient'
        when nitrogen_g_kg between 1.0 and 2.5 then 'Optimal'
        else 'High'
    end as nitrogen_status,
    case 
        when phosphorus_mg_kg < 20.0 then 'Low'
        when phosphorus_mg_kg between 20.0 and 45.0 then 'Medium'
        else 'High'
    end as phosphorus_status,
    case 
        when bulk_density_g_cm3 > 1.40 then 'High Restriction (Compacted)'
        when bulk_density_g_cm3 between 1.20 and 1.40 then 'Moderate'
        else 'Ideal'
    end as compaction_risk
from base
