"""registry.py - Stores many Farm objects in ONE data structure: a dictionary.

The dictionary key is the unique, anonymous farm ID, so lookups are instant:
    registry = {"FRM-001": <Farm>, "FRM-002": <Farm>, ...}
"""


def add_farm(registry, farm):
    """Add a Farm to the registry. Returns True if added, False if duplicate."""
    if farm.farm_id in registry:
        print(f"Farm {farm.farm_id} already exists - not added.")
        return False
    registry[farm.farm_id] = farm
    print(f"Added farm {farm.farm_id}.")
    return True


def display_farms(registry):
    """Print every farm in the registry."""
    if not registry:
        print("No farms recorded yet.")
        return
    print(f"\n=== Crop Yield Report ({len(registry)} farms) ===")
    for farm in registry.values():
        farm.display_info()
        print()


def find_farm(registry, farm_id):
    """Return the Farm with this ID, or None if it does not exist."""
    return registry.get(farm_id)
