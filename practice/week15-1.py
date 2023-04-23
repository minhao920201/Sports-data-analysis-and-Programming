import pandas as pd
import matplotlib.pyplot as plt

box = pd.read_excel('2019FIBA_WC_R1_box_score.xlsx').to_dict('records') #適用只有一張工作表

N = len(box)//2	#比賽場數 = 資料列數除以2

win = [0]*N	#由 N 個 0 構成的列表	
lose = [0]*N

metric = 'DREB'
for row in box:
    i = row['order'] #第幾場比賽
    if row['勝敗'] == 'W':
        win[i-1] = row[metric]
    else:
        lose[i-1] = row[metric]

plt.figure(figsize=(6,6))
plt.plot([0,50],[0,50],color = 'gray')
plt.plot(win, lose, 'o') #以勝隊數值為 x 值，敗隊數值為 y 值
plt.xlabel('勝隊數值')
plt.ylabel('敗隊數值')
plt.title('FIBA2019 勝負隊 ' + metric + ' 數據')
plt.show()
