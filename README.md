# Chat-Map-Creator
This is the repository of Chat-Map-Creator, supporting multiple outuput (e.g. open street map .osm format, opendrive, etc...)

# Extract coordination and generate corresponding OSM&OpenDrive file
![2024-07-22 10-02-11屏幕截图](https://github.com/user-attachments/assets/7240f7ed-9b61-4b95-a94c-0037b2af304a)
![2024-07-22 10-02-34屏幕截图](https://github.com/user-attachments/assets/aa3bb70d-52fa-45c4-b4ae-281c307746e7)

# Installation Steps
1.Install pyproj, numpy ,setuptools==53.1.0,and osmread, python<=3.8

2.run gaode_return.py code,use text input get latitude and longatude

3.api_latitude_longitude_cen_to_osm.py convert coordination to osm file, then add_version_changeset_tonode add default dummy value to imcomplete node 

4.osm2xodr convert osm to opendrive file, then you can use it 
