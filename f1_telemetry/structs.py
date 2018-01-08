"""
UDP telemetry packet structures
"""
import ctypes

class CarUDPData(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for the car data portion of a F1 2017 UDP packet
    """
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


class UDPPacket(ctypes.LittleEndianStructure):
    """
    Ctypes data structure for a F1 2017 UDP packet
    """
    _pack_ = 1
    _fields_ = [
        ('time',                    ctypes.c_float),
        ('lapTime',                 ctypes.c_float),
        ('lapDistance',             ctypes.c_float),
        ('totalDistance',           ctypes.c_float),
        ('x',                       ctypes.c_float),     # World space position
        ('y',                       ctypes.c_float),     # World space position
        ('z',                       ctypes.c_float),     # World space position
        ('speed',                   ctypes.c_float),     # Speed of car in MPH
        ('xv',                      ctypes.c_float),     # Velocity in world space
        ('yv',                      ctypes.c_float),     # Velocity in world space
        ('zv',                      ctypes.c_float),     # Velocity in world space
        ('xr',                      ctypes.c_float),     # World space right direction
        ('yr',                      ctypes.c_float),     # World space right direction
        ('zr',                      ctypes.c_float),     # World space right direction
        ('xd',                      ctypes.c_float),     # World space forward direction
        ('yd',                      ctypes.c_float),     # World space forward direction
        ('zd',                      ctypes.c_float),     # World space forward direction
        ('susp_pos',                ctypes.c_float * 4), # Note: All wheel arrays have the order:
        ('susp_vel',                ctypes.c_float * 4), # RL, RR, FL, FR
        ('wheel_speed',             ctypes.c_float * 4),
        ('throttle',                ctypes.c_float),
        ('steer',                   ctypes.c_float),
        ('brake',                   ctypes.c_float),
        ('clutch',                  ctypes.c_float),
        ('gear',                    ctypes.c_float),
        ('g_force_lat',             ctypes.c_float),
        ('g_force_lon',             ctypes.c_float),
        ('lap',                     ctypes.c_float),
        ('engineRate',              ctypes.c_float),
        ('sli_pro_native_support',  ctypes.c_float),     # SLI Pro support
        ('car_position',            ctypes.c_float),     # car race position
        ('kers_level',              ctypes.c_float),     # kers energy left
        ('kers_max_level',          ctypes.c_float),     # kers maximum energy
        ('drs',                     ctypes.c_float),     # 0 = off, 1 = on
        ('traction_control',        ctypes.c_float),     # 0 (off) - 2 (high)
        ('anti_lock_brakes',        ctypes.c_float),     # 0 (off) - 1 (on)
        ('fuel_in_tank',            ctypes.c_float),     # current fuel mass
        ('fuel_capacity',           ctypes.c_float),     # fuel capacity
        ('in_pits',                 ctypes.c_float),     # 0 = none, 1 = pitting, 2 = in pit area
        ('sector',                  ctypes.c_float),     # 0 = sector1, 1 = sector2, 2 = sector3
        ('sector1_time',            ctypes.c_float),     # time of sector1 (or 0)
        ('sector2_time',            ctypes.c_float),     # time of sector2 (or 0)
        ('brakes_temp',             ctypes.c_float * 4), # brakes temperature (centigrade)
        ('tyres_pressure',          ctypes.c_float * 4), # tyres pressure PSI
        ('team_info',               ctypes.c_float),     # team ID 
        ('total_laps',              ctypes.c_float),     # total number of laps in this race
        ('track_size',              ctypes.c_float),     # track size meters
        ('last_lap_time',           ctypes.c_float),     # last lap time
        ('max_rpm',                 ctypes.c_float),     # cars max RPM, at which point the rev limiter will kick in
        ('idle_rpm',                ctypes.c_float),     # cars idle RPM
        ('max_gears',               ctypes.c_float),     # maximum number of gears
        ('sessionType',             ctypes.c_float),     # 0 = unknown, 1 = practice, 2 = qualifying, 3 = race
        ('drsAllowed',              ctypes.c_float),     # 0 = not allowed, 1 = allowed, -1 = invalid / unknown
        ('track_number',            ctypes.c_float),     # -1 for unknown, 0-21 for tracks
        ('vehicleFIAFlags',         ctypes.c_float),     #  -1 = invalid/unknown, 0 = none, 1 = green, 2 = blue, 3 = yellow, 4 = red
        ('era',                     ctypes.c_float),     # era, 2017 (modern) or 1980 (classic)
        ('engine_temperature',      ctypes.c_float),     # engine temperature (centigrade)
        ('gforce_vert',             ctypes.c_float),     # vertical g-force component
        ('ang_vel_x',               ctypes.c_float),     # angular velocity x-component
        ('ang_vel_y',               ctypes.c_float),     # angular velocity y-component
        ('ang_vel_z',               ctypes.c_float),     # angular velocity z-component
        ('tyres_temperature',       ctypes.c_byte * 4),  # tyres temperature (centigrade)
        ('tyres_wear',              ctypes.c_byte * 4),  # tyre wear percentage
        ('tyre_compound',           ctypes.c_byte),      # compound of tyre – 0 = ultra soft, 1 = super soft, 2 = soft, 3 = medium, 4 = hard, 5 = inter, 6 = wet
        ('front_brake_bias',        ctypes.c_byte),      # front brake bias (percentage)
        ('fuel_mix',                ctypes.c_byte),      # fuel mix - 0 = lean, 1 = standard, 2 = rich, 3 = max
        ('currentLapInvalid',       ctypes.c_byte),      # current lap invalid - 0 = valid, 1 = invalid
        ('tyres_damage',            ctypes.c_byte * 4),  # tyre damage (percentage)
        ('front_left_wing_damage',  ctypes.c_byte),      # front left wing damage (percentage)
        ('front_right_wing_damage', ctypes.c_byte),      # front right wing damage (percentage)
        ('rear_wing_damage',        ctypes.c_byte),      # rear wing damage (percentage)
        ('engine_damage',           ctypes.c_byte),      # engine damage (percentage)
        ('gear_box_damage',         ctypes.c_byte),      # gear box damage (percentage)
        ('exhaust_damage',          ctypes.c_byte),      # exhaust damage (percentage)
        ('pit_limiter_status',      ctypes.c_byte),      # pit limiter status – 0 = off, 1 = on
        ('pit_speed_limit',         ctypes.c_byte),      # pit speed limit in mph
        ('session_time_left',       ctypes.c_float),     # NEW: time left in session in seconds 
        ('rev_lights_percent',      ctypes.c_byte),      # NEW: rev lights indicator (percentage)
        ('is_spectating',           ctypes.c_byte),      # NEW: whether the player is spectating
        ('spectator_car_index',     ctypes.c_byte),      # NEW: index of the car being spectated

        # Car data
        ('num_cars',                ctypes.c_byte),      # number of cars in data
        ('player_car_index',        ctypes.c_byte),      # index of player's car in the array
        ('car_data',                CarUDPData * 20),    # data for all cars on track

        ('yaw',                    ctypes.c_float),      # NEW (v1.8)
        ('pitch',                  ctypes.c_float),      # NEW (v1.8)
        ('roll',                   ctypes.c_float),      # NEW (v1.8)
        ('x_local_velocity',       ctypes.c_float),      # NEW (v1.8) Velocity in local space
        ('y_local_velocity',       ctypes.c_float),      # NEW (v1.8) Velocity in local space
        ('z_local_velocity',       ctypes.c_float),      # NEW (v1.8) Velocity in local space
        ('susp_acceleration',      ctypes.c_float * 4),  # NEW (v1.8) RL, RR, FL, FR
        ('ang_acc_x',              ctypes.c_float),      # NEW (v1.8) angular acceleration x-component
        ('ang_acc_y',              ctypes.c_float),      # NEW (v1.8) angular acceleration y-component
        ('ang_acc_z',              ctypes.c_float),      # NEW (v1.8) angular acceleration z-component
    ]

assert ctypes.sizeof(UDPPacket) == 1289
