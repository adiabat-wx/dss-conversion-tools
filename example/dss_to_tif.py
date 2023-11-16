from mil.army.usace.hec.vortex.io import TiffDataWriter
from mil.army.usace.hec.vortex.io import DataReader, DssDataReader

# Specify the path to .dss file 
dss_fp = 'C:/dss_files/precip_20180505.dss'

# Get dss pathnames
sourceGrids = DataReader.getVariables(dss_fp)

# Loop through variables in dss file
for vName in sourceGrids:

    # Grab metadata for raster filename
    meta = [str(i) for i in vName.split('/')]
    start = meta[4].replace(':','H')
    end = meta[5].replace(':','H')

    # Specify output raster
    tif_fp = 'C:/pythonscripts/merced/precip_obs_'+start+'_'+end+'.tif'
        
    # Read DSS file to get variable as type <VortexData>
    srcs = DssDataReader.builder()\
            .path(dss_fp)\
            .variable(str(vName)).build()
    vData = srcs.getDtos()
  
    # Write DSS variable to raster
    myImport = TiffDataWriter.builder()\
            .data(vData)\
            .destination(tif_fp).build()
    myImport.write()
