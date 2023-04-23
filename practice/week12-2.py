import csv

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

def fprint(line):
    for e, w in zip(line, [5]*16+[6]*3+[5]*9+[6]*3+[8]):
        x = len(str(e))
        if '.' not in str(e): print(' '*(w-x)+str(e),end='')
        else: print(f' {e:.3f}', end='')
    print()

fields, year_data = ReadDataFromFile('cpbl-player-batter-1990-2019.csv')

#print(' '*3,end='')
print(fields)

num = 0
for p in year_data:
    if p['SAC']+p['SF']>=30:
        fprint(p.values())
        num += 1
print('共計', num, '筆')

