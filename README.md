# CS210Project

## Dataset

This project uses the Yelp Open Dataset:
https://business.yelp.com/data/resources/open-dataset/
Due to licensing restrictions, the dataset is not included in this repository.

To run this project:
1. Download the dataset from the link above
2. Place the following files in the same directory as main.py, ml.py, schema.sql:
   - yelp_academic_dataset_business.json
   - yelp_academic_dataset_review.json
3. Run "python3 main.py" to generate the daily_demand.csv, filtered_pa_weather.csv, restaurants.csv, reviews.csv
4. Run "sqlite3 cs210_restaurant_demand.db < schema.sql" to generate the features.csv file
5. Run python3 ml.py to see the findings from the three models and generate ml_results.png, ml_importance_random_forest.png, & ml_importance_xgboost.png

Note: if you download all the files (including csvs), running the code should overwrite the existing csv files
