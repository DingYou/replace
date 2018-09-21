import xlrd
import json
import requests

ExcelFile = "/Users/dingyou/Downloads/小学英语词汇/小学英语词汇1.4.xlsx"
Type = 1
url = "127.0.0.1:8080/library/mix/insertMixWords"

excel = xlrd.open_workbook(ExcelFile)
sheet_names = excel.sheet_names()

sheet = excel.sheet_by_name("不可同时出现")

rowNum = sheet.nrows
colNum = sheet.ncols

for i in range(0, rowNum):
    words = list()
    for j in range(0, colNum):
        value = sheet.cell(i, j).value.strip()
        if value != '':
            words.append(value)
    params = dict()
    params['type'] = Type
    params['words'] = words
    json_params = json.dumps(params)
    print(json_params)
    response = requests.post(url, json_params)
    print(response.json())

