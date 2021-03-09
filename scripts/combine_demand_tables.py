#!/usr/bin/python3

import pandas as pd
import geopandas as gpd

# Load each of the individual demand DataFrames
df_16_17 = pd.read_csv('../data/ousd_demand_16-17.csv')
df_17_18 = pd.read_csv('../data/ousd_demand_17-18.csv')
df_18_19 = pd.read_csv('../data/ousd_demand_18-19.csv')
df_19_20 = pd.read_csv('../data/ousd_demand_19-20.csv')
df_20_21 = pd.read_csv('../data/ousd_demand_20-21.csv')

# Add columns for each year of demand data
final_df = df_16_17
final_df['demand_16_17'] = df_16_17['Demand']
final_df['demand_17_18'] = df_17_18['Demand']
final_df['demand_18_19'] = df_18_19['Demand']
final_df['demand_19_20'] = df_19_20['Demand']
final_df['demand_20_21'] = df_20_21['Demand']

# Clean up columns
final_df = final_df.drop(columns=['Demand', 'Year', 'sitename CDE.1'])
final_df = final_df.rename(columns={'LATY DD offset':'lat', 'LONGX DD offset':'lon', 'sitename CDE':'school_name'})

# Remove NaN coordinate values
final_df = final_df.dropna(subset=['lat', 'lon'])

# Save DataFrame
final_df.to_csv('../data/ousd_combined_demand.csv', index=False)

# Create GeoDataFrame from coordinates
final_gdf = gpd.GeoDataFrame(final_df, geometry=gpd.points_from_xy(final_df['lon'], final_df['lat']))
final_gdf = final_gdf.drop(columns=['lat', 'lon'])

# Load gentrification GeoDataFrame for the bay area
gent_gdf = gpd.read_file('../data/sanfrancisco.gpkg')

# Join with our demand DataFrame
final_gdf = final_gdf.set_crs(gent_gdf.crs)
final_gdf = gpd.sjoin(final_gdf, gent_gdf)

# Save resulting GeoDataFrame
final_gdf.to_file("../data/school_demand.gpkg", driver="GPKG")