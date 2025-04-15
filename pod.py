import json
import csv

# Naloži podatke (uporabi tvoje dejanske JSON podatke tukaj)
with open("segments_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

# Pripravi seznam vseh segmentov
segments = []
for entry in data["all"]:
    segments.extend(entry["segments"])

# Definiraj imena stolpcev za CSV brez elevation_profile
fieldnames = [
    "id", "name", "climb_category", "climb_category_desc", "avg_grade",
    "elev_difference", "distance", "start_lat", "start_lng",
    "end_lat", "end_lng", "starred"
]

# Zapiši podatke v CSV
with open("segmenti.csv", "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    for seg in segments:
        row = {
            "id": seg["id"],
            "name": seg["name"],
            "climb_category": seg["climb_category"],
            "climb_category_desc": seg["climb_category_desc"],
            "avg_grade": seg["avg_grade"],
            "elev_difference": seg["elev_difference"],
            "distance": seg["distance"],
            "start_lat": seg["start_latlng"][0],
            "start_lng": seg["start_latlng"][1],
            "end_lat": seg["end_latlng"][0],
            "end_lng": seg["end_latlng"][1],
            "starred": seg["starred"]
        }
        writer.writerow(row)

print("CSV datoteka 'segmenti.csv' je bila ustvarjena.")
