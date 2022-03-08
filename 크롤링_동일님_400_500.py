from datetime import date, timedelta
import twint
import csv
import time


# 크롤링 날짜 지정
def dete_range(start_date, end_date, delta):
    ans = [end_date]
    for _ in range((end_date - start_date).days):
        end_date -= delta
        ans.append(end_date)
    return ans

start_date = date(2016, 1, 1)
end_date = date(2021,12,31)
delta = timedelta(days=1)
crolling_days = dete_range(start_date, end_date, delta)


# 라면 제품명 가져오기
f = open('Ramen_nickname.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
ramen_data = []
for line in rdr:
    ramen_data.append(line)
f.close()


column_name = ramen_data[0]
ramen_names = []
keys = []
# 제품 개수
for line in ramen_data[400:]:
    ramen_names.append(line[3])
    keys.append(line[11])

ramen_result = {key: {} for key in keys}

for idx1 in range(len(ramen_names)):
    print(ramen_names[idx1])
    filename = ramen_names[idx1] + '_2016_0101_2021_1231.csv'
    for day in crolling_days:
        c = twint.Config()
        c.Search = ramen_names[idx1]
        c.Since = str(day)
        c.Until = str(day+delta)
        c.Store_csv = True
        c.Output = "none"
        c.Output = filename
        while True:
            flag = False
            try:
                twint.run.Search(c)
            except twint.token.RefreshTokenException:
                print('RefreshTokenException')
                flag = True
            
            if not flag:
                break
            if flag:
                continue