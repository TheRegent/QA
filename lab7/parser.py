import re

def parse_iperf_output(output):
    match = re.search(r'(\d+\.\d+) Mbits/sec', output)
    return float(match.group(1)) if match else 0
