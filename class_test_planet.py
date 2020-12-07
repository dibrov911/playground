class Planet:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name
solar_system = []
planet_names = [
    "Mercury","Venus","Ears","Mars","Jupyter","Saturn","Uranus","Neptune"
]
for name in planet_names:
    planet = Planet(name)
    planet.name = name
    solar_system.append(planet) 
print(solar_system)