
select distinct to_date(left(date,10), 'dd/mm/yyyy') txdate, avg(speed) over (partition by left(date,10)) avg_speed 
from {{ref('tfl_review')}}
order by 1

--select distinct site_id, count(*) over (partition by site_id ) from {{ref('tfl_review')}}