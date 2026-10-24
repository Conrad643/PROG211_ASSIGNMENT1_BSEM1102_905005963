"""main.py - Demo of the Crop Yield Monitoring System.

Run with:  python main.py
"""

from models import Crop, Farm
from registry import add_farm, display_farms, find_farm


def main():
    registry = {}  # the single data structure: farm_id -> Farm

    # --- Task 1: create objects and let them interact ----------------------
    farm1 = Farm("FRM-001", "Bo")
    rice = Crop("rice", 2.0)
    rice.record_harvest("2025 wet season", 1800)
    rice.record_harvest("2026 wet season", 2100)
    cassava = Crop("cassava", 1.5)
    cassava.record_harvest("2026 dry season", 3000)
    farm1.add_crop(rice)
    farm1.add_crop(cassava)

    farm2 = Farm("FRM-002", "Port Loko")
    groundnut = Crop("groundnut", 1.0)
    groundnut.record_harvest("2026 wet season", 650)
    farm2.add_crop(groundnut)

    # --- Task 2: add and display records using the dictionary --------------
    add_farm(registry, farm1)
    add_farm(registry, farm2)
    add_farm(registry, farm1)  # duplicate ID: rejected

    # --- Task 3: class method building a farm from a dictionary ------------
    farm3 = Farm.from_dict(
        {"farm_id": "FRM-003", "district": "Kailahun",
         "crops": {"rice": 2.5, "cassava": 1.0}}
    )
    farm3.crops["rice"].record_harvest("2026 wet season", 2400)
    add_farm(registry, farm3)

    display_farms(registry)

    # --- Extra demos: methods and input validation --------------------------
    print("Total farms created:", Farm.get_total_farms())
    print("Best rice harvest on FRM-001:", find_farm(registry, "FRM-001").crops["rice"].best_harvest())
    print("2100 kg equals", Crop.kg_to_bags(2100), "bags")

    try:
        Farm("Mariama-Kamara", "Bo")  # a personal name is rejected on purpose
    except ValueError as error:
        print("Rejected:", error)


if __name__ == "__main__":
    main()
