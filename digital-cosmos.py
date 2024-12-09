# Task 1: Set up a Python Virtual Environment and Install Required Packages
import requests

# Task 2: Fetch Data from a Space API
# Defining a function to fetch planet data from API and print the extracted information
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planet_data = response.json()

    print("Planet Data:")
    for planet in planet_data['bodies']:
        if planet['isPlanet']:
            name = planet['englishName']
            mass_value = planet['mass']['massValue']
            mass_exponent = planet['mass']['massExponent']
            orbit_period = planet['sideralOrbit']
            print(f"Planet: {name}, Mass: {mass_value * 10**mass_exponent} kg, Orbit Period: {orbit_period} days")

fetch_planet_data()

# Task 3: Data Presentation and Analysis
# Defining a function to fetch planet data from API with improved formatting
def fetch_planet_data():
    url = "https://api.le-systeme-solaire.net/rest/bodies/"
    response = requests.get(url)
    planet_data = response.json()

    planets = []

    for planet in planet_data['bodies']:
        if planet['isPlanet']:
            name = planet['englishName']
            mass_value = planet['mass']['massValue']
            mass_exponent = planet['mass']['massExponent']
            orbit_period = planet['sideralOrbit']
            planets.append({'name': name, 'mass_value': mass_value, 'mass_exponent': mass_exponent, 'orbit_period': orbit_period})
    
    return planets

# Defining a function to find and return the planet with the largest mass
def find_heaviest_planet(planets):
    heaviest_planet_mass = max([planet['mass_value'] * 10**planet['mass_exponent'] for planet in planets])
    for planet in planets:
        total_mass = planet['mass_value'] * 10**planet['mass_exponent']
        if total_mass == heaviest_planet_mass:
            heaviest_planet_name = planet['name']

    return heaviest_planet_name, heaviest_planet_mass

planets = fetch_planet_data()
name, mass = find_heaviest_planet(planets)
print(f"\nThe heaviest planet is {name} with a mass of {mass} kg.")