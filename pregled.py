import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("segmenti.csv")

# Skupinsko število segmentov po regijah
region_counts = df['region'].value_counts().head(10)

print("Top 10 regij po številu segmentov:")
print(region_counts)

# Prikaz in shranjevanje grafa
plt.figure(figsize=(10,6))
region_counts.plot(kind='bar', color='skyblue')
plt.title('Top 10 regij po številu segmentov')
plt.xlabel('Regija')
plt.ylabel('Število segmentov')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("top10_regij_segmentov.png", dpi=300)

# Prikaži graf (neobvezno, lahko izpustiš če ti ni treba prikazat)
plt.show()

# Preštej število voženj po kategorijah vzpona (stolpec 'custom_climb_category')
category_counts = df['custom_climb_category'].value_counts()

# Izračunaj povprečno število voženj v posamezni kategoriji vzpona
average_rides_per_category = df.groupby('custom_climb_category')['id'].count() / len(df['custom_climb_category'].unique())

# Izpiši rezultate
print("\nŠtevilo voženj po kategorijah vzpona:")
print(category_counts)

print("\nPovprečno število voženj po kategorijah vzpona:")
print(average_rides_per_category)

# Vizualizacija števila voženj po kategorijah vzpona
plt.figure(figsize=(10, 6))
category_counts.plot(kind='bar', color='skyblue')
plt.title('Število Voženj po Kategorijah Vzpona')
plt.xlabel('Kategorija Vzpona')
plt.ylabel('Število Voženj')
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("števila_voženj_po_kategorijah_vzpona.png", dpi=300)

plt.show()


segment_counts = df['name'].value_counts()

# Izberi top 10
top_segments = segment_counts.head(10)

# Izpis v konzolo
print("\nTop 10 najbolj priljubljenih segmentov (po številu pojavitev):")
print(top_segments)

# Vizualizacija
plt.figure(figsize=(10, 6))
plt.barh(top_segments.index, top_segments.values, color='skyblue')
plt.title('Top 10 Najbolj Priljubljenih Segmentov (Po Številu Pojavitev)')
plt.xlabel('Število Pojavitev')
plt.ylabel('Ime Segmenta')
plt.tight_layout()

plt.savefig("najbolj_priljubljenih_segmentov.png", dpi=300)

# Prikaži graf
plt.show()


plt.figure(figsize=(8,6))
sns.histplot(df['distance'], bins=15, kde=True, color='green')
plt.title('Porazdelitev dolžine segmentov')
plt.xlabel('Dolžina segmenta (m)')
plt.ylabel('Frekvenca')
plt.tight_layout()
plt.savefig("porazdelitev_dolzin.png", dpi=300)
plt.show()

top_vzponi = df[['name', 'total_elevation_gain']].sort_values(by='total_elevation_gain', ascending=False).head(10)
print(top_vzponi)

plt.figure(figsize=(10,6))
top_vzponi.set_index('name').plot(kind='bar', legend=False, color='purple')
plt.title('Top 10 segmentov po višinski razliki')
plt.ylabel('Višinska razlika (m)')
plt.xlabel('Segment')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("top10_vzponi.png", dpi=300)
plt.show()

