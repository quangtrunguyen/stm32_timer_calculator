def adc_frequency_calc(clk,prescaler):
    """Calculates the conversion frequency of ADC
    
    Keyword argument:
    clk -- Clock frequency of the STM32
    prescaler -- prescaler for the ADC frequency
    """

    if clk <= 0 or prescaler <=0:
        return 0
    else:
        return (clk/prescaler)
