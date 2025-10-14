import pwm_dac as pwm
import signal_generator as sg

A = 1
dynamic_range = 3.133
signal_frequency = 1
sampling_frequency = 1000

try:
    dac = pwm.PWM_DAC(12, 500, dynamic_range, True)
    t = 0

    while True:
        voltage = A*sg.get_triangle_value(signal_frequency, t)
        dac.set_voltage(voltage)
        t += (1 / sampling_frequency)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()