# CS210Project

## Dataset

This project uses the Yelp Open Dataset:
https://business.yelp.com/data/resources/open-dataset/
Due to licensing restrictions, the dataset is not included in this repository.


Steps to Run Project:
1. Download these files to the same directory
   - Schema.sql, ml.py, main.py, open-meteo-philadelphia-weather.csv
   - Note that we used a larger version (5GB file) of the JSON files in our directories that we cannot upload to Codebench or GitHub due to copyright and size restrictions. 
   - We recommend following the instructions on GitHub to download the full dataset. If you do not want to download the datasets, then you do not need to run main.py, as we will attach the output CSV files from main.py for you to use in schema.sql. 
   - In this case, download daily_demand.csv, filtered_pa_weather.csv, restaurants.csv, and reviews.csv into the same directory.
2. Run these commands:
   - Python3 main.py (if you download the Yelp datasets and run this file)
   - sqlite3 cs210_restaurant_demand.db < schema.sql
         - this generated features.csv to be used for ml.py
   - python3 ml.py,


Note: if you download all the files (including csvs), running the code in main.py should overwrite the existing csv files

Video Link: https://www.youtube.com/watch?v=2hVCkeW24Y8
Presentation Link: https://docs.google.com/presentation/d/1oSzttgiO4H41CfwS60_tVgxkDLz6IGkUuQfZValNapM/edit?usp=sharing
