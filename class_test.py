#%%
class Planet:
    pass
solar_system = []
for i in range(8):
    planet = Planet()
    solar_system.append(planet)
print(solar_system)

# %%
class Planet:
    def __init__(self,name):
        self.name = name 
    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
            
earth = Planet("Earth")
print(earth.name)
print(earth)
# %%

# %%
solar_system = []
planet_names = [
    "Mercury","Venus","Ears","Mars","Jupyter","Saturn","Uranus","Nemtune"
]
for name in planet_names:
    planet.name = name
    solar_system.append(planet) 
print(solar_system)
# %%
