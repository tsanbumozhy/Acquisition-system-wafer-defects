import json

with open(r'C:/Users/Anbumozhy/Desktop/KLA/Level_1_Input_Data/input.json') as json_File :
	data=json.load(json_File)


die = data['die']

streetWidth = data['street_width']

careAreaDimentions = data['care_areas']

exclusionZones = data['exclusion_zones']
