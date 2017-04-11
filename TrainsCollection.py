from prettytable import PrettyTable
from colorama import init, Fore
init()
class TrainsCollection:
    header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()

    def __init__(self, available_trains, options):
        """查询到的火车班次集合k
        :param available_trains: 一个列表, 包含可获得的火车班次, 每个
                                 火车班次是一个字典
        :param options: 查询的选项, 如高铁, 动车, etc...
        """
        self.available_trains = available_trains
        self.options = options

    def _get_duration(self, raw_train):
        duration = raw_train.get('lishi').replace(':', '小时') + '分'
        if duration.startswith('00'):
            return duration[4:]
        if duration.startswith('0'):
            return duration[1:]
        return duration

    @property
    def trains(self):
        header = '车次 车站 时间 历时 一等 二等 软卧 硬卧 硬座 无座'.split()
        for raw_train in self.available_trains:
            listInfo = raw_train['queryLeftNewDTO']

            train_no = listInfo['station_train_code']
            initial = train_no[0].lower()
            if not self.options or initial in self.options:
                train = [
                    train_no,  # 车次
                    '\n'.join([Fore.GREEN + listInfo['from_station_name'] + Fore.RESET,
                               Fore.RED + listInfo['to_station_name'] + Fore.RESET]),    # 车站
                    '\n'.join([Fore.GREEN + listInfo['start_time'] + Fore.RESET,  # 时间
                               Fore.RED + listInfo['arrive_time'] + Fore.RESET]),
                    self._get_duration(listInfo),    # 历时
                    listInfo['zy_num'],     # 一等
                    listInfo['ze_num'],     # 二等
                    listInfo['rw_num'],     # 软卧
                    listInfo['yw_num'],     # 硬卧
                    listInfo['yz_num'],     # 硬座
                    listInfo['wz_num'],     #无座
                ]
                yield train

    def pretty_print(self):
        pt = PrettyTable()
        pt._set_field_names(self.header)
        for train in self.trains:
            pt.add_row(train)
        print(pt)
