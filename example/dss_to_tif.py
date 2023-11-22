from mil.army.usace.hec.vortex.io import TiffDataWriter
from mil.army.usace.hec.vortex.io import DataReader, DssDataReader

# Specify the path to .dss file 
OUT_P = 'C:/tif_files'
dss_fp = 'C:/dss_files/precip_20180505.dss'

# Get dss pathnames
sourceGrids = DataReader.getVariables(dss_fp)

# Loop through variables in dss file
for vName in sourceGrids:

    # Grab metadata for raster filename (may need adjusting based on format of dss)
    meta = [str(i) for i in vName.split('/')]
    start = meta[4].replace(':','H')
    end = meta[5].replace(':','H')

    # Specify output raster (example for obs only dss file)
    tif_fp = '{}/precip_obs_{}_{}.tif'.format(OUT_P, start, end)
        
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
