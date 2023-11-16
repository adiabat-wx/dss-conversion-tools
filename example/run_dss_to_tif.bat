set "LOCAL_PATH=%~dp0\dss_to_tif.py"
:: Set VORTEX_HOME to Vortex path
set "VORTEX_HOME=C:\HEC\HEC-Vortex"
set "PATH=%VORTEX_HOME%\bin;%VORTEX_HOME%\bin\gdal;%PATH%"
set "GDAL_DRIVER_PATH=%VORTEX_HOME%\bin\gdal\gdalplugins"
set "GDAL_DATA=%VORTEX_HOME%\bin\gdal\gdal-data"
set "PROJ_LIB=%VORTEX_HOME%\bin\gdal\projlib"
set "CLASSPATH=%VORTEX_HOME%\lib\*"

C:\jython2.7.3\bin\jython.exe -J-Xmx5g -Djava.library.path=%VORTEX_HOME%\bin;%VORTEX_HOME%\bin\gdal %RELATIVE_PATH%
cmd /k
