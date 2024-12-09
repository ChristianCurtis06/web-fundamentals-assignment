# Task 1: Setting Up a Python Virtual Environment and Installing Packages
import requests

# Task 2: Fetching Data from Pokemon API
# Defining a function to fetch data for Pikachu from API and print the extracted information
def fetch_pikachu_data():
    url = 'https://pokeapi.co/api/v2/pokemon/pikachu'
    try:
        response = requests.get(url)
        pikachu_data = response.json()

        if isinstance(pikachu_data, dict):
            print(f"Name: {pikachu_data.get("name", "No Name")}")
            print("Abilities:")
            for ability in pikachu_data.get("abilities"):
                print(f"- {ability['ability']['name']}")
        else:
            status = pikachu_data.get("status")
            reason = pikachu_data.get("reason", "Unknown error")
            print(f"Error {status}: {reason}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

#fetch_pikachu_data()

# Task 3: Analyzing and Displaying Data
# Defining a function to fetch and print pokemon data from API for each listed pokemon
def fetch_pokemon_data(pokemon_name):
    url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
    response = requests.get(url)
    pokemon_data = response.json()

    if isinstance(pokemon_data, dict):
        name = pokemon_data.get("name", "No Name")
        abilities = [ability['ability']['name'] for ability in pokemon_data.get("abilities")]
        return name, abilities
    else:
        status = pokemon_data.get("status")
        reason = pokemon_data.get("reason", "Unknown error")
        print(f"Error {status}: {reason}")

# Defining a function to calculate and return the average weight of the listed pokemon
def calculate_average_weight(pokemon_list):
    total_weight = 0
    for pokemon_name in pokemon_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{pokemon_name}'
        response = requests.get(url)
        pokemon_data = response.json()

        if isinstance(pokemon_data, dict):
            pokemon_weight = pokemon_data.get("weight", 0)
            total_weight += pokemon_weight
        else:
            status = pokemon_data.get("status")
            reason = pokemon_data.get("reason", "Unknown error")
            print(f"Error {status}: {reason}")

    average_weight = total_weight / len(pokemon_list)
    return average_weight

def main():
    try:
        pokemon_names = ["pikachu", "bulbasaur", "charmander"]
        for pokemon_name in pokemon_names:
            name, abilities = fetch_pokemon_data(pokemon_name)
            print(f"\nName: {name}")
            print("Abilities:")
            for ability in abilities:
                print(f"- {ability}")

        print(f"\nThe average weight of {", ".join(pokemon_names)}: {calculate_average_weight(pokemon_names) / 10} kg")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()