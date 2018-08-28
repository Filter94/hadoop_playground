import re

pair_template = "{0}\t{1}"


def print_result(key, value):
    if key is not None:
        print pair_template.format(key, value)


def parse_file_path(line):
    request_start_idx = line.find('"') + 1
    file_path_start_idx = line.find(" ", request_start_idx) + 1
    file_path_end_idx = line.find(" ", file_path_start_idx)
    return line[file_path_start_idx: file_path_end_idx]

# inefficient
# def parse_log_entry(entry):
#     return re.match("(?P<ip>.+?) (?P<id>.+?|-) (?P<username>.+?|-) \[(?P<datetime>.+?)\] "
#              "\"(?P<request>.+?)\" (?P<status>\d+?) (?P<size>\d+?|-)", entry)
