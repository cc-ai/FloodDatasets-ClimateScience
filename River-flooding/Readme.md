This folder contain the datasets and codes to read return periods data.

# Datasets

## Flood inundation maps

Flood inundation maps are simulated by ListFlood model in Dottori, F., P. Salamon, A. Bianchi, L. Alfieri, F. A. Hirpa, and L. Feyen (2016), Development and evaluation of a framework for global flood hazard mapping, Adv. Water Resour., 94, 87–102, https://doi:10.1016/j.advwatres.2016.05.002. All return periods can be found [here](https://data.jrc.ec.europa.eu/collection/floods) and also in `network/tmp1/ccai/climate-data/river-flooding/flood-maps`. Available in 900-m resolution globally and 100-m in Europe.

## Return period maps

Future return periods of the corresponding flood inundation maps calculated by the models presented in Alfieri, L., Bisselink, B., Dottori, F., Naumann, G., de Roo, A., Salamon, P., et al. (2017). Global projections of river flood risk in a warmer world.
Earth’s Future, 5(2), 171–182. https://doi.org/10.1002/2016EF000485 located in `network/tmp1/ccai/climate-data/river-flooding/return-period`.

`shift-in-frequency.py` : Code to read the data for a given coordination, calculating mean value of seven different models and their standard deviation in different warming levels under RCP 8.5 (business as usual). 




.
