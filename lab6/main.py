import subprocess
import re

# Вкажіть IP-адресу вашого iperf сервера тут
server_ip = '10.0.2.15'

def client(server_ip):
    try:
        # Виконання команди iperf3
        process = subprocess.Popen(["iperf", "-c", server_ip, "-u"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()
        return output.decode(), error.decode()
    except Exception as e:
        return None, str(e)

def parser(output):
    results = []
    # Регулярний вираз для знаходження інтервалів
    regex = r"\[\s*\d+]\s+(\d+\.\d+-\d+\.\d+)\s+sec\s+(\d+\.\d+ MBytes)\s+(\d+\.\d+ Mbits/sec)"
    matches = re.finditer(regex, output, re.MULTILINE)

    for matchNum, match in enumerate(matches, start=1):
        interval, transfer, bitrate = match.groups()
        # Конвертування значень у зручний формат
        transfer_value = float(transfer.split()[0])
        bitrate_value = float(bitrate.split()[0])
        results.append({'Interval': interval, 'Transfer': transfer_value, 'Bitrate': bitrate_value})

    return results

# Використання функцій
result, error = client(server_ip)

if error:
    print(error)
else:
    result_list = parser(result)
    for value in result_list:
            print(value)
    print("Test was completed successful!")