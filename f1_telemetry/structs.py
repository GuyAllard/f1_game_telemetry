"""
UDP telemetry packet structures
"""
import ctypes

class CarUDPData(ctypes.LittleEndianStructure):
    _pack_ = 1
    _fields_ = [
        ('worldPosition',     ctypes.c_float * 3), # world co-ordinates of vehicle
        ('lastLapTime',       ctypes.c_float),
        ('currentLapTime',    ctypes.c_float),
        ('bestLapTime',       ctypes.c_float),
        ('sector1Time',       ctypes.c_float),
        ('sector2Time',       ctypes.c_float),
        ('lapDistance',       ctypes.c_float),
        ('driverId',          ctypes.c_byte),
        ('teamId',            ctypes.c_byte),
        ('carPosition',       ctypes.c_byte),      # UPDATED: track positions of vehicle
        ('currentLapNum',     ctypes.c_byte),
        ('tyreCompound',      ctypes.c_byte),      # compound of tyre – 0 = ultra soft, 1 = super soft, 2 = soft, 3 = medium, 4 = hard, 5 = inter, 6 = wet
        ('inPits',            ctypes.c_byte),      # 0 = none, 1 = pitting, 2 = in pit area
        ('sector',            ctypes.c_byte),      # 0 = sector1, 1 = sector2, 2 = sector3
        ('currentLapInvalid', ctypes.c_byte),      # current lap invalid - 0 = valid, 1 = invalid
        ('penalties',         ctypes.c_byte),      # NEW: accumulated time penalties in seconds to be added
    ]
