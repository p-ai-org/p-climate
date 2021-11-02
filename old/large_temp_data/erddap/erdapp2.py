from erddapClient import ERDDAP_Griddap

dataset_id = "erdSoda331oceanmday"
remote = ERDDAP_Griddap('https://coastwatch.pfeg.noaa.gov/erddap', dataset_id)

print(remote)
print(remote.dimensions)

xSubset = ( remote.setResultVariables('temperature')
                  .setSubset(time="2012-01-13",
                             depth=slice(5.03355,6),
                             latitude=slice(18.09165, 31.96065),
                             longitude=slice(175,176))
                  .getxArray() )

print(xSubset)