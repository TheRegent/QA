import subprocess
import paramiko
import pytest

username = "fedir-server"
password = "1234"
server_ip = "10.0.2.15"


@pytest.fixture(scope='function')
def server():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(server_ip, username=username, password=password)

    # Start the iperf server in UDP mode
    stdin, stdout, stderr = client.exec_command('iperf -s -u -D')
    yield stdout.read() + stderr.read()

    client.exec_command('pkill iperf')
    client.close()

@pytest.fixture(scope='function')
def client(server):
    subprocess.run(['sleep', '5'])
    proc = subprocess.run(['iperf', '-c', server_ip, '-u'], capture_output=True, text=True)
    yield proc.stdout