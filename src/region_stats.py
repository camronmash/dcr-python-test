import json

DATA_FILE = "../data/countries.json"

def calculate_region_stats(countries):
    stats = []
    
    for country in countries:
        region = country['region']
        
        # Checks for the first entry of an existed entry of region
        region_info = next((item for item in stats if item['name'] == region), None)
        
        # If region doesn't exist, create a new entry
        if not region_info:
            region_info = {
                "name": region,
                "number_countries": 0,
                "total_population": 0
            }
            stats.append(region_info)
        
        region_info['number_countries'] += 1
        region_info['total_population'] += country['population']

    
    region_stats ={"regions": stats}
    return region_stats

def get_raw_data():
    data = None
    with open(DATA_FILE) as f:
        data = json.load(f)
    return data

countries = get_raw_data()
region_stats = calculate_region_stats(countries)
print(region_stats)