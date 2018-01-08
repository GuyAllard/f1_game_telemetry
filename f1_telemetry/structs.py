# coding: utf-8
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

# lookups for tracks, teams and drivers
Tracks = {
    0:  'Melbourne',
    1:  'Sepang',
    2:  'Shanghai',
    3:  'Sakhir (Bahrain)',
    4:  'Catalunya',
    5:  'Monaco',
    6:  'Montreal',
    7:  'Silverstone',
    8:  'Hockenheim',
    9:  'Hungaroring',
    10: 'Spa',
    11: 'Monza',
    12: 'Singapore',
    13: 'Suzuka',
    14: 'Abu Dhabi',
    15: 'Texas',
    16: 'Brazil',
    17: 'Austria',
    18: 'Sochi',
    19: 'Mexico',
    20: 'Baku (Azerbaijan)',
    21: 'Sakhir Short',
    22: 'Silverstone Short',
    23: 'Texas Short',
    24: 'Suzuka Short'
}

Teams = {
    4:  'Mercedes',
    0:  'Redbull',
    1:  'Ferrari',
    6:  'Force India',
    7:  'Williams',
    2:  'McLaren',
    8:  'Toro Rosso',
    11: 'Haas',
    3:  'Renault',
    5:  'Sauber',
}

ClassicTeams = {
    0:  'Williams 1992',
    1:  'McLaren 1988',
    2:  'McLaren 2008',
    3:  'Ferrari 2004',
    4:  'Ferrari 1995',
    5:  'Ferrari 2007',
    6:  'McLaren 1998',
    7:  'Williams 1996',
    8:  'Renault 2006',
    10: 'Ferrari 2002',
    11: 'Redbull 2010',
    12: 'McLaren 1991'
}

Drivers = {
    9:  'Lewis Hamilton',
    15: 'Valtteri Bottas',
    16: 'Daniel Ricciardo',
    22: 'Max Verstappen',
    0:  'Sebastian Vettel',
    6:  'Kimi Räikkönen',
    5:  'Sergio Perez',
    33: 'Esteban Ocon',
    3:  'Felipe Massa',
    35: 'Lance Stroll',
    2:  'Fernando Alonso',
    34: 'Stoffel Vandoorne',
    23: 'Carlos Sainz Jr.',
    1:  'Daniil Kvyat',
    7:  'Romain Grosjean',
    14: 'Kevin Magnussen',
    10: 'Nico Hulkenberg',
    20: 'Jolyon Palmer',
    18: 'Marcus Ericsson',
    31: 'Pascal Wehrlein'
}

ClassicDrivers = {
    23: 'Arron Barnes',
    1:  'Martin Giles',
    16: 'Alex Murray',
    68: 'Lucas Roth',
    2:  'Igor Correia',
    3:  'Sophie Levasseur',
    24: 'Jonas Schiffer',
    4:  'Alain Forest',
    20: 'Jay Letourneau',
    6:  'Esto Saari',
    9:  'Yasar Atiyeh',
    18: 'Callisto Calabresi',
    22: 'Naota Izum',
    10: 'Howard Clarke',
    8:  'Lars Kaufmann',
    14: 'Marie Laursen',
    31: 'Flavio Nieves',
    7:  'Peter Belousov',
    0:  'Klimek Michalski',
    5:  'Santiago Moreno',
    15: 'Benjamin Coppens',
    32: 'Noah Visser',
    33: 'Gert Waldmuller',
    34: 'Julian Quesada'
}
