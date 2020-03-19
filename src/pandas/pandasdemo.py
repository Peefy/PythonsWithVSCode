
import sys
import math
from copy import deepcopy

import pandas as pd
from pandas import DataFrame

MATERIAL_KEYWORDS = ['写真', '喷绘', '背胶', '相纸', '反光', '字', '条幅', '旗', '平板打印', '雕刻', '车贴','其它']
HEADERS = ['订单编号','开单日期','客户名称', '业务员', '付款状态', '项目名称', '耗材',	'制作内容',	'规格', '数量', '单位',	'面积',	'单价',	'金额', '备注']
price_index = HEADERS.index('金额')
name_index = HEADERS.index('业务员')
material_index = HEADERS.index('耗材')
nowrootpath = './src/pandas/'
inxlsname = nowrootpath + '1.xls'
outxlsname = nowrootpath + '2020年1月 业务.xls'
outsheetname = '2020年1月 业务'

nameset = []
nameset.append('')

namebukets = [[] for _ in range(len(MATERIAL_KEYWORDS)) ]
nameprices = [0] * len(MATERIAL_KEYWORDS)

namebuketsarr = []
namepricesarr = []

namebuketsarr.append(deepcopy(namebukets))
namepricesarr.append(deepcopy(nameprices))

if __name__ == "__main__":
    df = pd.read_excel(inxlsname)
    for data in df.ix[:].values:
        if data[0] == '合计':
            continue
        name = data[name_index]
        material = data[material_index]
        price = data[price_index]
        if type(name) is not float:
            if name not in nameset:
                nameset.append(name)
                namebuketsarr.append(deepcopy(namebukets))
                namepricesarr.append(deepcopy(nameprices))
            nameix = nameset.index(name)     
        else:
            nameix = 0
        if type(material) is float:
            namebuketsarr[nameix][-1].append(data)
            if math.isnan(price) == False:
                namepricesarr[nameix][-1] += price
                continue
        isin = False
        for i, m in enumerate(MATERIAL_KEYWORDS):
            if type(material) != float and m in material:
                isin = True
                namebuketsarr[nameix][i].append(data)
                if math.isnan(price) == False:
                    namepricesarr[nameix][i] += price
                    break
        if isin == False:
            namebuketsarr[nameix][-1].append(data)
            if math.isnan(price) == False:
                namepricesarr[nameix][-1] += price

    totalprice = 0
    i = 0
    for n, namebuket in enumerate(namebuketsarr):
        for k, b in enumerate(namebuket):
            if len(b) == 0:
                continue
            for v in b:
                df.loc[i] = v
                i += 1
            itemstr = [''] * len(HEADERS)
            itemstr[0] = nameset[n] + MATERIAL_KEYWORDS[k] + '合计'
            nameprice = namepricesarr[n]
            itemstr[price_index] =  nameprice[k]
            df.loc[i] = itemstr
            i += 1
        itemstr = [''] * len(HEADERS)
        itemstr[0] = nameset[n] + '合计'
        nameprice = namepricesarr[n]
        itemstr[price_index] = sum(nameprice)
        totalprice += itemstr[price_index]
        df.loc[i] = itemstr
        i += 1
    
    itemstr = [''] * len(HEADERS)
    itemstr[0] = '所有合计'
    itemstr[price_index] = totalprice
    df.loc[i] = itemstr
    i += 1

    df.to_excel(outxlsname, sheet_name=outsheetname, index=False, header=True)
