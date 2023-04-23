import csv
import matplotlib.pyplot as plt

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
#-----------------------------------------------------------------------
def fprint(line):
    for e, w in zip(line, [5]*16+[6]*3+[5]*9+[6]*3+[8]):
        x = len(str(e))
        if '.' not in str(e): print(' '*(w-x)+str(e),end='')
        else: print(f' {e:.3f}', end='')
    print()
#-----------------------------------------------------------------------
def GetPlayerRecord(fields, year_data):
    player_data = {}
    for p in year_data:
        name = p['NAME']
        if name not in player_data:
            player_data[name] = {}
            for field in fields[2:]:
                player_data[name][field] = []
        for field in fields[2:]:
            player_data[name][field].append(p[field])
    return player_data
#-----------------------------------------------------------------------
def mean(vals):
    if len(vals)>0:
        return sum(vals)/len(vals)
    else:
        return 0

#-----------------------------------------------------------------------
# 上面的程式碼先不要管它們
#-----------------------------------------------------------------------

fields, year_data = ReadDataFromFile('cpbl-player-batter-1990-2019.csv')
player_data = GetPlayerRecord(fields, year_data)

plt.figure(figsize=(12,5))  #設定圖表大小
name = '彭政閔'
pd = player_data[name]
plt.plot(pd['YEAR'], pd['AVG']) #繪製折線圖
plt.xticks(range(pd['YEAR'][0], pd['YEAR'][-1]+1)) #設定 x 軸刻度
plt.xlabel('年度')
plt.ylabel('打擊率')
plt.title(name+'生涯打擊率', loc='left')
plt.show()
