def sinusoidal_PWM_frequency(clk, prescaler, arr, samples):
    """Calculates the frequency of the PWM generated Sine-wave
    
    Keyword argument:
    clk -- Clock frequency of the STM32
    prescaler -- prescaler for the timer frequency
    arr -- Autoreloadregister,  Counter period of the timer
    """
    return 0