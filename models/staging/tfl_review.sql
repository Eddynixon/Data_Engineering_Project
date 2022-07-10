select * from {{ source('tfl', 'TFL_TABLE') }}
where site_number != 'SITE_NUMBER'