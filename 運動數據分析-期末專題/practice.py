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

fields,year_data = ReadDataFromFile("practice.csv")
#print(fields)
for i in range(0,len(year_data),2):
    for j in range(i+1,len(year_data),2):
        two_point_shoot = 0
        three_point_shoot = 0
        penalty_shot = 0
        if year_data[i]["勝負"] == "勝":
            two_point_shoot = year_data[i]["二分球命中率"] - year_data[j]["二分球命中率"]
            three_point_shoot = year_data[i]["三分球命中率"] - year_data[j]["三分球命中率"]
            penalty_shot = year_data[i]["罰球命中率"] - year_data[j]["罰球命中率"]
        else:
            two_point_shoot = year_data[j]["二分球命中率"] - year_data[i]["二分球命中率"]
            three_point_shoot = year_data[j]["三分球命中率"] - year_data[i]["三分球命中率"]
            penalty_shot = year_data[j]["罰球命中率"] - year_data[i]["罰球命中率"]
        print(round(two_point_shoot,2),round(three_point_shoot,2),round(penalty_shot,2))
        break
"""
school_data = {}
for p in year_data:
    school = p['學校']
    if school not in school_data:
        school_data[school] = {}
        for field in p:
            if field != '學校':
                school_data[school][field] = []
    for field in p:
        if field != '學校':
            school_data[school][field].append(p[field])
for school in school_data:
    print(school,school_data[school])
"""
