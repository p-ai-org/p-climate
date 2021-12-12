#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np


# In[19]:


temp_df_pt1 = pd.read_csv('../actual_temperature_data/gridded_averages_1880-2021/NOAAGlobalTemp_v5a_1.csv')
temp_df_pt2 = pd.read_csv('../actual_temperature_data/gridded_averages_1880-2021/NOAAGlobalTemp_v5a_2.csv')

# concatenate dataframes
# gonna turn all the wrong years into -1
frames = [temp_df_pt1, temp_df_pt2]
temp_df = pd.concat(frames, sort=False)

tree_df = pd.read_csv('../tree_data.csv')
tree_df['year'] = tree_df['year'].apply(lambda x: int(x) if str(x).isdigit() else -1)
print(tree_df['tree_species'].value_counts())

# In[5]:




# In[20]:


# How many have bad years
print(tree_df.shape)


# In[21]:


def get_5x5_grid(og_lat, og_lon, base=2.5):
    lat1 = base * round((og_lat-2.5)/base)
    lat2 = base * round((og_lat+2.5)/base)

    lon1 = base * round((og_lon-2.5)/base)
    lon2 = base * round((og_lon+2.5)/base)

    if lat2-2.5 < og_lat:
        lat2 += 2.5
        lat1 += 2.5
    else:
        lat2 -= 2.5
        lat1 -= 2.5

    if lon2-2.5 < og_lon:
        lon2 += 2.5
        lon1 += 2.5
    else:
        lon2 -= 2.5
        lon1 -= 2.5

    if (lat1 % 5 )== 0 or (lat2 % 5 )== 0:
        if lat1 < 0:
            lat1 += 2.5
            lat2 += 2.5
        else: 
            lat1 -= 2.5
            lat2 -= 2.5

    if (lon1 % 5 )== 0 or (lon2 % 5 )== 0:
        lon1 += 2.5
        lon2 += 2.5

    if (lat1 == -92.5 and lat2 == -87.5):
        lat1 = -87.5
        lat2 = -82.5
    elif (lat1 == 87.5 and lat2 == 92.5):
        lat1 = 82.5
        lat2 = 87.5
    
    if (lon1 == 0.0 and lon2 == 5.0):
        lon1 = 2.5
        lon2 = 7.5
    elif (lon1 == 355.0 and lon2 == 360.0):
        lon1 = 352.5
        lon2 = 357.5

    return lat1, lat2, lon1, lon2


# In[22]:


temp_df['year'] = temp_df['time'].apply(lambda x: str(x)[0:4])
temp_df = temp_df.dropna(subset=['anom'])
temp_annual_df =  temp_df.groupby(['year', 'lat', 'lon']).agg({'anom': ['mean']}).reset_index()


# In[24]:


# given an observation row, return the row with the correct 5x5 temperature anomaly

def get_gridded_temp_anom(lat, lon, year):
    lat1, lat2, lon1, lon2 = get_5x5_grid(lat, lon)
    temp_df_for_lat_lon = temp_df[((temp_df['lat'] == lat1) | (temp_df['lat'] == lat2)) &
                                  ((temp_df['lon'] == lon1) | (temp_df['lon'] == lon2)) &
                                  (temp_df['year'] == str(year))]
    annual_temp_df_for_lat_lon = temp_df_for_lat_lon.groupby(['year']).agg({'anom': ['mean']}).reset_index()
    if len(annual_temp_df_for_lat_lon[annual_temp_df_for_lat_lon['year']==str(year)]['anom']['mean'].tolist()) > 0:
        temp_anom = annual_temp_df_for_lat_lon[annual_temp_df_for_lat_lon['year']==str(year)]['anom']['mean'].tolist()[0]
        return temp_anom


# In[ ]:


# run it on the data

tree_df_temp = tree_df[tree_df['year'] > 1879]
tree_df_temp = tree_df_temp[tree_df_temp['year'] < 2021]
tree_df_temp = tree_df_temp[tree_df_temp['tree_species']
                            == 'Previa maxima']
tree_df_temp['temp_anom'] = tree_df_temp.apply(lambda x: get_gridded_temp_anom(x['lat'], x['long'], x['year']), axis=1)


# In[ ]:


tree_df_temp.to_csv('../data_with_temp/all_tree_with_temp_small.csv')


# In[ ]:




