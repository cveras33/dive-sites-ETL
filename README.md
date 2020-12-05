# U.S. Dive Sites ETL #
There is a lot of very important and useful data available these days, but it is often dispersed among multiple data sources and not well organized. Extracting the data from it's sources, transforming it by cleaning or reformatting it, and loading or storing the resulting data into a well designed database is a critical process for data-driven organizations. This process is referred to as ETL.

## Background ## 
Data about dive sites around the world which are within 25 miles of a wreck of obstruction, along with information about the weather and tides at the dive site will be extracted from multiple data sources. The data will then be transformed to ensure only relevant data from each of the sources makes it to the final database. Once the data is extracted, and cleaned/transformed, it will be loaded into a MongoDB database. 

This database is meant to serve diving companies, as well as independent divers that are planning future diving excursions to assist in a search to find a desired diving location and to provide important information about that dive site. 

## Table of Contents ## 
* [ETL Process](#etl-process)
  * [Step 1: Extract](#step-1-extract)
    * [Data Sources](#data-sources)
  * [Step 2: Transform](#step-2-transform)
  * [Step 3: Load](#step-3-load)
* [Data Sources](#data-sources)
* [Setup](#setup)
  * [Mac](#mac)
  * [PC](#pc)
* [Status](#status)
* [Contacts](#contacts)

## ETL Process ## 
### Step 1: Extract ### 

**Wrecks and Obstructions Extraction**
* Downloaded AWOIS Obstructions and AWOIS Wrecks .xlsx files from the [Wrecks and Obstructions Database](https://nauticalcharts.noaa.gov/data/wrecks-and-obstructions.html) 
* Converted the respective files to a .csv file on local machine 
* Read the .csv file into Jupyter Notebook for cleaning and transformation 

**Dive Sites Extraction**
* Used latitude and longitude values from wrecks and obstructions extracted data to make requests from [Dive Sites API](http://api.divesites.com/docs/) 
* Requests to the API found any dive sites within 25 miles of the latitude and longitute coordinates from the wrecks and obstructions extracted data
* Data returned from the API requests included Dive Site Name, Dive Site ID, and Distance from the coordinates used in the API request

**Tides and Weather Extraction**
* Again, used latitude and longitude values from wrecks and obstructions extracted data to make requests from [Open Weather API](https://openweathermap.org/api) to get temperature in fahrenheit(&deg;F) and wind speed(mph). 

#### Data Sources #### 
* [Dive Sites API](http://api.divesites.com/docs/)
* [Open Weather API](https://openweathermap.org/api)
* [Tides and Currents API](https://tidesandcurrents.noaa.gov/web_services_info.html)
* [Weather Stations List](https://tidesandcurrents.noaa.gov/cdata/StationList?type=Current+Data&filter=active)
* [Wrecks and Obstructions Database](https://nauticalcharts.noaa.gov/data/wrecks-and-obstructions.html)
  * AWOIS Wrecks (.xlsx)
  * AWOIS Obstructions (.xlsx)

### Step 2: Transform ###

### Step 3: Load ### 

## Setup ## 

#### Mac ####

#### PC ####

#### Status #### 
This project is *in progress*. 

#### Contacts #### 
[Tyler Brown](https://github.com/Starcode897)  
[William Rosen](https://github.com/wrosen07)  
[Buddy Slater](https://github.com/jtslater2)  
[Jessy Thomas](https://github.com/jethomas2020)  
[Chloe Veras](https://github.com/cveras33)
