import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#https://censusindia.gov.in/census.website/data/census-tables
# Load the data from the specified file path
df = pd.read_csv(r'D:\Desktop\PYTHONDATASET.csv')
print(df.head());
#print(df.desicribe());
# Clean column names: strip spaces, replace spaces with underscores, and remove trailing periods
df.columns = df.columns.str.strip().str.replace(" ", "_").str.rstrip(".")

# Strip leading/trailing spaces from the "Name" column
df["Name"] = df["Name"].str.strip()

# Convert data types: remove commas and convert to integers for specific columns

# Convert "Area" to float and "Population_per_sq_km" to float
df["Area"] = df["Area"].astype(float)
df["Population_per_sq_km"] = df["Population_per_sq_km"].astype(float)

# Check for missing values
print("Missing values:\n", df.isnull().sum())
# If there are missing values, you can handle them accordingly (e.g., df.dropna(inplace=True))

# Consistency check for India (optional but recommended)
india_total = df[(df["Region"] == "INDIA") & (df["Area_type"] == "Total")]["Population_Persons"].iloc[0]
india_rural = df[(df["Region"] == "INDIA") & (df["Area_type"] == "Rural")]["Population_Persons"].iloc[0]
india_urban = df[(df["Region"] == "INDIA") & (df["Area_type"] == "Urban")]["Population_Persons"].iloc[0]
print(f"Consistency check for India: Total={india_total}, Rural+Urban={india_rural + india_urban}")

# Objective 1: Population Distribution Across States
states_total = df[(df["Region"] == "STATE") & (df["Area_type"] == "Total")]
states_total = states_total.sort_values("Population_Persons", ascending=False)
plt.figure(figsize=(12, 8))
plt.barh(states_total["Name"], states_total["Population_Persons"])
plt.xlabel("Population")
plt.ylabel("State")
plt.title("Population Distribution Across States")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.show()

# Objective 2: Urban vs Rural Population for Each State
states_rural_urban = df[(df["Region"] == "STATE") & (df["Area_type"].isin(["Rural", "Urban"]))]
pivot = states_rural_urban.pivot(index="Name", columns="Area_type", values="Population_Persons")
pivot.plot(kind="bar", stacked=True, figsize=(12, 8))
plt.xlabel("State")
plt.ylabel("Population")
plt.title("Urban vs Rural Population for Each State")
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Objective 3: Population Density Across Districts (Top 10)
districts_total = df[(df["Region"] == "DISTRICT") & (df["Area_type"] == "Total")]
top10_density = districts_total.nlargest(10, "Population_per_sq_km")
plt.figure(figsize=(10, 6))
plt.bar(top10_density["Name"], top10_density["Population_per_sq_km"])
plt.xlabel("District")
plt.ylabel("Population Density (per sq km)")
plt.title("Top 10 Districts by Population Density")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

# Objective 4: Gender Ratio Across States
states_total = df[(df["Region"] == "STATE") & (df["Area_type"] == "Total")].copy()
states_total["Gender_Ratio"] = (states_total["Population_Females"] / states_total["Population_Males"]) * 1000
plt.figure(figsize=(12, 8))
plt.bar(states_total["Name"], states_total["Gender_Ratio"])
plt.axhline(y=1000, color="r", linestyle="--", label="Equal Ratio")
plt.xlabel("State")
plt.ylabel("Gender Ratio (Females per 1000 Males)")
plt.title("Gender Ratio Across States")
plt.xticks(rotation=90)
plt.legend()
plt.tight_layout()
plt.show()

# Objective 5: Relationship Between Households and Population for Sub-Districts
sub_districts = df[df["Region"] == "SUB-DISTRICT"]
plt.figure(figsize=(10, 6))
sns.scatterplot(data=sub_districts, x="Number_of_households", y="Population_Persons", hue="Area_type")
plt.xlabel("Number of Households")
plt.ylabel("Population")
plt.title("Relationship Between Households and Population in Sub-Districts")
plt.tight_layout()
plt.show()

india_rural_urban = df[(df["Region"] == "INDIA") & (df["Area_type"].isin(["Rural", "Urban"]))]
labels = ["Rural", "Urban"]
sizes = [india_rural, india_urban]
plt.figure(figsize=(8, 8))
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90, colors=["#66b3ff", "#ff9999"])
plt.title("Proportion of Urban vs Rural Population in India")
plt.axis("equal")  # Equal aspect ratio ensures pie is circular
plt.tight_layout()
plt.show()

sub_districts_subset = sub_districts[["Population_Persons", "Number_of_households", "Area", "Population_per_sq_km"]]
plt.figure(figsize=(10, 10))
sns.pairplot(sub_districts_subset)
plt.suptitle("Pair Plot of Population, Households, Area, and Density in Sub-Districts", y=1.02)
plt.tight_layout()
plt.show()
# 7. Histogram: Distribution of Population Density Across Sub-Districts
plt.figure(figsize=(10, 6))
plt.hist(sub_districts["Population_per_sq_km"], bins=30, edgecolor="black")
plt.xlabel("Population Density (per sq km)")
plt.ylabel("Number of Sub-Districts")
plt.title("Distribution of Population Density Across Sub-Districts")
plt.tight_layout()
plt.show()