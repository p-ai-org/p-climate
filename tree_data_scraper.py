import os
import pandas as pd
import io

# Collect all the files into one list
root_files = os.listdir('trees_all')
sub_files_to_flatten = [[f'{r}/{f}' for f in os.listdir(f'trees_all/{r}')] for r in root_files]
#Flatten list of files into one list
sub_files = [f'trees_all/{item}' for sublist in sub_files_to_flatten for item in sublist]
print(f'{len(sub_files)} files')

df_final = pd.DataFrame(columns=['year','avg_tree_ring_width','lat','long','elevation','tree_species'])
north_lat_ind = len('# Northernmost_Latitude:')
# Get data table from files
for fl in sub_files:
    north_lat = south_lat = west_lon = east_lon = 0
    species = ''
    earliest_year,latest_year = 0,0
    organism_group = 0 #?
    elevation = 0
    years,avg = [],[]
    # Tree ring and meta data from the file
    with open(fl,'r') as f:
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
                species = lines[i].split(': ')[1]
            elif lines[i].startswith('# Earliest_Year:'):
                earliest_year = int(lines[i].split(': ')[1])
            elif lines[i].startswith('# Most_Recent_Year:'):
                latest_year = int(lines[i].split(': ')[1])
            elif lines[i].startswith('# Elevation:'):
                elevation = float(lines[i].split(': ')[1])
            elif lines[i].startswith('age'):
                #Should be the last thing found
                extracted = ' '.join(lines[i:])
                data = io.StringIO(extracted)
                df_data = pd.read_csv(data, sep="\t")
                age_label = df_data.columns[0]
                df_data['Avg'] = df_data.drop(age_label,axis=1).mean(axis=1)
                years,avg = df_data[age_label].tolist,df_data['Avg'].tolist()
                df_final.append()
    lat = (north_lat + south_lat)/2
    lon = (east_lon + west_lon)/2




