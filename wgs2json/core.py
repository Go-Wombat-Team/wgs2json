import re
import json
import pprint

from wgs2json.utils import DataclassJSONEncoder
from wgs2json.models import WgPeer, WgInterface


class WireGuard:
    def __init__(self, stdin, args):
        self.interface_regex = r'((?:[^\n][\n]?)+)'
        self.parameter_regex = r'(^.+): (.+$)'
        self.stdin = stdin
        self.is_pretty = True if '--pretty' in args else False

    def __call__(self):
        output = []
        for i in map(self.make_json, self.all_interfaces()):
            if 'interface' in i:
                interface = WgInterface(peers=[], **i)
                output.append(interface)
            else:
                interface.peers.append(WgPeer(**i))

        output = json.dumps(output, cls=DataclassJSONEncoder)  # mostly for validation purposes

        if self.is_pretty:
            self.pretty_print(output)
        else:
            print(output)

        return(output)

    @staticmethod
    def pretty_print(output):
        output = json.loads(output)
        pp = pprint.PrettyPrinter(indent=2)
        pp.pprint(output)

    def all_interfaces(self):
        interfaces = re.findall(self.interface_regex, self.stdin, re.MULTILINE)
        if interfaces:
            return interfaces
        else:
            raise ValueError('There are no interfaces')

    def format_value(self, key, value):
        key = self.format_key(key)
        array_format = ['allowed_ips']

        if key in array_format:
            value = value.split(', ')

        return value

    @staticmethod
    def format_key(key):
        return key.replace('  ', '').replace(' ', '_')

    def make_json(self, s):
        confing = re.findall(self.parameter_regex, s, re.MULTILINE)
        return {self.format_key(key): self.format_value(key, value) for key, value in confing}
