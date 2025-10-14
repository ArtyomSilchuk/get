import time
import numpy as np

def get_sin_value(freq, t):
    return ( 0.5 + 0.5*np.sin(2*np.pi*freq*t) )

def get_triangle_value(freq, t):
    value = 2 * ((freq*t)%1)
    if value>1:
        value = 2-value
    return value

def wait_for_sampling_period(sampling_frequency):
    time.sleep( 1/sampling_frequency )