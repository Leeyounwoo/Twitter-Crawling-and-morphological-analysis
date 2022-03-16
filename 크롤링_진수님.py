from datetime import date, timedelta
import twint
import csv
import time
import os.path



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

crolling_days = crolling_days[:-1]
print(len(crolling_days), crolling_days[-1])
# 라면 제품명 가져오기
f = open('Ramen_nickname.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
ramen_data = []
for line in rdr:
    ramen_data.append(line)
f.close()


# ramen_names = ['신림동 백순대 볶음면 컵', '간짬뽕 라면', '삼양 튀김칼국수 컵', '삼양 된장라면']
# ramen_names = ['나가사끼짬뽕 큰컵', '쇠고기면 큰컵', '삼양 김치찌개 큰컵', '삼양라면 큰컵']
# ramen_names = ['국민컵라면', '삼양 컵육개장', '삼양 고추짬뽕 컵', '나가사끼짬뽕 컵', '삼양라면 매운맛 컵']
# ramen_names = ['삼양라면 컵', '삼양라면 컵 오리지널', '삼계탕면 컵', '삼양라면 골드 컵', '미원라면 컵']
ramen_names = ['하이리빙파워 미니컵', '삼양 맛있는라면 컵', '삼양라면 매운맛 컵', '삼양 유부우동 큰컵']


print(len(ramen_names))
print(ramen_names)
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
        # time.sleep(2)
        while True:
            flag = False
            try:
                twint.run.Search(c)
            except twint.token.RefreshTokenException:
                # time.sleep(2)
                print('RefreshTokenException')
                flag = True
            
            if not flag:
                break
            if flag:
                continue