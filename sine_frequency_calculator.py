def sinusoidal_PWM_frequency(clk, prescaler, arr, samples):
    """Calculates the frequency of the PWM generated Sine-wave
    
    Keyword argument:
    clk -- Clock frequency of the STM32
    prescaler -- prescaler for the timer frequency
    arr -- Autoreloadregister,  Counter period of the timer max.65535
    """

    if arr <= 0 or clk <= 0 or prescaler <=0 or samples <= 0:
        return 0
    else:
        return (clk/prescaler)/(arr*samples)
