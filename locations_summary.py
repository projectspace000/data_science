#!/usr/bin/env python
#locations_summary.py

import pandas as pd

# import data and clean data
locations = pd.read_csv("C:\\Users\\flynn\\Desktop\\DataScience\\locations.csv", encoding = "latin-1")

# remove unwanted columns
print("Starting Columns\n")
list(locations.columns.values)

locations.drop(["locationCode1", "County", 
				"siteId", "terminalId", 
				"SiteStartDate", "latitude", 
				"longitude"], inplace = True, axis = 1)

print("Remaining Columns\n")
list(locations.columns.values)

# rename columns using proper name and case
# i need to find the right way to wrap this, toooooo loooong
locations.rename(columns={"Territory3" : "Territory", 
						"FSR2" : "FSR", "storeNumber1" : "Store",
						"LocationName" : "Location", "addressLine1" : "Address",
						"city" : "City", "state" : "State",
						"phoneNumber" : "Phone", "SerialNumber" : "Kiosk",
						"placement" : "Placement"}, inplace=True)

print("Cleaned Columns\n")
list(locations.columns.values)

# find a way to set a cleaner list like this
# columns_rename = ["Territory3 : Territory",
# 	["FSR2 : FSR"],
# 	["storeNumber1 : Store"],
# 	["LocationName : Location"],
# 	["addressLine1 : Address"],
# 	["city : City"],
# 	["state : State"],
# 	["phoneNumber : Phone"],
# 	["SerialNumber : Kiosk"],
# 	["placement : Placement"]]

# count locations by FSR
fsr_counts = locations.groupby(["FSR"]).size()
print(fsr_counts)