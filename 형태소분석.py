import csv
import os.path
import json



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
for line in ramen_data[1:100]:
    ramen_names.append(line[3])
    keys.append(line[11])

ramen_result = {key: {} for key in keys}

for idx1 in range(len(ramen_names)):
    print(ramen_names[idx1])
    filename = ramen_names[idx1] + '_2016_0101_2021_1231.csv'

    if os.path.isfile(filename):
        f = open(filename, 'r', encoding="utf-8")
        rdr = csv.reader(f)
        data = []
        for line in rdr:
            data.append(line)
        f.close()
        taste_dict = {'kko_deul': ['꼬들꼬들', '꼬들'],
                    'taeng_geul': ['탱글탱글', '탱글'],
                    'jjol_git': ['쫄깃쫄깃', '쫄깃'],

                    'green Onion': ['대파', '파'],
                    'egg': ['달걀' ,'계란'],
                    'beef': ['소고기', '쇠고기'],
                    'pork': ['돼지고기', '돈육'],
                    'chicken_breast': ['닭가슴살', '닭찌찌', '닭 찌찌'],
                    'milk': ['우유'],
                    'rice_cake': ['떡'],
                    'dumpling': ['만두'],
                    'soft_tofu': ['순두부'],
                    'kimchi': ['김치'],
                    'mayonnaise': ['마요네즈'],
                    'cheese': ['치즈'],
                    'garlic': ['마늘'],
                    'pepper': ['후추'],
                    'chili_powder': ['고춧가루'],

                    'vegan': ['비건', '채식주의', '채식'],
                    'outdoor': ['한강', '캠핑', '바다', '여행'],
                    'morning': ['아침', '조식'],
                    'lunch': ['점심', '중식'],
                    'dinner': ['저녁', '석식'],
                    'midnight_snack': ['야식'],
                    'diet': ['다이어트', '식단'],

                    'not_spicy': ['안 매워', '안매워', '안 맵', '안맵', '안 매운', '안매운', '순한', '순하', '순함'],
                    'spicy' : ['맵싸', '맵게', '맵깔', '맵',  '매콤', '매운', '매워', '알싸'],
                    'delicious': ['존맛', '꿀맛'],
                    'not_delicious': ['노맛', '맛없'],
                    'lightness': ['담백', '깔끔', '개운'],
                    # '해장': ['얼큰', '해장']
                    }
        ans = {'tweet_cnt': 0}
        tweet_cnt = 0
        for key in taste_dict.keys():
            ans[key] = 0

        taste_list = list(taste_dict.keys())
        for i in range(1, len(data)):
            tweet = data[i][10]
            flag = False
            for key_idx in range(len(taste_dict.keys())-1):
                taste_cnt = 0
                for taste in taste_dict[taste_list[key_idx]]:
                    cnt = 0
                    while tweet.count(taste) != 0:
                        idx = tweet.index(taste)
                        length = len(taste)
                        tweet = tweet[:idx] + tweet[idx+length:]
                        cnt += 1
                        tweet_cnt += 1
                        flag = True
                    taste_cnt += cnt
                ans[taste_list[key_idx]] += taste_cnt
            ans['tweet_cnt'] = tweet_cnt
        ramen_result[keys[idx1]] = ans

with open('Ramen_taste.json', 'w', encoding='utf-8') as f:
    json.dump(ramen_result, f, indent=4)