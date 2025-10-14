import mcp4725_driver
import signal_generator as sg

A = 3
dynamic_range = 5.15
signal_frequency = 1
sampling_frequency = 1000

try:
    dac = mcp4725_driver.MCP4725(dynamic_range)
    t = 0

    while True:
        voltage = A*sg.get_triangle_value(signal_frequency, t)
        dac.set_voltage(voltage)
        t += (1 / sampling_frequency)
        sg.wait_for_sampling_period(sampling_frequency)

finally:
    dac.deinit()