from erddapy import ERDDAP
from erddapClient import ERDDAP_Griddap
import json

# def get_gridded_noaa_data(dataset_id, 
#                         time_start, time_end, 
#                         depth_start, depth_end,
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
    protocol="griddap", #,
    response="opendap",
    )

e.response = "csv"
e.dataset_id = "erdSoda331oceanmday"
# "nceiErsstv5"
# "erdSoda331oceanmday"
# "hawaii_3e19_7ccd_16ff_LonPM180"
#"ncdc_oisst_v2_avhrr_amsr_by_time_zlev_lat_lon"
#"ersst_v3b_by_time_lev_lat_lon"
#"ncdc_oisst_v2_avhrr_by_time_zlev_lat_lon"
# "noaa_esrl_7ae4_472e_343f"
# "NOAA_DHW_monthly"
# "ncdc_oisst_v2_avhrr_by_time_zlev_lat_lon"
#"ersst_v3b_by_time_lev_lat_lon"
# "ncdc_oisst_v2_avhrr_by_time_zlev_lat_lon" # "nmme_cfs_v2_va200_by_time_lat_lon"
# "ncdc_oisst_v2_avhrr_by_time_zlev_lat_lon"  #"whoi_406-20160902T1700"

e.griddap_initialize()

print(f"variables in this dataset:\n\n{e.variables}")
print(
    f"\nconstraints of this dataset:\n\n{json.dumps(e.constraints, indent=1)}")
e.constraints = {
        "time>=": "2002-06-01T00:00:00Z", #"2020-02-28T12:00:00Z", # "2000-10-03T12:00:00Z",
        "time<=": "2011-10-04T00:00:00Z", # "2021-10-03T12:00:00Z",
        "time_step": 1,
        #  "lev>=": 0.0,
        # "lev<=": 0.0,
        # "lev_step": 1,
        "depth>=": 0.0,
        "depth<=": 0.0,
        "depth_step": 1,
        "latitude>=": 5, #.875,
        "latitude<=": 6, #.875,
        "latitude_step": 1,
        "longitude>=": 180, # 0.125,
        "longitude<=": 181, #359.875,
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
df.to_csv('ersst_v5_2002-06-01_to_2011-10-04_locs_5_6_180_181.csv')
# df.to_csv('oisst_v2_amsr_2002-06-01_to_2011-10-04_locs_5_6_180_181.csv')
# df.to_csv('ersst_v3b_1867-09-15_to_1867-09-15_locs_5_6_180_181.csv')
# df.to_csv('test3.csv')
# print(df)

# ds = e.to_xarray()

# ds["sst"].plot()