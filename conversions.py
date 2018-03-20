def convertCelciusToFahrenheit(celcius):

    fahrenheit = (float(celcius) * 9 / 5) + 32

    return '%.2f'%(fahrenheit)


def convertFahrenheitToCelcius(fahrenheit):

    celcius = (float(fahrenheit) - 32) * 5 / 9

    return '%.2f'%(celcius)


def convertCelciusToKelvin(celcius):

    kelvin = float(celcius) + 273.15

    return '%.2f'%(kelvin)


def convertKelvinToCelcius(kelvin):

    celcius = float(kelvin) - 273.15

    return '%.2f'%(celcius)


def convertDistance(mile=0, yard=0, meter=0):

    if mile != 0:
        yard = mile * 1760
        meter = mile * 1609

    elif yard != 0:
        mile = yard * .000569
        meter = yard * .9144

    elif meter != 0:
        mile = meter * .0006214
        yard = meter * 1.0936

    return (mile, yard, meter)

print convertDistance(mile=3)
print convertDistance(yard=1000)
print convertDistance(meter= 1000)
print convertCelciusToFahrenheit(100)
print convertFahrenheitToCelcius(190)
print convertCelciusToKelvin(100)
print convertKelvinToCelcius(380)

