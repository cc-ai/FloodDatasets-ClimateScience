#constructing the name of the data files
import math
####given lon by user :let say -160.27
userlon=-74.27
####given lat by user :let say 40.27
userlat=40.27

if userlat >0:
    V_hemisphere='N'
else:
    V_hemisphere='S'

if  userlon <0:
    H_hemisphere='W'
  
else:
    H_hemisphere='E'
    
############# construct name for warming level 2 --- 2050----RCP8.5 without storm

file_name_mean=V_hemisphere+str(abs(math.floor(userlat)))+H_hemisphere+str(abs(math.floor(userlon)))+ '.tif_2050_RCP85.tif'
#file_name_lower=V_hemisphere+str(abs(math.floor(userlat)))+H_hemisphere+str(abs(math.floor(userlon)))+ '.tif_2100_RCP85U.tif'
#file_name_upper=V_hemisphere+str(abs(math.floor(userlat)))+H_hemisphere+str(abs(math.floor(userlon)))+ '.tif_2100_RCP85L.tif'



