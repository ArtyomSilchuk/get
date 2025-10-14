import r2r_dac as r2r
import signal_generator as sg

A = 3
dynamic_range = 3.152
signal_frequency = 1
sampling_frequency = 10
R2Rpins = [16, 20, 21, 25, 26, 17, 27, 22]

try:
    dac = r2r.R2R_DAC(R2Rpins, dynamic_range, True)
    t = 0
    
    while True:
        voltage = A*sg.get_triangle_value(signal_frequency, t)
        dac.set_voltage(voltage)
        t += (1 / sampling_frequency)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()