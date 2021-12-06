"""unifi proxy"""
import socket
from pathlib import Path
import json
import sys

GROUP = '233.89.188.1'
PORT = 10001
REQUEST = bytes([1, 0, 0, 0])

def log(*objects, sep=' ', end='\n', file=sys.stdout, flush=True):
    print(*objects, sep=sep, end=end, file=file, flush=flush)


def main(group, port):
    """main function"""

    # FIXME: reading packet.json
    packet_path = Path('packet.json')
    if packet_path.exists():
        packet = bytes(json.loads(packet_path.read_text())['data'])
    else:
        log(f"file '{packet_path} is missing, please create it. exiting...")
        return 1

    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
        try:
            s.bind(("", port))
            mreq = socket.inet_aton(group) + socket.inet_aton('0.0.0.0')
            s.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
        except socket.error as exc:
            log(f"Error binding to 0.0.0.0:{port}: {exc}")
            return 2
        else:
            log(f"Listening on 0.0.0.0:{port}")
        while True:
            data, (remote_ip, remote_port) = s.recvfrom(1024)
            if data != REQUEST:
                continue
            log(f"Received from {remote_ip}:{remote_port}...", end='')

            try:
                r = s.sendto(packet, (remote_ip, remote_port))
            except socket.error as exc:
                log(f"Exception: {exc}")
            else:
                log(f"successfully sent {r} bytes")


if __name__ == '__main__':
    sys.exit(main(GROUP, PORT))
