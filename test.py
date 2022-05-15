from sine_frequency_calculator import sinusoidal_PWM_frequency
from adc_calc import adc_frequency_calc

def test():
    assert sinusoidal_PWM_frequency(0,1,1,1) == 0
    assert adc_frequency_calc(0,1) == 0
    
    
    

