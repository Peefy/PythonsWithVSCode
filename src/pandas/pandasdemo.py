
import math
from copy import deepcopy

import pandas as pd
from pandas import DataFrame

# MATERIAL_KEYWORDS = ['写真', '喷绘', '背胶', '相纸', '反光', '字', '条幅', '旗', '平板打印', '雕刻', '车贴','其它']
MATERIAL_KEYWORDS = ['写真背胶', '户外写真车贴','户外写真', '写真相纸', '裁切费', '反光膜', '绢丝布', '刀旗旗面', '写真布', 'UV软膜']
MATERIAL_KEYWORDS += ['喷绘车贴', '喷绘', '条幅']
MATERIAL_KEYWORDS += ['普通名片', '即时贴刻字镂空', '157克铜板纸单面彩印', '非标5毫米乳白色亚克力', '即时贴','设计','改图','磨砂黑板皮+铝板+不锈钢防尘罩', \
    '0.84单面PVC','A4胸卡（普通纸）正反面','丝网印衣服','300克铜版纸+卡套','pvc打印', \
        'PVC打印','即使贴红字白边','铁板刻字','5mmPVC刻板','铁板刻镂空字','木托奖牌','250g双面印塑封', '其他']
HEADERS = ['订单编号', '客户名称', '业务员','设计员', '付款状态', '项目名称', '耗材','制作内容',	'规格', '数量', '单位',	'面积',	'单价',	'金额', '备注']
price_index = HEADERS.index('金额')
name_index = HEADERS.index('设计员')
material_index = HEADERS.index('耗材')
nowrootpath = './src/pandas/'
inxlsname = nowrootpath + '4.xls'
outxlsname = nowrootpath + '2020年4月业务.xls'
outsheetname = '2020年4月业务'
lastline0item = '合计'

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
        if data[0] == lastline0item:
            continue
        name = data[name_index]
        material = data[material_index]
        price = data[price_index]
        if type(name) is not float and name != '':
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
            itemstr[price_index] = nameprice[k]
            df.loc[i] = itemstr
            i += 1
        itemstr = [''] * len(HEADERS)
        itemstr[0] = nameset[n] + '所有合计'
        nameprice = namepricesarr[n]
        itemstr[price_index] = sum(nameprice)
        totalprice += itemstr[price_index]
        if itemstr[price_index] != 0:
            df.loc[i] = itemstr
            i += 1
    
    itemstr = [''] * len(HEADERS)
    itemstr[0] = '所有合计'
    itemstr[price_index] = totalprice
    df.loc[i] = itemstr
    i += 1

    df.to_excel(outxlsname, sheet_name=outsheetname, index=False, header=True)
