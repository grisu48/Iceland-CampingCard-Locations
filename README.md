# Iceland-CampingCard-Locations

This is a simple python script to extract the locations of the CampingCard.is to a GPX file.

The provided GPX file is valid for 2017 and was used by an Iceland trip. A newer version for 2018 is also included but not tested. Verify and use at own risk (but it should be fine)

https://www.campingcard.is/

* `CampingCard.is_2018.gpx` - GPX file for CampingCard 2018
* `CampingCard.is_2017.gpx` - Legacy file for 2017

## Usage 

    ./fetch_campingcard_gpx.py >CampingCard.is_Locations.gpx

This will run the script and writes the GPX file to `CampingCard.is_Locations.gpx`
 
