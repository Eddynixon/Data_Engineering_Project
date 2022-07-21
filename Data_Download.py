import datetime
import calendar
from urllib import request
#request.urlretrieve(url_1,file_name)
def findDay(date):
    born = datetime.datetime.strptime(date, '%d %m %Y').weekday()
    return (calendar.day_name[born])


day = 1
while day <= 30:
    try:
        date = "%01d" % (day,)+' 07 2018'
        #date = day+' 06 2018'
        dy = datetime.datetime.strptime(date, '%d %m %Y').weekday()
        dy = "%01d" % (day,)
        url_prefix = 'https://cycling.data.tfl.gov.uk/CycleCounters/Blackfriars/July/'
        #url_prefix = "https://cycling.data.tfl.gov.uk/CycleCounters/Blackfriars/June/Jun%20"
        #url_prefix = "https://cycling.data.tfl.gov.uk/CycleCounters/Blackfriars/May/May%20"
        furl =f"{url_prefix}{findDay(date)}{',%20Jul%20'}{dy}{'%202018.xls'}" # July URL format
        #furl = f"{url_prefix}{dy}{'%202018.xls'}"
        file_name = 'Output'+ "%01d" % (day,)+'_07_2018.csv'
        file_path ='C:/Users/HP/Documents/my_git/data-engineering-zoomcamp/week_1_basics_n_setup/2_docker_sql/tfl_download'
        file_dest = f"{file_path}/{file_name}"
        request.urlretrieve(furl,file_dest)
        print(date, 'download completed, uploading into data warehouse')
    except:
        print(furl)
        pass     
    day += 1

