from base64 import encode
import csv
import os.path
import json
from pprint import pprint


taste_dict = {
    'kko_deul': ['꼬들꼬들', '꼬들'],
    'taeng_geul': ['탱글탱글', '탱글'],
    'jjol_git': ['쫄깃쫄깃', '쫄깃'],

    'green Onion': ['대파', '파'],
    'egg': ['달걀' ,'계란'],
    'beef': ['소고기', '쇠고기', '한우'],
    'pork': ['돼지고기', '돈육', '삼겹살', '목살', '삼겹'],
    'chicken_breast': ['닭가슴살', '닭 가슴살', '닭찌찌', '닭 찌찌'],
    'milk': ['우유'],
    'rice_cake': ['떡'],
    'dumpling': ['만두'],
    'soft_tofu': ['순두부'],
    'kimchi': ['김치'],
    'mayonnaise': ['마요네즈'],
    'cheese': ['치즈'],
    'garlic': ['마늘'],
    'pepper': ['후추'],
    'chili_powder': ['고춧가루', '고추가루'],
    'bean sprouts': ['숙주'],
    'cabbage': ['양배추'],
    'carrot': ['당근'],
    'paprika': ['파프리카'],
    'pumpkin': ['호박'],
    'mushroom': ['버섯'],
    'potato': ['감자'],
    'red pepper': ['고추'],
    'soya sprouts': ['콩나물'],
    'seefood': ['새우', '꽃게', '문어', '오징어', '조개', '맛살', '대하'],
    'seaweed': ['미역'],
    'sausage': ['소세지, 햄', '베이컨', '스팸'],
    'eomuk': ['어묵'],
    'tuna': ['참치'],
    'ketchup': ['케찹', '케챱', '케첩'],

    'vegan': ['비건', '채식주의', '채식'],
    'outdoor': ['한강', '캠핑', '바다', '여행', '등산', '등반', '해수욕장', '해변', '야영', '낚시'],
    'morning': ['아침', '조식'],
    'lunch': ['점심', '중식'],
    'dinner': ['저녁', '석식'],
    'midnight_snack': ['야식', '야참', '밤참'],
    'diet': ['다이어트', '식이요법', '식단', '건강'],

    'not_spicy': ['안 매워', '안매워', '안 맵', '안맵', '안 매운', '안매운', '순한', '순하', '순함'],
    'spicy' : ['맵싸', '맵게', '맵깔', '맵',  '매콤', '매운', '매워', '알싸'],
    'delicious': ['존맛', '꿀맛', '맛있', '맛잇'],
    'not_delicious': ['노맛', '맛없'],
    'lightness': ['담백', '깔끔', '개운'],
    'Haejang': ['얼큰', '해장']
}

taste_list = list(taste_dict.keys())

# 라면 제품명 가져오기
f = open('Ramen_nickname.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
ramen_data = []
for line in rdr:
    ramen_data.append(line)
f.close()

ramen_data = ramen_data[1:]

ramen_id = []
ramen_names = []
ramen_nicknames = []
# 제품 개수
for line in ramen_data:
    ramen_id.append(line[11])
    ramen_names.append(line[2])
    ramen_nicknames.append(line[3])

ramen_result = {key: {} for key in ramen_id}
for key in ramen_id:
    ramen_result[key] = {
        'kko_deul': 0,
        'taeng_geul': 0,
        'jjol_git': 0,

        'green Onion': 0,
        'egg': 0,
        'beef': 0,
        'pork': 0,
        'chicken_breast': 0,
        'milk': 0,
        'rice_cake': 0,
        'dumpling': 0,
        'soft_tofu': 0,
        'kimchi': 0,
        'mayonnaise': 0,
        'cheese': 0,
        'garlic': 0,
        'pepper': 0,
        'chili_powder': 0,
        'bean sprouts': 0,
        'cabbage': 0,
        'carrot': 0,
        'paprika': 0,
        'pumpkin': 0,
        'mushroom': 0,
        'potato': 0,
        'red pepper': 0,
        'soya sprouts': 0,
        'seefood': 0,
        'seaweed': 0,
        'sausage': 0,
        'eomuk': 0,
        'tuna': 0,
        'ketchup': 0,

        'vegan': 0,
        'outdoor': 0,
        'morning': 0,
        'lunch': 0,
        'dinner': 0,
        'midnight_snack': 0,
        'diet': 0,

        'not_spicy': 0,
        'spicy' : 0,
        'delicious': 0,
        'not_delicious': 0,
        'lightness': 0,
        'Haejang': 0,
        'tweet_cnt': 0,
        'blog_cnt': 0,
        'crawling_cnt': 0,
    }




print('라면 데이터 수: ', len(ramen_names))
no_txt = []
no_crawling = []
for ramen_index in range(len(ramen_names)):
    print(ramen_index + 1, " 번째 라면 형태소 분석중")
    filename = './블로그 크롤링/' + ramen_names[ramen_index] + '.txt'
    if os.path.isfile(filename):
        f = open(filename, 'r', encoding='utf-8')
        texts = f.readlines()
        # txt: O, data: X
        if not texts:
            no_crawling.append(ramen_names[ramen_index])        
        # txt: O, data: O
        else:
            for text in texts:
                if text[0] == '=':
                    ramen_result[ramen_id[ramen_index]]['blog_cnt'] += 1
                    ramen_result[ramen_id[ramen_index]]['crawling_cnt'] += 1
                else:
                    flag = False
                    for taste_key_index in range(len(taste_list)):
                        taste_cnt = 0
                        for taste in taste_dict[taste_list[taste_key_index]]:
                            cnt = 0
                            while text.count(taste) != 0:
                                idx = text.index(taste)
                                length = len(taste)
                                text = text[:idx] + text[idx+length:]
                                cnt += 1
                                flag = True
                            taste_cnt += cnt
                        ramen_result[ramen_id[ramen_index]][taste_list[taste_key_index]] += taste_cnt

                    
    # txt: X
    else:
        no_txt.append(ramen_names[ramen_index])


with open('Ramen_taste.json', 'w', encoding='utf-8') as f:
    json.dump(ramen_result, f, indent=4)


