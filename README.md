# Crop Yield Monitoring System

A small Python program that tracks crop harvests on farms, built with Object-Oriented Programming for **PROG211 Object-Oriented Programming 1** (Limkokwing University, Sierra Leone).

**Domain:** Agriculture. Smallholder farmers, extension workers, and community groups in Sierra Leone can record harvests of crops like rice, cassava, and groundnut, and see yield per hectare and totals per farm.

## How to run

Requires Python 3.8 or newer. No extra packages are needed.

```
python main.py
```

## Project structure

| File | Purpose |
|------|---------|
| `models.py` | The `Crop` and `Farm` classes |
| `registry.py` | A dictionary of farms, with functions to add, find, and display records |
| `main.py` | Demo that creates objects and prints a report |
| `LICENSE` | MIT open-source license |

## How it meets the assignment

**Task 1 - Classes and objects**
- `Crop` has attributes `name`, `area_hectares`, `harvests` and methods such as `record_harvest()` and `display_info()`.
- `Farm` has attributes `farm_id`, `district`, `crops` and methods such as `add_crop()` and `display_info()`.
- Objects interact: a `Farm` holds `Crop` objects and calls their methods to calculate its total yield.

**Task 2 - Data structure**
- One data structure is used to store the objects: a **dictionary** in `registry.py`, with the anonymous farm ID as the key.
- `add_farm()` and `display_farms()` add and show records. `find_farm()` looks up a farm by ID.
- Harvests are stored as **tuples** `(season, kg)`, since a past harvest record should not change.

**Task 3 - Methods**
- Instance methods: `record_harvest()`, `total_yield()`, `yield_per_hectare()`, `add_crop()`, `farm_total_yield()`, `display_info()`.
- Class methods (`@classmethod`): `Farm.from_dict()` builds a farm from a dictionary, and `Farm.get_total_farms()` returns how many farms exist.
- Static methods (`@staticmethod`): `Crop.validate_area()`, `Crop.kg_to_bags()`, `Farm.validate_farm_id()`.

## Digital Public Goods (DPG) alignment

| DPG principle | How this project meets it |
|---------------|---------------------------|
| **Open-source** | Code is public on GitHub under the MIT license, so anyone can use, adapt, and improve it. |
| **Inclusive and accessible design** | Plain-text output in simple English. Weights are in kilograms and 50 kg bags, which farmers already use. Runs on any computer with Python and needs no internet. |
| **Privacy-respecting** | No sensitive personal data is stored. Farms use anonymous codes like `FRM-001`. `Farm.validate_farm_id()` rejects anything else, so a farmer's name cannot be entered by mistake. |
| **Modular and reusable** | Models, storage, and demo are in separate files. The classes can be reused in a web app, a mobile app, or a different data store without changes. |

## Sample input and output

**Sample input** (from `main.py`): farms `FRM-001` (Bo), `FRM-002` (Port Loko), and `FRM-003` (Kailahun, built with `Farm.from_dict()`), each with crops and harvest records. A duplicate ID and an invalid ID are also tried on purpose.

**Output:**

```
Added farm FRM-001.
Added farm FRM-002.
Farm FRM-001 already exists - not added.
Added farm FRM-003.

=== Crop Yield Report (3 farms) ===
Farm FRM-001 (Bo)
  - Rice: 2.0 ha, 3900 kg total (1950.0 kg/ha)
      2025 wet season: 1800 kg (36.0 bags)
      2026 wet season: 2100 kg (42.0 bags)
  - Cassava: 1.5 ha, 3000 kg total (2000.0 kg/ha)
      2026 dry season: 3000 kg (60.0 bags)
  Farm total: 6900 kg

Farm FRM-002 (Port Loko)
  - Groundnut: 1.0 ha, 650 kg total (650.0 kg/ha)
      2026 wet season: 650 kg (13.0 bags)
  Farm total: 650 kg

Farm FRM-003 (Kailahun)
  - Rice: 2.5 ha, 2400 kg total (960.0 kg/ha)
      2026 wet season: 2400 kg (48.0 bags)
  - Cassava: 1.0 ha, 0 kg total (0.0 kg/ha)
  Farm total: 2400 kg

Total farms created: 3
Best rice harvest on FRM-001: ('2026 wet season', 2100)
2100 kg equals 42.0 bags
Rejected: Farm ID must look like 'FRM-001' (anonymous code).
```