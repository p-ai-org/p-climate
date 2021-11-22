import xarray as xr

fn = 'NOAAGlobalTemp_v5.0.0_gridded_s188001_e202109_c20211008T133250.nc'

csv_file_out = 'NOAAGlobalTemp_v5a.csv'

ds = xr.open_dataset(fn)
df = ds.to_dataframe()

df.to_csv(csv_file_out)