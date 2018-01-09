from __future__ import print_function
import socket
from structs import UDPPacket
import ctypes


def get_packet(address, port):
    """
    Recieve a single UDP telemetry packet from the specified port and ip address
    
    :param address: IP address for the socket
    :param port: Port for the socket
    :return: A UDPPacket
    """
    # create a socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # bind the socket to the specified ip address and port
    sock.bind((address, port))
    # recieve data
    data, addr = sock.recvfrom(ctypes.sizeof(UDPPacket))
    # convert from raw bytes to UDPPacket structure
    return UDPPacket.from_buffer_copy(data)


def get_telemetry(address, port):
    """
    Generator function which yields UDPPackets from the specified ip address and port
    
    :param address: IP address for receiving packets
    :param port: Port on which to receive packets
    :yeild: a UDPPacket for each udp packet received
    """
    last_packet = None
    while True:
        packet = get_packet(address, port)
        if last_packet is None or packet.time > last_packet.time:
            yield packet
            last_packet = packet


for packet in get_telemetry('192.168.1.150', 20777):
    print(int(packet.gear) - 1)
