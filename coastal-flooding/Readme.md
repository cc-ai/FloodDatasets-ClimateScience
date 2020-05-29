This file contains links to the generated coastal flood maps, sea level projections and codes to construct the file names for a given coordination.

# Datasets

## North America coastal inundation maps

The simulated coastal flood maps are provided in `/network/tmp1/ccai/climate-data/coastalflood_NorthAmerica`. It contains inundation maps in year 2050 and 2100 under RCP 2.6 (extreme cut policy) and RCP 8.5 (business as usual).

## Coastal flood maps with uncertainty (need to be updated)

Same as North america coastal maps + Lower(5th percentile) and Upper(95th percentile) bounds on sea level projection. Located in `/network/tmp1/ccai/climate-data/coastalflood`.

## Sea level projections 

Sea level projections used in coastal flood simulation are calculated by CMIP5 runs. More details in Kopp, R. E. et al. Probabilistic 21st and 22nd century sea-level projections at a global network of tide-gauge sites. Earth’s. Future 2, 383–406 (2014). https://doi.org/10.1002/2014EF000239. The projections are available in `/network/tmp1/ccai/climate-data/sea-level-projection`



# Code

`coastalflood_name_construction.py` : This code generated the name of the coastal maps for a given coordination. There are many of them ;)
