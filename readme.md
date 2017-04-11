# 说明
## 运行环境
环境 ： linux/mac
语言 ：python
版本 : 3.4

## Usage
1. 克隆代码，到你指定位置，进入
2. 生成城市代码
```
python3 parse_station.py > stations.py
```
然后，给stations.py 里面的dict给予变量名称 stations

3. 运行帮助命令，可以知道简单的基本用法
```
python3 ticket.py -h
```
```
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
    tickets 北京 上海 2017-04-12
    tickets -dg 成都 南京 2017-4-12
```



