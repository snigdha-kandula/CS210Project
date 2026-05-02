import pandas as pd

business_df = pd.read_json(
    "yelp_academic_dataset_business.json",
    lines=True,
    nrows=10000
)

restaurants = business_df[
    business_df["categories"].str.contains("Restaurants", na=False)
]

print("Number of restaurants:", len(restaurants))
print(restaurants[["business_id", "name", "city", "state", "categories"]].head())

reviews_df = pd.read_json(
    "yelp_academic_dataset_review.json",
    lines=True,
    nrows=50000
)

print("Number of reviews:", len(reviews_df))
print(reviews_df.head())

merged = reviews_df.merge(
    restaurants[["business_id", "name", "city", "state"]],
    on="business_id",
    how="inner"
)

print("Merged rows:", len(merged))
print(merged.head())

merged["date"] = pd.to_datetime(merged["date"]).dt.date

daily_demand = (
    merged.groupby(["business_id", "name", "city", "state", "date"])
    .size()
    .reset_index(name="daily_review_count")
)

print(daily_demand.head())
print("Daily demand rows:", len(daily_demand))