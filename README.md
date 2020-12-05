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
* [Setup](#setup)
* [Sample Queries](#sample-queries)
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
* For a *deeper dive* into the cleaning process see [technical steps for cleaning](https://github.com/cveras33/dive-sites-ETL/blob/main/technical_steps_cleaning.md)
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
* Finally, the reformatted files were inserted into collections in the `dive_sites_db` through an iterable `for loop` and `PyMongo insert()` function 

## Setup ## 
1. Clone the repository to your local drive by: 
    * Clicking on the green "Code" buttom at the top of the page
    * Copying the `SSH` code 
    * Open your terminal and navigate to the directory you want this repository to live in 
      * i.e. `cd Documents/ETL-Project/` 
    * Type `git clone` and paste the `SSH` code you copied from the GitHub website into your terminal and hit enter 
2. You will need to have PyMongo and MongoDB installed on your machine in order to create and make queries on this database. 

**For Mac Users**: 
  * You will also need to have homebrew installed for some of the other installations. To install homebrew go to the following link and follow the instractions:
    * https://brew.sh/
  * To install PyMongo run the following in your terminal `pip install Flask-PyMongo` 
  * Then run `brew cask install chromedriver` in your terminal as well 
    * If you run into permission issues after installing chromedriver, you can grant permission by going to: System Preferences → Security and Privacy → General → Allow Anyway.
  * After all that is complete, run the following 3 commands in your terminal: 
    * `brew tap mongodb/brew`       
    * `brew install mongodb-community@4.4`
    * `brew services start mongodb-community@4.4`
  * You will also need to install MongoDB Compass for which you can find installation instructions at the following link: 
    * https://docs.mongodb.com/compass/master/install
    
**For PC Users**: 
  * Install Flask-PyMongo with the following command:
    * `pip install Flask-PyMongo`
  * Install the latest version of MongoDB Community Edition as described here:
    * https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/
  * Add the path to the MongoDB bin folder (probably something like: C:\Program Files\MongoDB\Server\4.4\bin\) to your System Environment Path Variable.
    
3. Now that all of the necessary technologies are installed, from the dive-sites-ETL folder in your terminal, type `jupyter notebook` and hit enter. This will open a tab in your default browser where you will see all the folders and files in the dive-sites-ETL folder. 
4. Click on the `load_to_mongodb.ipynb` file 
5. Once the notebook opens, click on the `Kernel` tab at the top of the notebook and select `Restart & Run All` 
6. This will create the `dive_sites_db` on your local machine. 
7. To view the database open the MongoDB Compass program and click connect 
8. `dive_sites_db` should be listed and you can click on it to view collections, as well as click on any of the collections to view a single record 

## Sample Queries ## 
So, now you have the repository and database set up on your local machine and you're ready to make some queries to find a great dive site with some cool wrecks or obstructions to see! The following queries are example of how you would use the `dive_sites_db` to find a dive site, wreck and/or obstruction and some history on that wreck/obstruction: 

* First connect to your MongoDB by typing the command `mongo` right in your command line 
* Then, you'll want to specify that you want to make queries from the dive_site_db so type `use dive_site_db` and hit enter and you'll be ready to start making some queries!

You know you want to see the wreck “FRENCH KISS” on your trip so you make the following query:

          > db.wrecks_obstructs.find({"Vessel Terms": "FRENCH KISS"}).pretty()

Which returns 

               {
	       "_id" : ObjectId("5fcb9cb168d692e78046b217"),
	       "Record #" : "9770",
       		"Vessel Terms" : "FRENCH KISS",
	       "Feature Type" : "Wreck - Submerged, dangerous to surface navigation",
	       "Lat" : "18.330839",
	       "Lng" : "-64.933231",
	       "GP Quality" : "High"
       		}


#### Status #### 
This project is *in progress*.

#### Contacts #### 
[Tyler Brown](https://github.com/Starcode897)  
[William Rosen](https://github.com/wrosen07)  
[Buddy Slater](https://github.com/jtslater2)  
[Jessy Thomas](https://github.com/jethomas2020)  
[Chloe Veras](https://github.com/cveras33)
