#!/usr/bin/env python
# coding: utf-8

# In[6]:


#!/usr/bin/env python
# coding: utf-8

import csv
import pandas as pd
import numpy as np
filename = 'C:....\\mila\\FloodArchive.xlsx';##directory

fopen=pd.read_excel(filename)

long=fopen['long']
lat=fopen['lat']
country=fopen['Country']
datebegin=fopen['Began']
floodcause=fopen['MainCause']
suffered=fopen['Displaced']
numdeath=fopen['Dead']
dateend=fopen['Ended']
severity=fopen['Severity']

userlon=73.5
userlat=15.5

long_list = np.abs(long-userlon) 
lat_list = np.abs(lat-userlat)         
      
long_idx = np.asarray(np.where( long_list <0.5 ))
lat_idx = np.asarray(np.where( lat_list <0.5))
history_report='There is no historical flood record in your region.'
coordinates_idx=[i for i in long_idx[0] if i in lat_idx[0]]
if len(coordinates_idx)>0:
    
    if (severity[coord_idx])<1.5:
        severity_rp='20 years (5 % chance of occurence)'
    elif (severity[coord_idx])==2:
        severity_rp='20 years (5 % chance) to 100 years (1 % chance of occurence)'
    elif (severity[coord_idx])>2:
        severity_rp='>100 years ( < 1 % chance of occurence)'
    
    coord_idx=coordinates_idx[-1]
    # indexlon=np.where(lon== findlon)
    floodduration=dateend[coord_idx]-datebegin[coord_idx]
    floodduration=str(floodduration).split()[0]
    # findlat=lat[min(range(len(lat)), key = lambda i: abs(lat[i]-userlat))] 
    # indexlat=np.where(lat== findlat)

    history_report='Based on the historical archives, the most recent flood in your region has occured on '+str(datebegin[coord_idx]).split()[0]+' due to the '+str(floodcause[coord_idx])+' and lasted for '+floodduration+' days.'+ str(suffered[coord_idx])+' people have sufferend from this flood and '+str(numdeath[coord_idx])+' people have died.' 'The return period of this flood is estimated to be ' +severity_rp  
    #     nomlat=find(abs(latlon(i,1)-latlonstorm(:,1))<1);
    #    nomlon=find(abs(latlon(i,2)-latlonstorm(:,2))<1);
print(history_report)


# In[ ]:




