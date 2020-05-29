This folder contain the datasets and codes to read return periods data.

# Datasets

## Flood inundation maps

Flood inundation maps are simulated by ListFlood model in Dottori, F., P. Salamon, A. Bianchi, L. Alfieri, F. A. Hirpa, and L. Feyen (2016), Development and evaluation of a framework for global flood hazard mapping, Adv. Water Resour., 94, 87–102, https://doi:10.1016/j.advwatres.2016.05.002. All return periods can be found [here](https://data.jrc.ec.europa.eu/collection/floods) and also in `network/tmp1/ccai/climate-data/river-flooding/flood-maps`. Available in 900-m resolution globally and 100-m in Europe.

## Return period maps

Future return periods of the corresponding flood inundation maps calculated by the models presented in Alfieri, L., Bisselink, B., Dottori, F., Naumann, G., de Roo, A., Salamon, P., et al. (2017). Global projections of river flood risk in a warmer world.
Earth’s Future, 5(2), 171–182. https://doi.org/10.1002/2016EF000485 located in `network/tmp1/ccai/climate-data/river-flooding/return-period`.

# Codes

`shift-in-frequency.py` : Code to read the data for a given coordination, calculating mean value of seven different models and their standard deviation in different warming levels under RCP 8.5 (business as usual). 

## Depedencies
* `numpy`
* `pandas`
* `netCDF4`
* `matplotlib` 

 ## Example usage
 ```clojure
 filename='returnPeriodShift_HELIX_dis_rcp85_r1_statistics.nc'
 rps1 = netCDF4.Dataset(filename,"r") #read data
 rps1.variables #give you a list of the variables included in the dataset, and their description.
 
 
 lat=np.array(rps1.variables["lat"]) # Read lattitude array : shape = (360,)
 lon=np.array(rps1.variables["lon"]) # Read longitude array : shape = (720,)
 warming_level=np.array(rps1.variables["warming_lev"])# Give three warming level : array([1.5, 2. , 3. ], dtype=float32)
 baseline_rp = np.array(rps1.variables["baseline_rp"]) #   array([ 10.,  20.,  50., 100., 200., 500.], dtype=float32)
 baseline_rp_shift1 = np.array(rps1.variables["baseline_rp_shift"]) # shape = (3, 6, 720, 360)
 ```
 
 
To read the data of a specific baseline in a specific warming level, such as baseline_rp=50 and warming level=2:


```clojure
rp_shifted=baseline_rp_shift1[1,2,:,:] 
# 1 corresponds to the index of warming_level=2 in  array([1.5, 2. , 3. ], dtype=float32)
# 2 corresponds to the index of baseline_rp=50 in array array([ 10.,  20.,  50., 100., 200., 500.], dtype=float32)
```
This gives the global map of the new return period in the warming level 2 degree for floods with return period 50.

You can visualize this map accordingly : 

```clojure

fig, (ax1) = plt.subplots(figsize=(13, 3), ncols=1)
map=plt.imshow(np.transpose(baseline_rp_shift2[2,1,:,:]), cmap=plt.cm.get_cmap('Blues', 6))
plt.colorbar()
plt.clim(0, 40);

```







.
