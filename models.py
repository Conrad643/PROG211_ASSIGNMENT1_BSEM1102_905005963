"""models.py - Core classes for the Crop Yield Monitoring System.

Privacy note: no personal data is stored. Farms are identified by an
anonymous code (e.g. "FRM-001"), never by a farmer's name or phone number.
"""


class Crop:
    """A crop planted on a farm, together with its recorded harvests."""

    def __init__(self, name, area_hectares):
        if not Crop.validate_area(area_hectares):
            raise ValueError("Area must be a positive number of hectares.")
        self.name = name
        self.area_hectares = area_hectares
        # Harvests are stored as an immutable tuple of (season, kg) tuples.
        self.harvests = ()

    # ---- Instance methods -------------------------------------------------
    def record_harvest(self, season, kg):
        """Add one harvest record as a (season, kg) tuple."""
        if kg < 0:
            raise ValueError("Harvest weight cannot be negative.")
        self.harvests += ((season, kg),)

    def total_yield(self):
        """Total kilograms harvested across all seasons."""
        return sum(kg for _, kg in self.harvests)

    def yield_per_hectare(self):
        """Average kilograms harvested per hectare."""
        return self.total_yield() / self.area_hectares

    def best_harvest(self):
        """Return the (season, kg) tuple with the highest weight, or None."""
        if not self.harvests:
            return None
        return max(self.harvests, key=lambda harvest: harvest[1])

    def display_info(self):
        print(
            f"  - {self.name.title()}: {self.area_hectares} ha, "
            f"{self.total_yield()} kg total "
            f"({self.yield_per_hectare():.1f} kg/ha)"
        )
        for season, kg in self.harvests:
            print(f"      {season}: {kg} kg ({Crop.kg_to_bags(kg)} bags)")

    # ---- Static methods ---------------------------------------------------
    @staticmethod
    def validate_area(area):
        """An area is valid if it is a positive number."""
        return isinstance(area, (int, float)) and area > 0

    @staticmethod
    def kg_to_bags(kg, bag_weight_kg=50):
        """Convert kilograms to standard 50 kg bags."""
        return round(kg / bag_weight_kg, 1)


class Farm:
    """A farm identified by an anonymous code, holding several crops."""

    total_farms = 0  # class attribute shared by all Farm objects

    def __init__(self, farm_id, district):
        if not Farm.validate_farm_id(farm_id):
            raise ValueError("Farm ID must look like 'FRM-001' (anonymous code).")
        self.farm_id = farm_id
        self.district = district
        self.crops = {}  # crop name -> Crop object
        Farm.total_farms += 1

    # ---- Instance methods -------------------------------------------------
    def add_crop(self, crop):
        """Attach a Crop object to this farm."""
        self.crops[crop.name.lower()] = crop

    def farm_total_yield(self):
        """Total kilograms harvested from every crop on this farm."""
        return sum(crop.total_yield() for crop in self.crops.values())

    def display_info(self):
        print(f"Farm {self.farm_id} ({self.district})")
        if not self.crops:
            print("  (no crops recorded)")
        for crop in self.crops.values():
            crop.display_info()
        print(f"  Farm total: {self.farm_total_yield()} kg")

    # ---- Class methods ----------------------------------------------------
    @classmethod
    def get_total_farms(cls):
        """How many Farm objects have been created."""
        return cls.total_farms

    @classmethod
    def from_dict(cls, data):
        """Build a Farm (and its crops) from a plain dictionary.

        Expected format:
            {"farm_id": "FRM-003", "district": "Kailahun",
             "crops": {"rice": 2.0, "cassava": 1.5}}   # crop -> hectares
        """
        farm = cls(data["farm_id"], data["district"])
        for crop_name, area in data.get("crops", {}).items():
            farm.add_crop(Crop(crop_name, area))
        return farm

    # ---- Static methods ---------------------------------------------------
    @staticmethod
    def validate_farm_id(farm_id):
        """Anonymous codes only: 'FRM-' followed by digits."""
        return (
            isinstance(farm_id, str)
            and farm_id.startswith("FRM-")
            and farm_id[4:].isdigit()
        )
