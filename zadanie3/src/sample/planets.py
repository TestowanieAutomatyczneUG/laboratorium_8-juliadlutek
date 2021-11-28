
class Planets:
    def func(self, age, planet):
        earth_year = 31557600
        if (type(age) != int) or (type(planet) != str):
            raise Exception("Niepoprawne typy zmiennych")
        elif age < 0:
            raise Exception("Wiek musi być liczbą dodatnią!")
        else:
            if planet == "Ziemia":
                return format(age / earth_year, '.2f')
            elif planet == "Merkury":
                return format(age / (earth_year * 0.2408467), '.2f')
            elif planet == "Wenus":
                return format(age / (earth_year * 0.61519726), '.2f')
            elif planet == "Mars":
                return format(age / (earth_year * 1.8808158), '.2f')
            elif planet == "Jowisz":
                return format(age / (earth_year * 11.862615), '.2f')
            elif planet == "Saturn":
                return format(age / (earth_year * 29.447498), '.2f')
            elif planet == "Uran":
                return format(age / (earth_year * 84.016846), '.2f')
            elif planet == "Neptun":
                return format(age / (earth_year * 164.79132), '.2f')
            else:
                raise Exception("Niepoprawna nazwa planety")