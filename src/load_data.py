import json
import requests
from db import Country, Region

class LoadData:
    DATA_URL = "https://storage.googleapis.com/dcr-django-test/countries.json"

    def __init__(self):
        # Cache of regions
        self.regions = {}

    def get_raw_data(self):
        response = requests.get(self.DATA_URL)

        if response.status_code == 200:
            return response.json()
        else: 
            return None

    def add_country(self, data):
        region_name = data.get("region", "Unknown")
        region_id = self.get_region_id(region_name)

        country = Country()
        found = country.get_by_name(data["name"])
        if found:
            # Storing the topLevelDomain array values as a single string separated by comma.
            top_level_domains = ", ".join(data["topLevelDomain"])
            country.update(data["name"], top_level_domains, data["capital"])
            return
        
        country.insert(
            data["name"],
            data["alpha2Code"],
            data["alpha3Code"],
            data["population"],
            region_id,
            data["topLevelDomain"],
            data["capital"],
        )

    def get_region_id(self, region_name):
        if region_name not in self.regions:
            region = Region()
            region.get_or_create_by_name(region_name)
            self.regions[region.data["name"]] = region.data["id"]
        return self.regions[region_name]

    def run(self):
        data = self.get_raw_data()
        for row in data:
            print(row)
            self.add_country(row)


if __name__ == "__main__":
    LoadData().run()

