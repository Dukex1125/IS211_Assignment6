import unittest
import conversions

class knownConversios(unittest.TestCase):
    knownFahrenheitConversions = ((0, 32), (10, 50), (25, 77), (50, 122), (75, 167), (100, 212))
    knownKelvinConversions = ((10, 283.15), (35, 308.15), (50, 323.15), (75, 348.15), (100, 373.15))
    distanceMileYardMeter = ((3, 5280, 4827), (4, 7040, 6436), (1, 1760, 1609),
                             (2, 3520, 3218), (5, 8800, 8045))

    def testDistanceConversion(self):
        """convertDistance should yield proper conversions displayed on distanceMileYardMeter list."""
        for mile, yard, meter in self.distanceMileYardMeter:
            miles, yards, meters = (conversions.convertDistance(mile))
            self.assertEqual((mile, yard, meter), (miles, yards, meters))

    def testConvertCelciusToFahrenheit(self):
        """convertToFahrenheit should give known results"""
        for celcius, fahrenheit in self.knownFahrenheitConversions:
            result = float(conversions.convertCelciusToFahrenheit(celcius))
            self.assertEqual(fahrenheit, result)

    def testConvertCelciusToKelvin(self):
        """convertToKelvin should give known results."""
        for celcius, kelvin in self.knownKelvinConversions:
            result = float(conversions.convertCelciusToKelvin(celcius))
            self.assertEqual(kelvin, result)

    def testConvertKelvinToCelcius(self):
        """convertKelvinToCelcius should give knownKelvinConversion results"""
        for celcius, kelvin in self.knownKelvinConversions:
            result = float(conversions.convertKelvinToCelcius(kelvin))
            self.assertEqual(celcius, result)

    def testConvertFahrenheittoCelcius(self):
        """convertFahrenheitToCelcius should give knownFahrenheitConversion results"""
        for celcius, fahrenheit in self.knownFahrenheitConversions:
            result = float(conversions.convertFahrenheitToCelcius(fahrenheit))
            self.assertEqual(celcius, result)

if __name__ == '__main__':
    unittest.main()