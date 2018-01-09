from __future__ import print_function
import socket
from structs import UDPPacket
import ctypes


def on_packet(packet):
    print(int(packet.gear) - 1)


def get_packet(port, address):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((address, port))
    data, addr = sock.recvfrom(ctypes.sizeof(UDPPacket))
    return UDPPacket.from_buffer_copy(data)


def get_telemetry(address, port, callback=on_packet):
    last_packet = None
    while True:
        packet = get_packet(port, address)
        if last_packet is None or packet.time > last_packet.time:
            callback(packet)
            last_packet = packet


get_telemetry('192.168.1.150', 20777)
