
---

#### **3️⃣ `data_preprocessing.py` (Cleaning & Feature Engineering)**
```python
import pandas as pd

# Load Data
train = pd.read_csv("data/train.csv")
train_label = pd.read_csv("data/train_label.csv")

# Combine datasets
train["Total_Booking"] = train_label["Total_Booking"]

# Feature Engineering
train["date"] = pd.to_datetime(train["datetime"]).dt.date
train["hour"] = pd.to_datetime(train["datetime"]).dt.hour
train["weekday"] = pd.to_datetime(train["datetime"]).dt.day_name()

# Save cleaned data
train.to_csv("data/train_cleaned.csv", index=False)

