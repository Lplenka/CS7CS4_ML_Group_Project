# CS7CS4_ML_Group_Project
Motivation

 The commute speed in different cities across the world varies significantly. Often the commute speed is affected by distance, time of the week, month, year, road infrastructure, holidays, festivities, government policies etc. Many of these factors also vary in the extent they affect the speed across different cities of the world. 
This project aims to build a Machine Learning model that can predict the commute speed between any two points in a city on any day of the week at any given time. In addition, we want to analyze the most important factors affecting the speed of commute in different cities.
The factors we are considering are:
Road infrastructure score 
Name of the area in the city (along with Latitude and Longitude)
The number of nearby schools, hospitals.
Population density of the city.
Weather features like temperature, rain, snow, fog, thunder etc.
This project aims to answer the following questions:
How do the aforementioned factors affect the commute speed in cities?
Why do commute speeds in different cities across the world vary?
Given the aforementioned features, how accurately can we predict the commute speed in an area of a city?
Pivots
During the project proposal stage, we proposed predicting commute travel times between any two points in the city at any hour of the day based on Uber Travel Time data. But when we started fetching the data, we realized the data is way more convoluted and it is shared by Uber in a very different format than how it looks on the website. It had a lot of references to OpenStreetMap elements (way_id, node_id), data was aggregated quarterly while we needed it in a daily-hourly fashion, there was no straight reference to latitude and longitude. So, we pivoted to Uber Speed Data and aimed to predict the commute speed between any two areas in a city at any hour of the day. 

However, this dataset had speed data for segments of a ride or for a small street(less than a mile). So, this was not providing the mean travel speed for one entire ride from a location to another of a city rather provided speed for one segment of the ride which is an OpenStreetMap way_id. Hence, we pivoted again and decided to map way_id and node_id to latitude-longitude and then map those to area names. This helped us to merge the aforementioned features with  Uber Speed Data based on area name and analyse how these factors affect the commute speed within any area of a city at any hour of the day.
