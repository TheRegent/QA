import pytest
from parser import parse_iperf_output

class TestIperf:
    def test_iperf_bandwidth(self, client):
        print("Client Output:", client)
        bandwidth = parse_iperf_output(client)
        assert bandwidth > 1, "Bandwidth below 1 Mbps threshold"
