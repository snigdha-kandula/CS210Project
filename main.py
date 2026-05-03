import pandas as pd

#reading data from public Yelp dataset
business_df = pd.read_json("yelp_academic_dataset_business.json", lines=True)

##narrowing to just restaurants
restaurants = business_df[business_df["categories"].str.contains("Restaurants", na=False)]

print("Number of restaurants:", len(restaurants))
#print(restaurants[["state"]].value_counts().head(20)) - used to find state with most restaurants

#narrowing to Philadelphia, PA restaurants because weather data trends would be easier to gauge
pa_restaurants = restaurants[(restaurants["city"] == "Philadelphia") & (restaurants["state"] == "PA")].copy()

#cleaning
pa_restaurants = pa_restaurants.dropna(subset=["business_id"])
pa_restaurants["categories"] = pa_restaurants["categories"].fillna("")
pa_restaurants = pa_restaurants[["business_id", "name", "latitude", "longitude", "stars", "review_count", "categories"]]

print("Number of Philadelphia, PA restaurants:", len(pa_restaurants))
print(pa_restaurants[["business_id", "name", "categories", "stars", "review_count"]].head())

#getting Yelp review data
reviews_df = pd.read_json("yelp_academic_dataset_review.json", lines=True, nrows=600000)

print("Number of reviews:", len(reviews_df))
print(reviews_df.head())

#getting Philadelphia, PA reviews
pa_reviews = reviews_df[reviews_df["business_id"].isin(pa_restaurants["business_id"])].copy()

#cleaning
pa_reviews = pa_reviews.dropna(subset=["review_id", "business_id", "date"])
pa_reviews["date"] = pd.to_datetime(pa_reviews["date"]).dt.date
pa_reviews = pa_reviews[["review_id", "business_id", "user_id", "stars", "date", "useful", "funny", "cool"]]

print("Number of Philadelphia, PA restaurant reviews:", len(pa_reviews))
print(pa_reviews.head())

#check the years to see how much yearly data is included
print("Date range:", pa_reviews["date"].min(), "to", pa_reviews["date"].max())
print("Reviews per year:\n", pd.to_datetime(pa_reviews["date"]).dt.year.value_counts().sort_index())

#filter to after yelp gaining popularity and before covid
pa_reviews = pa_reviews[(pd.to_datetime(pa_reviews["date"]).dt.year >= 2013) & (pd.to_datetime(pa_reviews["date"]).dt.year <= 2019)]
print("Reviews after year filter:", len(pa_reviews))

#get rid of any duplicate reviews
before = len(pa_reviews)
pa_reviews = pa_reviews.drop_duplicates(subset=["review_id"])
after = len(pa_reviews)
print(f"Duplicates removed: {before - after}")

#filter to restaurants with more than 10 reviews
review_counts = pa_reviews["business_id"].value_counts()
active_ids = review_counts[review_counts >= 10].index
pa_reviews = pa_reviews[pa_reviews["business_id"].isin(active_ids)]
pa_restaurants = pa_restaurants[pa_restaurants["business_id"].isin(active_ids)]

print("Active restaurants:", len(pa_restaurants))
print("Filtered reviews:", len(pa_reviews))

#daily demand
daily_demand = (pa_reviews.groupby(["business_id", "date"]).size().reset_index(name="daily_review_count"))

print("Daily demand rows:", len(daily_demand))
print(daily_demand.head())


#weather data
weather_df = pd.read_csv("open-meteo-philadelphia-weather.csv", skiprows=3)

print(weather_df.head())
print(weather_df.columns)
print("Weather rows:", len(weather_df))

weather_df = weather_df.rename(columns={
    "time": "weather_date",
    "temperature_2m_max": "temp_max",
    "temperature_2m_mean": "temp_avg",
    "temperature_2m_min": "temp_min",
    "weather_code (wmo code)": "weather_code",
    "precipitation_sum (inch)": "precipitation"
})

weather_df["weather_date"] = pd.to_datetime(weather_df["weather_date"]).dt.date

weather_df = weather_df[["weather_date", "temp_max", "temp_avg", "temp_min", "weather_code", "precipitation"]]

#check to see if any null values (shouldn't be)
weather_df = weather_df.dropna(subset=["weather_date", "temp_avg", "precipitation"])

#check to make sure weather matches reviews date range
print("Date range:", weather_df["weather_date"].min(), "to", weather_df["weather_date"].max())
print("Missing values:\n", weather_df.isnull().sum()) #confirmed no null

# create csv files
pa_restaurants.to_csv("restaurants.csv", index=False)
pa_reviews.to_csv("reviews.csv", index=False)
daily_demand.to_csv("daily_demand.csv", index=False)
weather_df.to_csv("filtered_pa_weather.csv", index=False)