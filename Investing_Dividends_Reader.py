def __init__(dividends_data):
    """
    Investing Dividends Reader


    :param dividends_data:
    :return:
    """
    print("** Investing_Dividends_Reader.py **")
    import os
    import re

    content = dividends_data

    content = content.replace("\n", "").replace("\t", "").replace("  ", "").replace('\\"', '"').replace('"/', '"').replace('\\"', '"').replace("\\/", "").replace("/\\", "")
    # print(content)
    print("* 正在清洗数据中......")

    a_list = re.findall(r'<td class="flag">(.*?)<tr>', content)
    b_list = list()
    for item in a_list:
        company = re.findall('<span class="earnCalCompanyName middle">(.*?)</span>', item)[0]
        try:
            ex_dividend_date = re.findall(r'<td>([a-zA-z]+ \d+, \d+)</td>', item)[0]
        except IndexError:
            ex_dividend_date = "--"
        try:
            dividend = re.findall(r'<td>(-?\d+.\d+)?</td>', item)[0]
        except IndexError:
            dividend = "--"
        try:
            type_ = re.findall('<span class="icon(.*?)" title=', item)[0]
        except IndexError:
            type_ = "--"
        try:
            payment_date = re.findall(r'<td data-value="\d+">(.*?)</td>', item)[0]
        except IndexError:
            payment_date = "--"
        try:
            yield_ = re.findall(r'<td>(-?\d+.\d+?%)</td>', item)[0]
        except IndexError:
            yield_ = "--"
        b_list.append([company, ex_dividend_date, dividend, type_, payment_date, yield_])

    print("o 清洗数据完成。")
    print("oo Investing_Dividends_Reader.py oo")
    return b_list


