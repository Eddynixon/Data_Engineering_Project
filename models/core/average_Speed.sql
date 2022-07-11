{%- materialization my_view, default -%}

  {%- set target_relation = api.Relation.create(
        identifier=identifier, schema='DWH', database='analytics',
        type='table') -%}
   -- ... setup database ...
  -- ... run pre-hooks...

  -- build model
  {% call statement('main') -%}
    {{ create_table_as(target_relation, sql) }}
  {%- endcall %}
  
  -- ... run post-hooks ...
  -- ... clean up the database...

  -- Return the relations created in this materialization
  {{ return({'relations': [target_relation]}) }}


{%- endmaterialization -%}

select distinct to_date(left(date,10), 'dd/mm/yyyy') txdate, avg(speed) over (partition by left(date,10)) avg_speed 
from {{ref('tfl_review')}}
order by 1