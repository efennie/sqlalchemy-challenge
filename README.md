# sqlalchemy-challenge

The purpose of this code is to run through climate data collected at different climate collection stations in hawaii. The location information and full csv files are available under hawaii_measurements.csv and hawaii_stations.csv. The data is also located in the hawaii.sqlite file. 

Using SQLAlchemy and ORM, the data is imported and automapped within the climate_started.ipynb file. Each table is then referenced for later use within the jupyter notebook file. The code will pull the most recent 12 months of data from the tables and save the data as a dataframe.

Once the data is filtered, it will be plotted with matplotlib as a bar graph with Inches of Rain vs. Date collected. The figure will also be saved in the process. 

Some basic stats are then calculated to look at the filtered data. 

The stations are then further analyzed. A unique count is done to get an idea of which stations are the most active in their weather data collection. The most active station is then further queried.

The maximum temperature, average temperature, and the minimum temperature values are calculated and printed. The active station data is further filtered by the last 12 months of data collected. 

The active station's filtered data is then used to plot a histogram of Frequency of Temperature Observations.

Meanwhile...

Within the app.py file, you'll find different app routes for using Flask to remotely call on the weather data. There are routes that illustrate similar functions that were created within the climate_starter.ipynb file. The routes will show the station names and locations, all the precipitation data from all the stations, the temperature observations for one year from the most active station, and finally the querent may use the weatherstats app to choose a start and end date (within our range) and get the minimum, maximum, and average temperature observations within that date range.
