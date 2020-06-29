import matplotlib.pyplot as plt
plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import random
import datetime

from urllib.request import urlopen
from xml.etree import ElementTree as ET

def get_currencies(currencies_ids_lst=['R01010', 'R01020A', 'R01035', 'R01060',
'R01090B', 'R01100', 'R01115', 'R01239', 'R01235', 'R01135']):

    cur_res_str = urlopen("http://www.cbr.ru/scripts/XML_daily.asp")

    result = {}

    cur_res_xml = ET.parse(cur_res_str)

    root = cur_res_xml.getroot()
    valutes = root.findall('Valute')
    for el in valutes:
        valute_id = el.get('ID')

        if str(valute_id) in currencies_ids_lst:
            valute_cur_val = el.find('Value').text
            result[valute_id] = valute_cur_val

    return result

def dec_to_base(N, base):
    if not hasattr(dec_to_base, 'table'):
        dec_to_base.table = '0123456789ABCDEF'
    x, y = divmod(N, base)
    return dec_to_base(x, base) + dec_to_base.table[y] if x else dec_to_base.table[y]

date = str(datetime.date.today())

dollar_data = ET.parse(urlopen('http://www.cbr.ru/scripts/XML_dynamic.asp?date_req1=01/11/2019&date_req2=12/11/2019&VAL_NM_RQ=R01235')).getroot().findall('Record')

dollar_curse = []
dollar_dates = []
for el in dollar_data:
    dollar_curse.append(float(el.find('Value').text.replace(',', '.')))
    dollar_dates.append(el.attrib['Date'][0:5])

cur_vals = get_currencies()
objects = cur_vals.keys()
y_pos = np.arange(len(objects))

performance = [float(x.replace(',','.')) for x in cur_vals.values()]


ind = np.arange(len(performance))

colors = []

for el in cur_vals:
    num = dec_to_base(random.randint(0, 16777215), 16).zfill(6)
    colors.append('#' + num)

plt.subplot(1, 2, 1)
plt.bar(y_pos, performance, color=colors)
# plt.xticks(y_pos, objects)
plt.ylabel('Курс')
plt.xlabel('Валюта')
plt.xticks(ind, (
'BRL', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL', 'EUR', 'USD', 'KZT'))
plt.title('Курсы валют ЦБ РФ к рублю на ' + date)

plt.subplot(1, 2, 2)
plt.plot(dollar_dates, dollar_curse)
plt.ylabel('Курс')
plt.xlabel('Валюта')
plt.title('Курс доллара ЦБ РФ к рублю. Ноябрь, 2019 год')

plt.show()
