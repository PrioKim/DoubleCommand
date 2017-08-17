import requests
import datetime

iter_date = datetime.date(2007, 1, 1)
end_date = datetime.date(2017, 8, 17)


while iter_date != end_date:
        str_date = iter_date.strftime('%Y-%m-%d')

        url = 'http://www.kobis.or.kr/kobis/business/stat/boxs/findDailyBoxOfficeList.do'
        get_params = {'loadEnd':'0', 'searchType':'excel', 'sSearchFrom':str_date, 'sSearchTo':str_date}

        r = requests.get(url, allow_redirects=True, params=get_params)
        open(str_date + '.xls', 'wb').write(r.content)
        iter_date = iter_date + datetime.timedelta(days=1)
