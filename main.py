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
