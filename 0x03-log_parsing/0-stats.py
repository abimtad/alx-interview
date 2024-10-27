#!/usr/bin/python3
import sys
import signal

total_file_size = 0
status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
line_count = 0

def print_stats():
    """ Prints the accumulated metrics. """
    print(f"File size: {total_file_size}")
    for code in sorted(status_codes.keys()):
        if status_codes[code] > 0:
            print(f"{code}: {status_codes[code]}")

def process_line(line):
    """ Processes each line to update the file size and status code count. """
    global total_file_size
    parts = line.split()
    try:
        if len(parts) < 7:
            return
        ip, dash, timestamp, method, path, protocol, status_code, file_size = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5], parts[6], parts[7]
        if method != '"GET' or protocol != 'HTTP/1.1"':
            return
        total_file_size += int(file_size)
        if status_code in status_codes:
            status_codes[status_code] += 1
    except Exception:
        pass

def signal_handler(sig, frame):
    """ Signal handler for keyboard interruption (CTRL + C). """
    print_stats()
    sys.exit(0)

# Register the signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

# Read lines from stdin
for line in sys.stdin:
    process_line(line.strip())
    line_count += 1
    if line_count % 10 == 0:
        print_stats()
