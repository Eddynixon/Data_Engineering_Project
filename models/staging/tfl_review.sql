with tfl_tbl_review as (
select * from {{ source('tfl', 'TFL_TABLE') }}
where site_number != 'SITE_NUMBER')
select * from tfl_tbl_review