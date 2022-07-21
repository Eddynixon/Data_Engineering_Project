
import datetime
import calendar
from urllib import request
#request.urlretrieve(url_1,file_name)

 
import os 
import snowflake.connector

user_name = os.environ.get('SNOW_USER')
password = os.environ.get('SNOW_PASSWORD')
account = os.environ.get('SNOW_ACCOUNT')
conn = snowflake.connector.connect(
                user=user_name,
                password=password,
                account=account,
                warehouse='Data_Engineering_Project',
                database='analytics',
                schema='analytics_project'
                )

day = 1
while day <= 30:
    try:
        date = "%01d" % (day,)+' 07 2018'
        #date = day+' 06 2018'
        file_name = 'Output'+ "%01d" % (day,)+'_07_2018.csv'
        file_path ='C:/Users/HP/Documents/my_git/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql/tfl_download'
        file_dest = f"{file_path}/{file_name}"
        conn.cursor().execute(f"{'PUT file://'}{file_dest} {'@%tfl_table'}")
        conn.cursor().execute("COPY INTO analytics.analytics_project.tfl_table ON_ERROR=CONTINUE")
        print(date, 'upload into DWH completed')
    except:
        pass     
    day += 1