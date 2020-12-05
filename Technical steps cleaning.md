Technical steps for cleaning and providing data for dive sites project.



1. Identify source of data - Using a google search, we were able to find the National Oceanic and Atmospheric Administration website which has links to the Automated Wreck and Obstruction Information System (AWOIS) files.  We chose to use the Excel files of the AWOIS Wrecks and the AWOIS Obstructions.

2. Examining the data - Since the files were native Excel documents, we were able to open the files and start examining "what's in here".  ((screens shots below - wrecks first then obstructions))

   ​	

3. The first thing was the files had the same layout.  Same columns and names so whatever we did with the first file we could apply to the second file.  The next step was to see if there was any data that was not needed for our project.  The columns "DEPTH", "SOUNDING_TYPE" and "YEARSUNK" were filled in less that 50 percent of the time so we chose to remove this data.  The "RECRD" column was found to be a unique number across both files so we were able to keep this as a id number going forward.  "VESSLTERMS","FEATURE_TYPE","LATDEC", "LONGDEC" were kept.  These are the backbone of what we wanted from this data source.  "GP_QUALITY" proved to be an interesting data point.   With values of "High", "Med", "Low" and "Poor", this describes the quality of the lat/long location information.  This was thought to be useful for our project so it was kept.  "HISTORY" was a free-form notes field with useful information but was not formatted well.  We chose to keep it in a separate chart with the RECRD field to be able to access this information

4. Using Jupyter Notebook, we imported the csv files into a dataframe and dropped the unwanted columns.  We created the History dataframe and exported it to history csv file and dropped the history column from the original dataframe.  We renamed the columns and exported the clean data to the csv file.