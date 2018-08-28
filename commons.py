import re

pair_template = "{0}\t{1}"


def print_result(key, value):
    if key is not None:
        print pair_template.format(key, value)


def parse_log_entry(entry):
    return re.match("(?P<ip>.+?) (?P<id>.+?|-) (?P<username>.+?|-) \[(?P<datetime>.+?)\] "
             "\"(?P<request>.+?)\" (?P<status>\d+?) (?P<size>\d+?|-)", entry)
