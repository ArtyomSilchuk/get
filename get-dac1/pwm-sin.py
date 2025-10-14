import pwm_dac
import signal_generator

A = 1
dynamic_range = 3.133
signal_frequency = 1
sampling_frequency = 1000

try:
    dac = pwm_dac.PWM_DAC(12, 500, dynamic_range, True)
    t = 0

    while True:
        voltage = A*signal_generator.get_sin_value(signal_frequency, t)
        dac.set_voltage(voltage)
        t += (1 / sampling_frequency)
        signal_generator.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()