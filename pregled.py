import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Če želiš zemljevid:
import geopandas as gpd
from shapely.geometry import Point
import contextily as ctx

# Nastavitve za lepše grafe
sns.set(style="whitegrid")
plt.rcParams["figure.autolayout"] = True

# Naloži podatke
df = pd.read_csv("segmenti.csv")

# Osnovne informacije
print("Osnovne informacije:")
print(df.info())
print("\nStatistični opis:")
print(df.describe())

# >>>>>> FILTER za dolžino > 0
df_filtered = df[df["distance"] > 0]

# 1. Histogram dolžine segmentov (brez distance = 0)
plt.figure(figsize=(10, 6))
sns.histplot(df_filtered["distance"], bins=30, kde=True)
plt.title("Porazdelitev dolžine segmentov (v metrih)")
plt.xlabel("Dolžina segmenta (m)")
plt.ylabel("Število segmentov")
plt.grid(True)
plt.savefig("graf1_histogram_dolzina.png")
plt.close()

# 2. Višinska razlika glede na dolžino segmenta
plt.figure(figsize=(10, 6))
sns.scatterplot(x="distance", y="elev_difference", hue="climb_category", data=df, palette="viridis")
plt.title("Višinska razlika glede na dolžino segmenta")
plt.xlabel("Dolžina segmenta (m)")
plt.ylabel("Višinska razlika (m)")
plt.legend(title="Kategorija vzpona")
plt.grid(True)
plt.savefig("graf2_scatter_dolzina_vs_visina.png")
plt.close()

# 3. Povprečni naklon po kategoriji vzpona
plt.figure(figsize=(8, 6))
sns.boxplot(x="climb_category", y="avg_grade", data=df)
plt.title("Povprečni naklon po kategoriji vzpona")
plt.xlabel("Kategorija vzpona")
plt.ylabel("Povprečni naklon (%)")
plt.grid(True)
plt.savefig("graf3_boxplot_naklon_kategorije.png")
plt.close()

# 4. Geografska razporeditev začetnih točk z zemljevidom
geometry = [Point(xy) for xy in zip(df["start_lng"], df["start_lat"])]
gdf = gpd.GeoDataFrame(df, geometry=geometry, crs="EPSG:4326")
gdf = gdf.to_crs(epsg=3857)

fig, ax = plt.subplots(figsize=(10, 8))
gdf.plot(ax=ax, column="climb_category", cmap="coolwarm", legend=True, markersize=20)
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)
ax.set_title("Geografske začetne točke segmentov z zemljevidom")
ax.set_axis_off()
plt.savefig("graf4_geografske_tocke_map.png")
plt.close()

# 5. Frekvenca kategorij vzpona
plt.figure(figsize=(8, 6))
sns.countplot(x="climb_category", data=df, palette="Set2")
plt.title("Frekvenca kategorij vzpona")
plt.xlabel("Kategorija vzpona")
plt.ylabel("Število segmentov")
plt.savefig("graf5_frekvenca_kategorij.png")
plt.close()

# 6. Top 10 najstrmejših vzponov
print("\nTop 10 najstrmejših vzponov:")
top_strmi = df[df["avg_grade"] > 0].sort_values("avg_grade", ascending=False).head(10)
print(top_strmi[["name", "avg_grade", "elev_difference", "distance"]])

print("\nVse vizualizacije so bile shranjene kot slike PNG.")
