import csv
from matplotlib import pyplot as plt
#開檔+將數字轉換成整數及浮點數
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

def CompareDataFromFile(data,session): #data:接收開檔後的資料，session:接收賽事類別
    dic_count = {"count_two_point_shot":0,"count_three_point_shot":0,"count_penalty_shot":0} #紀錄勝隊二分三分罰球進球率哪項較高，較高者則加1
    #讓比賽球隊倆倆比較
    for i in range(0,len(data),2):
        for j in range(i+1,len(data),2):
            dic_hit_rate = {"two_point_shot":0,"three_point_shot":0,"penalty_shot":0} #紀錄兩球隊各項進球率的差距
            if data[i]["準決賽/決賽"] == session: #先判斷是決賽還是準決賽
                if data[i]["勝負"] == "勝": #在判斷誰勝誰負，以"勝隊的進球率"為"被減數"，"輸球隊的進球率"為"減數"
                    for word in dic_hit_rate:
                        dic_hit_rate[word] = round(data[i][word] - data[j][word],2)
                else:
                    for word in dic_hit_rate:
                        dic_hit_rate[word] = round(data[j][word] - data[i][word],2)
            #print(dic_hit_rate)

                largest = -1 #獲勝球隊各項進球率可能比輸球球隊低，因此設為-1
                #判斷二分球進球率、三分球進球率及罰球進球率的大小
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
                print(largest,largest_name) #印出每個比賽勝隊中進球率最大值
            break
    print(dic_count) #印出dic_count字典中統計出來的結果
    return dic_count

#顯示分析後的圖表
def ShowPlot(data,session_name): #data:利用CompareDataFromFile函式整理過的資料，session_name:賽事為決賽或準決賽
    li_name = []
    li_value = []
    for key in data:
        li_name.append(key)
        li_value.append(data[key])
    #print(li)
    plt.title("進球率與比賽勝負關係圖-"+session_name)
    plt.xlabel("進球率")
    plt.ylabel("次數")
    plt.bar(li_name,li_value)
    plt.savefig("進球率與比賽勝負關係圖-"+session_name)
    plt.show()



fields,year_data = ReadDataFromFile("Girl_Group.csv") #這邊需換檔名，因為分成兩個EXCEL檔

dic_semi_final = CompareDataFromFile(year_data,"準決賽")
dic_finals = CompareDataFromFile(year_data,"決賽")

ShowPlot(dic_semi_final,"準決賽")
ShowPlot(dic_finals,"決賽")
