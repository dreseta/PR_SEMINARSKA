import json
import csv

# Če so tvoji podatki v datoteki, npr. 'podatki.json', uporabi to:
with open("segments.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Če imaš podatke direktno v spremenljivki, jih lahko nadomestiš:
# data = [...]  <-- tukaj prilepiš tvoj JSON seznam

# Določimo polja, ki jih želimo v CSV
fieldnames = [
    "id", "name", "activity_type", "distance", "average_grade",
    "maximum_grade", "elevation_high", "elevation_low",
    "total_elevation_gain", "kom", "qom", "climb_score",
    "is_flat", "custom_climb_category", "country", "region"
]

# Ustvari CSV datoteko
with open("segmenti.csv", "w", newline='', encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for segment in data:
        # Pretvori seznam "region" v niz, če obstaja
        segment["region"] = ", ".join(segment.get("region", []))
        # Piši samo želena polja
        writer.writerow({key: segment.get(key, "") for key in fieldnames})
