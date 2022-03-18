import csv

f = open('Ramen_nickname.csv', 'r', encoding='utf-8')
rdr = csv.reader(f)
ramen_data = []
for line in rdr:
    ramen_data.append(line)
f.close()

Energy = []
Protein = []
Lipids = []
Carbohydrates = []
sugars = []
Sodium = []
# print(ramen_data[0][16])
# print(ramen_data[0][18])
# print(ramen_data[0][19])
# print(ramen_data[0][20])
# print(ramen_data[0][21])
# print(ramen_data[0][22])

for i in range(1, len(ramen_data)):
    Energy.append(float(ramen_data[i][16]))
    Protein.append(float(ramen_data[i][18]))
    Lipids.append(float(ramen_data[i][19]))
    Carbohydrates.append(float(ramen_data[i][20]))
    sugars.append(float(ramen_data[i][21]))
    Sodium.append(float(ramen_data[i][22]))
print("에너지: {}".format(sum(Energy) / len(ramen_data) - 1))
print("단백질: {}".format(sum(Protein) / len(ramen_data) - 1))
print("지질: {}".format(sum(Lipids) / len(ramen_data) - 1))
print("탄수화물: {}".format(sum(Carbohydrates) / len(ramen_data) - 1))
print("총 당류: {}".format(sum(sugars) / len(ramen_data) - 1))
print("나트륨: {}".format(sum(Sodium) / len(ramen_data) - 1))
