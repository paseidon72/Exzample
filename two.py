import json


data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    },
"researcher": {
        "name": "Ford Prefect",
        "species": "Ketelgeusian",
        "relatives": [
            {
                "name": "Vaphod Reeblebrox",
                "species": "Metelgeusian"
            }
        ]
    }
}
with open("data_file.json", "w") as write_file:
    json.dump(data, write_file, indent=4)
