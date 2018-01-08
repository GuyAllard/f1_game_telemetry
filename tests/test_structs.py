import ctypes

from .context import UDPPacket

def test_struct_size():
    assert ctypes.sizeof(UDPPacket) == 1289
