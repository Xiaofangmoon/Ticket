# coding: utf-8

"""命令行火车票查看器

Usage:
    tickets [-gdtkz] <from> <to> <date>

Options:
    -h,--help   显示帮助菜单
    -g          高铁
    -d          动车
    -t          特快
    -k          快速
    -z          直达
    -f,--fileout  查询结果输出到文件
    

Example:
    tickets 北京 上海 2016-10-10
    tickets -dg 成都 南京 2016-10-10
"""
from docopt import docopt

from stations import stations
import requests
from TrainsCollection import TrainsCollection
import json

from requests.packages.urllib3.exceptions import InsecureRequestWarning

# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def cli():
    """command-line interface"""
    arguments = docopt(__doc__)
    options = ''.join([
        key for key, value in arguments.items() if value is True
    ])
    result = getSearchData(arguments)
    available_trains = result['data']
    TrainsCollection(available_trains, options).pretty_print()


# 获取数据
def getData(url, method='get', **data):
    result = None
    if method == 'get':
        result = requests.get(url, params=data, verify=False)
    elif method == 'post':
        result = requests.post(url, params=data, verify=False)
    else:
        result = requests.get(url, params=data, verify=False)
    return result.text


def getSearchDataByType(url, paramData, type='json'):
    returnContent = getData(url, data=paramData)
    if type == 'json':
        return json.loads(returnContent)
    else:
        return json.loads(returnContent)


# 获取查询结果
# 返回结果 : dict

def getSearchData(arguments):
    date = arguments['<date>']
    from_station = stations.get(arguments['<from>'])
    to_station = stations.get(arguments['<to>'])
    url = 'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date={}&leftTicketDTO.from_station={}&leftTicketDTO.to_station={}&purpose_codes=ADULT'.format(
        date, from_station, to_station)
    paramData = {}
    resultData = getSearchDataByType(url, paramData, type='json')
    return resultData


if __name__ == '__main__':
    cli()
