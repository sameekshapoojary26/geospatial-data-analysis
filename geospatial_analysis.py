import pandas as pd
import folium

# Load dataset
df = pd.read_csv("india_regional_market_v2.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Remove duplicate and missing records
df = df.drop_duplicates()
df = df.dropna(subset=["State", "City", "Latitude", "Longitude"])

# Regional market analysis
print("Total Records:", len(df))
print("\nMonthly Search Demand by State:")
print(df.groupby("State")["MonthlySearchDemand"].sum())

print("\nAverage Acquisition Cost by State:")
print(df.groupby("State")["EstimatedAcquisitionCostINR"].mean())

map_view = folium.Map(
    location=[20.5937, 78.9629],
    zoom_start=5,
    tiles="CartoDB positron"

)

# Add locations to map
for _, row in df.iterrows():
    folium.CircleMarker(
        location=[row["Latitude"], row["Longitude"]],
        radius=5,
        popup=(
            f"City: {row['City']}<br>"
            f"State: {row['State']}<br>"
            f"Monthly Search Demand: {row['MonthlySearchDemand']}"
        ),
        tooltip=row["City"],
        color="blue",
        fill=True,
        fill_opacity=0.6
    ).add_to(map_view)

# Save interactive map
map_view.save("regional_map.html")

print("\nGeospatial analysis completed successfully!")
print("Interactive map saved as regional_map.html")
