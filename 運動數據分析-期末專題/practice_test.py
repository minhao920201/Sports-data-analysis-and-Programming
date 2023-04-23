import csv
from matplotlib import pyplot as plt
def ReadDataFromFile(filename):
    '''
    傳入 csv 檔名 filename
    傳回 欄位, 檔案內容
    '''
    with open(filename) as infile:
        csvfile = csv.DictReader(infile)
        data = list(csvfile)
        for row in data:
            for k in row:
                if '.' in row[k]:
                    row[k] = float(row[k])
                elif row[k].isdigit():
                    row[k] = int(row[k])
        return csvfile.fieldnames, data

fields,year_data = ReadDataFromFile("Boy_Group.csv")
#print(fields)

dic_count = {"count_two_point_shot":0,"count_three_point_shot":0,"count_penalty_shot":0}

#讓比賽球隊倆倆比較
for i in range(0,len(year_data),2):
    for j in range(i+1,len(year_data),2):
        dic_hit_rate = {"two_point_shot":0,"three_point_shot":0,"penalty_shot":0}
        if year_data[i]["勝負"] == "勝":
            for word in dic_hit_rate:
                dic_hit_rate[word] = round(year_data[i][word] - year_data[j][word],2)
        else:
            for word in dic_hit_rate:
                dic_hit_rate[word] = round(year_data[j][word] - year_data[i][word],2)
        print(dic_hit_rate)

        largest = 0
        for k in dic_hit_rate:
            if dic_hit_rate[k] > largest:
                largest = dic_hit_rate[k]
                largest_name = k

        if largest_name == "two_point_shot":
            dic_count["count_two_point_shot"] += 1
        elif largest_name == "three_point_shot":
            dic_count["count_three_point_shot"] += 1
        else:
            dic_count["count_penalty_shot"] += 1
        print(largest,largest_name)
        break
print(dic_count)

li = []
for key in dic_count:
    li.append(dic_count[key])
#print(li)
plt.title("進球率與比賽勝負關係圖")
plt.xlabel("進球率")
plt.ylabel("次數")
plt.bar(["二分球","三分球","罰球"],li)
plt.show()
