import pandas as pd
import numpy as np
import os
import io

# Collect all the files into one list
root_files = os.listdir('trees_all')
sub_files_to_flatten = [[f'{r}/{f}' for f in os.listdir(f'trees_all/{r}')] for r in root_files]
#Flatten list of files into one list
sub_files = [f'trees_all/{item}' for sublist in sub_files_to_flatten for item in sublist]
# Get rid of non noaa files
sub_files = [file for file in sub_files if 'noaa' in file]
print(f'{len(sub_files)} files')

cols = ['year','avg_tree_ring_width','lat','long','elevation','tree_species','organism_group']
df_final = pd.DataFrame(columns=cols)
north_lat_ind = len('# Northernmost_Latitude:')


# Get data table from files
for i, fl in enumerate(sub_files[1000:2000]):
    north_lat = south_lat = west_lon = east_lon = 0
    species = ''
    earliest_year,latest_year = 0,0
    organism_group = 0 #?
    elevation = 0
    years,avg = [],[]
    # Tree ring and meta data from the file
    with open(fl,'r') as f:
        if (i % 25 == 0):
            print(100 * i / 1000,'%', sep='')
        lines = f.readlines()
        for i in range(len(lines)):
            if lines[i].startswith('# Northernmost_Latitude:'):
                north_lat = float(lines[i].split(' ')[2])
            elif lines[i].startswith('# Southernmost_Latitude:'):
                south_lat = float(lines[i].split(' ')[2])
            elif lines[i].startswith('# Easternmost_Longitude:'):
                east_lon = float(lines[i].split(' ')[2])
            elif lines[i].startswith('# Westernmost_Longitude:'):
                west_lon = float(lines[i].split(' ')[2])
            elif lines[i].startswith('# Species_Name:'):
                species = lines[i].split(': ')[1].strip()
            elif lines[i].startswith('# Earliest_Year:'):
                try:
                    earliest_year = int(lines[i].split(': ')[1].strip())
                except ValueError:
                    earliest_year = np.nan
            elif lines[i].startswith('# Most_Recent_Year:'):
                try:
                    latest_year = int(lines[i].split(': ')[1])
                except ValueError:
                    latest_year = np.nan
            elif lines[i].startswith('# Elevation:'):
                try:
                    elevation = float(lines[i].split(': ')[1])
                except ValueError:
                    elevation = np.nan
            elif lines[i].startswith('age'):

                lat = (north_lat + south_lat)/2
                long = (east_lon + west_lon)/2

                #Should be the last thing found
                extracted = ' '.join(lines[i:])
                data = io.StringIO(extracted)
                df_data = pd.read_csv(data, sep="\t")
                age_label = df_data.columns[0]
                df_data['Avg'] = df_data.drop(age_label,axis=1).mean(axis=1)
                years,avg = df_data[age_label].tolist(),df_data['Avg'].tolist()
                for i in range(len(years)):
                    y, a = years[i], avg[i]
                    feats = {'year':y,'lat':lat,'long':long, 'avg_tree_ring_width':a,'elevation':elevation,'tree_species':species,'organism_group':0}
                    df_final = df_final.append(feats,ignore_index=True)

df_final.to_csv('clean_tree_data2000.csv', index=False)




