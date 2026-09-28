# 16. Python Pandas Exercise

# Excercise 1: basic operation of pandas
import pandas as pd
import numpy as np

# Load Iris dataset
df = pd.read_csv("iris_data.csv")
print(df.head())

df = df.drop("Id", axis=1)
print(df.head())

# rename the column name
df = df.rename(columns={"SepalLengthCm": "sepal_length", "SepalWidthCm": "sepal_width", "PetalLengthCm": "petal_length", "PetalWidthCm": "petal_width"})
df["species"] = df["species"].str.replace("Iris-", "")
print(df.head())

# shape of the table
print(df.shape)

# how many different species are there?
print(df["species"].nunique())

# how many time each species is repeated in given dataset
print(df["species"].value_counts())

# how many rows are there whose sepal length is greater than its mean
print((df["sepal_length"] > df["sepal_length"].mean()).sum())
# 70 rows are there whose sepal length is greater than avg sepal length

# extract all the rows whose petal width is greater than 1.5 and petal length is lesser than 5
print(df[(df["petal_width"] > 1.5) & (df["petal_length"] < 5)])

# which species has highest sepal length
print(df["sepal_length"].max())
print(df[df["sepal_length"] == df["sepal_length"].max()])

# extract mean median of sepal lenth,sepal width ,petal lenth , petal width for all the species
print(df.groupby("species").agg(["mean", "median"]))


# Excercise 200
df = pd.read_csv("Automobile_data.csv", na_values={'price': ["?", "n.a"], 'stroke': ["?", "n.a"], 'horsepower': ["?", "n.a"], 'peak-rpm': ["?", "n.a"], 'average-mileage': ["?", "n.a"]})
print(df)

# Exercise 2: From the given dataset print the first and last five rows
print(df.head())

missing_value = ["?", "n.a", np.nan]
df = pd.read_csv("Automobile_data.csv", na_values=missing_value)
print(df.isnull().sum())

df = df.drop("index", axis=1)

# Exercise 3: Find the most expensive car company name
print(df["price"].max())

most_exp_car = df[["company", "price"]][df.price == df["price"].max()]
print(most_exp_car)

# Exercise 3: Print All Toyota Cars details
print(df.groupby("company").get_group("toyota"))

# Exercise 4: Count total cars per company
print(df["company"].value_counts())

# Exercise 5: Find each company’s Higesht price car
import warnings
warnings.filterwarnings("ignore")

print(df.groupby("company")[["company", "price"]].max())

# Exercise 6: Find the average mileage of each car making company
print(df.groupby("company")[["average-mileage"]].mean())

# Exercise 7: Sort all cars by Price column
print(df.sort_values("price", ascending=False))

# Exercise 8: Concatenate two data frames using the following conditions
GermanCars = {'Company': ['Ford', 'Mercedes', 'BMV', 'Audi'], 'Price': [23845, 171995, 135925, 71400]}
japaneseCars = {'Company': ['Toyota', 'Honda', 'Nissan', 'Mitsubishi '], 'Price': [29995, 23600, 61500, 58900]}

germanCar = pd.DataFrame.from_dict(GermanCars)
print(germanCar)

japaneseCar = pd.DataFrame.from_dict(japaneseCars)
print(japaneseCar)

carsDF = pd.concat([germanCar, japaneseCar], keys=["germany", "Japan"])
print(carsDF)

# Exercise 9: Merge two data frames using the following condition
Car_Price = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'Price': [23845, 17995, 135925, 71400]}
car_Horsepower = {'Company': ['Toyota', 'Honda', 'BMV', 'Audi'], 'horsepower': [141, 80, 182, 160]}

carPrice = pd.DataFrame.from_dict(Car_Price)
print(carPrice)

carHorsepower = pd.DataFrame.from_dict(car_Horsepower)
print(carHorsepower)

carsDF = pd.merge(carPrice, carHorsepower, on="Company")
print(carsDF)
