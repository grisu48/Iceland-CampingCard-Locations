# Iceland-CampingCard-Locations

This is a simple python script to extract the locations of the CampingCard.is to a GPX file.

The provided GPX file is valid for 2017 and was used by an Iceland trip. A newer version for 2018 and 2019 is also included but not tested. Verify and use at own risk (it should be fine)

https://www.campingcard.is/

* `CampingCard.is_2019.gpx` - GPX file for CampingCard 2019
* `CampingCard.is_2018.gpx` - Legacy GPX file for 2018
* `CampingCard.is_2017.gpx` - Legacy GPX file for 2017

## Usage 

    ./fetch_campingcard_gpx.py >CampingCard.is_Locations.gpx

This will run the script and writes the GPX file to `CampingCard.is_Locations.gpx`
 
