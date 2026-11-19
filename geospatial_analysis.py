import pandas as pd
import folium

# Load regional dataset
df = pd.read_csv("regional_dataset.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove duplicate and missing records
df = df.drop_duplicates()
df = df.dropna(subset=["State", "City", "Postal Code"])

# Calculate regional revenue
if "Revenue" in df.columns:
    revenue = df.groupby("State")["Revenue"].sum()
    print("Revenue by State:")
    print(revenue)

# Calculate user density
if "Users" in df.columns:
    density = df.groupby("State")["Users"].sum()
    print("User Density by State:")
    print(density)

# Create interactive map
map_view = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5
)

# Save interactive map
map_view.save("regional_map.html")

print("Geospatial analysis completed!")
print("Map saved as regional_map.html")
