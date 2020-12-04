# U.S. Dive Sites ETL #
There is a lot of very important and useful data available these days, but it is often dispersed among multiple data sources and not well organized. Extracting the data from it's sources, transforming it by cleaning or reformatting it, and loading or storing the resulting data into a well designed database is a critical process for data-driven organizations. This process is referred to as ETL.

## Background ## 
Data about dive sites around the world, along with information about the weather, tides, and any wrecks or obstructions at the dive site will be extracted from multiple data sources. The data will then be transformed to ensure only relevant data from each of the datasets makes it to the final database. Once the data is extracted, and cleaned/transformed, it will be loaded into a SQL Database in PostgreSQL. 

This database is meant to cater to diving companies, as well as independent divers that are planning future diving excursions to assist in a search to find a desired diving location. 

## Table of Contents ## 
* [ETL Process](#etl-process)
  * [Step 1: Extract](#step-1-extract)
    * [Data Sources](#data-sources)
  * [Step 2: Transform](#step-2-transform)
  * [Step 3: Load](#step-3-load)
* [Data Sources](#data-sources)
* [Setup](#setup)
* [Status](#status)
* [Contacts](#contacts)

## ETL Process ## 
### Step 1: Extract ### 
#### Data Sources #### 
* [Dive Sites API](http://api.divesites.com/docs/)
* [Weather API](https://openweathermap.org/api)
* [Tides and Currents API](https://tidesandcurrents.noaa.gov/web_services_info.html)
* [Wrecks and Obstructions Database](https://nauticalcharts.noaa.gov/data/wrecks-and-obstructions.html)
  * AWOIS Wrecks (.xlsx)
  * AWOIS Obstructions (.xlsx)
* [Weather Station Identifiers](http://www.weathergraphics.com/identifiers/)

### Step 2: Transform ###

### Step 3: Load ### 

## Setup ## 

#### Status #### 
This project is *in progress*. 

#### Contacts #### 
[Tyler Brown](https://github.com/Starcode897)  
[William Rosen](https://github.com/wrosen07)  
[Buddy Slater](https://github.com/jtslater2)  
[Jessy Thomas](https://github.com/jethomas2020)  
[Chloe Veras](https://github.com/cveras33)
