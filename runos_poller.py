import sys
import requests
from time import sleep
from datetime import datetime
from argparse import ArgumentParser
import psutil

process_name = "runos"
pid_runos = None

for proc in psutil.process_iter():
    if process_name in proc.name():
        pid_runos = proc.pid
sleep(0.5)
process = psutil.Process(pid_runos)


def make_parser():
    parser = ArgumentParser(
        prog='./runos_poller.py',
        description='Сбор данных с контроллера и перенаправление разбираемых данных на стандартный поток выхода sdtout',

    )
    parser.add_argument(
        '--ip', type=str, default='127.0.0.1',
        help='Runos address'
    )
    parser.add_argument(
        '--port', '-p', type=int, default=8000,
        help='Runos REST port'
    )
    parser.add_argument(
        '--interval', '-i', type=int, default=30,
        help='Interval in seconds'
    )
    return parser


class Poller(object):
    def __init__(self, ip, port, interval):
        self.ctrl_ip = ip
        self.ctrl_port = port
        self.interval = interval

    def poll(self):
        while True:
            time = self.get_time()
            response = self.request_stats()
            data = self.json_to_csv(time, response)
            print(data)
            sleep(self.interval)

    def request_stats(self):
        req = requests.get(
            'http://{}:{}/switches/controlstats/'.format(self.ctrl_ip, self.ctrl_port))
        if req.status_code != 200:
            return None

        return req.json()

    @staticmethod
    def json_to_csv(time, data):
        if data is None:
            return '{}'.format(time)
        switches = data['control_stats']
        if switches is None:
            return '{}'.format(time)

        csv_str = ''
        sum_pi = 0
        for switch in switches:
            rx = switch['rx_ofpackets']
            tx = switch['tx_ofpackets']
            pi = switch['pkt_in_ofpackets']
            sum_pi += int(pi)
        csv_str += ',{},{}%,{:.1f}%'.format(sum_pi,process.cpu_percent(interval=None),process.memory_percent())
        return '{}{}'.format(time, csv_str)

    @staticmethod
    def get_time():
        return datetime.now().isoformat()


def start():
    parser = make_parser()
    opts = parser.parse_args(sys.argv[1:])
    poller = Poller(opts.ip, opts.port, opts.interval)
    poller.poll()


if __name__ == "__main__":
    start()