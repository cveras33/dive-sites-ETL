# Dive Sites ETL #
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
* [Status](#status)
* [Contacts](#contacts)

## ETL Process ## 
### Step 1: Extract ### 

**Wrecks and Obstructions Extraction**
* Downloaded AWOIS Obstructions and AWOIS Wrecks `.xlsx files` from the [Wrecks and Obstructions Database](https://nauticalcharts.noaa.gov/data/wrecks-and-obstructions.html) 
* Converted the respective files to a `.csv file` on local machine 
* Read the `.csv file` into Jupyter Notebook for cleaning and transformation 

**Dive Sites Extraction**
* Used latitude and longitude values from wrecks and obstructions extracted data to make requests from [Dive Sites API](http://api.divesites.com/docs/) 
* Requests to the API found any dive sites within 25 miles of the latitude and longitute coordinates from the wrecks and obstructions extracted data
* Data returned from the API requests included Dive Site Name, Dive Site ID, and Distance from the coordinates used in the API request

**Tides and Weather Extraction**
* Again, used latitude and longitude values from final dive sites data frame to make requests from [Open Weather API](https://openweathermap.org/api) to get temperature in fahrenheit(&deg;F) and wind speed(mph). 

#### Data Sources #### 
* [Dive Sites API](http://api.divesites.com/docs/)
* [Open Weather API](https://openweathermap.org/api)
* [Tides and Currents API](https://tidesandcurrents.noaa.gov/web_services_info.html)
* [Weather Stations List](https://tidesandcurrents.noaa.gov/cdata/StationList?type=Current+Data&filter=active)
* [Wrecks and Obstructions Database](https://nauticalcharts.noaa.gov/data/wrecks-and-obstructions.html)
  * AWOIS Wrecks (.xlsx)
  * AWOIS Obstructions (.xlsx)

### Step 2: Transform ###

**Wrecks and Obstructions Cleaning**
* *Wrecks and Obstructions cleaning were done exclusive of one another, but the same steps were taken for both data sets* 
* After extracting these two `.xlsx files` and converting them to `.csv files` there was some data that was irrelevant to the final data base 
* The irrelevant files were dropped from the data frame, leaving Record #,	Vessel Terms,	Feature Type,	Lat,	Lng,	GP Quality, and History. 
* The remaining data was then separated into the following two data frames:
  * Wrecks/Obstructions data frame, with columns: 
    * Record #,	Vessel Terms,	Feature Type,	Lat,	Lng, and	GP Quality
  * History data frame, with columns: 
    * Record # and History

**Wreck, Obstructions, and Dive Sites Cleaning and Transformation**
* Following the cleaning of wrecks/obstructions data, the resulting data frames were used to make the dive site API calls, as stated above in the [Step 1: Extract](#step-1-extract) section 
* When running the API calls, a `try` and `except` block was included to fill any rows where there was not a dive site within 25 miles of a wreck/obstruction with `NaN`
* The resulting data from the API calls had about 2,000 rows with `NaN` in the dive site name column, and ultimately these rows were dropped by running a `dropna(subset = ['Dive Site Name'])` on the data frames. 

*The above steps were performed on a data frame which looked like the following image, containing data on wrecks/obstructions and the dive site, which will be separated into two data frames in later steps* 
![example](https://github.com/cveras33/dive-sites-ETL/blob/main/Screenshots/wrecks_dive_sites_df.png)

* After the data was cleaned, and properly formatted in the data frame shown above, the data was then separated into two sepratate data frames: 
  * One containing data on the dive sites with the following columns: 
    * Dive Site Name, Dive Site ID, Distance, and Record # 
  * Another containing data on the wrecks/obstructions with the following columns (acknowledging this table was previously created, but this step of combining and then re-separating data frames was pertinent to ensuring coordinates of dive sites were properly aligned with wrecks/obstructions within 25 miles of the proper coordinates): 
    * Record #,	Vessel Terms,	Feature Type,	Lat,	Lng, and	GP Quality
    
* Next for the dive sites data frame, the wrecks/obstructions data frames, and the history data frames, the respective data frames which were separated by wreck and obstructions were combined using the `pd.concat()` function part of the  `Pandas Library` resulting in the following `.csv files`
  * [final_dive_sites_transformed.csv](https://github.com/cveras33/dive-sites-ETL/blob/main/Resources/final_dive_sites_transformed.csv)
  * [final_history.csv](https://github.com/cveras33/dive-sites-ETL/blob/main/Resources/final_history.csv)
  * [final_wrecks_obstructs_transformed.csv](https://github.com/cveras33/dive-sites-ETL/blob/main/Resources/final_wrecks_obstructs_transformed.csv)

### Step 3: Load ### 

* Once the data frames were all properly formatted, cleaned and tranformed, the `.csv files` were loaded into a MongoDB database named `dive_sites_db` via Jupyter Notebook 
* The `.csv files` were first converted to a dictionary format using `csv.DictReader()`
* After the files were reformatted, a connection to Mongo was created using `PyMongo` 
* Finally, the reformatted files were inserted into collections in the `dive_sites_db` through an iterable `for loop` and `PyMongo` `insert()` function 

## Setup ## 

#### Status #### 
This project is *in progress*.

#### Contacts #### 
[Tyler Brown](https://github.com/Starcode897)  
[William Rosen](https://github.com/wrosen07)  
[Buddy Slater](https://github.com/jtslater2)  
[Jessy Thomas](https://github.com/jethomas2020)  
[Chloe Veras](https://github.com/cveras33)
