from erddapy import ERDDAP


# def get_gridded_noaa_data(dataset_id, 
#                         time_start, time_end, 
#                         lat_start, lat_end,
#                         lon_start, lon_end):

#     e = ERDDAP(
#     server="https://gliders.ioos.us/erddap",
#     protocol="tabledap",
#     )

#     e.response = "csv"
#     e.dataset_id = "whoi_406-20160902T1700"
#     e.constraints = {
#         "time>=": "2016-07-10T00:00:00Z",
#         "time<=": "2017-02-10T00:00:00Z",
#         "latitude>=": 38.0,
#         "latitude<=": 41.0,
#         "longitude>=": -72.0,
#         "longitude<=": -69.0,
#     }
#     e.variables = [
#         "depth",
#         "latitude",
#         "longitude",
#         "salinity",
#         "temperature",
#         "time",
#     ]

#     df = e.to_pandas()
#     print(df)

e = ERDDAP(
    server= "https://www.ncei.noaa.gov/erddap/", #"https://gliders.ioos.us/erddap",
    protocol="griddap",
    response="opendap",
    )

e.response = "csv"
e.dataset_id =  "ncdc_oisst_v2_avhrr_by_time_zlev_lat_lon" # "nmme_cfs_v2_va200_by_time_lat_lon"
# "ersst_v3b_by_time_lev_lat_lon"
# "ncdc_oisst_v2_avhrr_by_time_zlev_lat_lon"  #"whoi_406-20160902T1700"

e.griddap_initialize()

import json

# print(f"variables in this dataset:\n\n{e.variables}")
# print(
#     f"\nconstraints of this dataset:\n\n{json.dumps(e.constraints, indent=1)}"
# )
e.constraints = {
        "time>=": "2000-10-03T12:00:00Z",
        "time<=": "2021-10-03T12:00:00Z",
        "time_step": 1,
        "depth>=": 0.0,
        "depth<=": 0.0,
        "depth_step": 1,
        "latitude>=": -89.875,
        "latitude<=": 89.875,
        "latitude_step": 1,
        "longitude>=": 0.125,
        "longitude<=": 359.875,
        "longitude_step": 1
    }
# e.variables = [
#         "depth",
#         "latitude",
#         "longitude",
#         "sst",
#         "anom",
#         "err",
#         "time",
#     ]

df = e.to_pandas()
df.to_csv('test3.csv')
# print(df)

# ds = e.to_xarray()

# ds["sst"].plot()