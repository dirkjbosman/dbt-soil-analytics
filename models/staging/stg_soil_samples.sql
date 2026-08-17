select
    sample_id,
    location_code,
    trim(region) as region,
    latitude,
    longitude,
    cast(collection_date as date) as collection_date,
    round(ph_level, 2) as ph_level,
    round(organic_matter_pct, 2) as organic_matter_pct,
    round(nitrogen_g_kg, 2) as nitrogen_g_kg,
    round(phosphorus_mg_kg, 2) as phosphorus_mg_kg,
    round(potassium_mg_kg, 2) as potassium_mg_kg,
    round(bulk_density_g_cm3, 2) as bulk_density_g_cm3,
    case 
        when ph_level < 5.5 then 'Strongly Acidic'
        when ph_level between 5.5 and 6.5 then 'Moderately Acidic'
        when ph_level between 6.6 and 7.3 then 'Neutral'
        else 'Alkaline'
    end as acidity_class
from read_csv_auto('data/raw_soil_samples.csv')