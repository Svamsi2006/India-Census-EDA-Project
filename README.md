# India-Census-EDA-Project
# India Demographic Data Analysis

This project analyzes demographic data for India, focusing on population statistics across states, districts, and sub-districts. Using Python, I cleaned the dataset, performed exploratory data analysis (EDA), and created seven insightful visualizations to uncover trends in population distribution, urbanization, density, gender ratios, and more.

## Table of Contents
- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Data Cleaning](#data-cleaning)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Visualizations](#visualizations)
- [Requirements](#requirements)
- [How to Run](#how-to-run)
- [File Structure](#file-structure)
- [Future Improvements](#future-improvements)
- [License](#license)

## Project Overview
The goal of this project is to explore India's demographic data to understand population patterns, urban-rural divides, and other key metrics. The dataset includes hierarchical data (India, states, districts, sub-districts) with details like population, households, area, and density. Through data cleaning and EDA, I generated visualizations to highlight insights, such as the most populous states, high-density districts, and relationships between variables.

This project was developed to showcase my skills in:
- Data cleaning with Pandas
- Exploratory data analysis
- Data visualization with Matplotlib and Seaborn
- Python programming

## Dataset
The dataset (`PYTHONDATASET.csv`) contains demographic statistics for India, structured as follows:
- **Columns**:
  - `State_Code`, `District_Code`, `Sub_District_Code`: Identifiers for regions
  - `Region`: Level of data (INDIA, STATE, DISTRICT, SUB-DISTRICT)
  - `Name`: Region name
  - `Area_type`: Total, Rural, or Urban
  - `No_of_villages_Inhabited`, `No_of_villages_Uninhabited`: Village counts
  - `Number_of_households`: Household count
  - `Population_Persons`, `Population_Males`, `Population_Females`: Population counts
  - `Area`: Area in square kilometers
  - `Population_per_sq_km`: Population density
- **Source**: Not publicly shared due to privacy; replace with your own CSV with similar structure to run the code.

## Data Cleaning
The dataset required several cleaning steps to ensure accuracy:
- **Column Names**: Removed spaces, underscores, and trailing periods (e.g., "No_of _villages_Uninhabited" → "No_of_villages_Uninhabited").
- **Whitespace**: Stripped spaces from the `Name` column for consistent filtering.
- **Data Types**:
  - Removed commas from numeric columns (e.g., population, households) and converted to integers.
  - Converted `Area` and `Population_per_sq_km` to floats.
- **Consistency Check**: Verified that India's total population equals the sum of rural and urban populations.
- **Missing Values**: Checked for nulls (none found in the sample, but code handles them if present).

## Exploratory Data Analysis
EDA focused on understanding population trends and relationships:
- Analyzed population distribution across states and districts.
- Compared urban and rural populations to assess urbanization.
- Examined population density to identify high-density areas.
- Calculated gender ratios (females per 1000 males) for states.
- Explored correlations between households, population, area, and density at the sub-district level.

## Visualizations
The project includes seven visualizations, saved as PNG files:
1. **Population Distribution Across States**: Horizontal bar chart of total population per state.
2. **Urban vs Rural Population**: Stacked bar chart comparing urban and rural populations by state.
3. **Top 10 Districts by Population Density**: Bar chart of the most densely populated districts.
4. **Gender Ratio Across States**: Bar chart of female-to-male ratios with a reference line at 1000.
5. **Households vs Population**: Scatter plot for sub-districts, colored by area type.
6. **Pair Plot**: Scatterplot matrix of population, households, area, and density for sub-districts.
7. **Urban vs Rural Population Share**: Pie chart showing India's urban vs rural population proportions.

Visualizations are stored in the `visualizations/` folder.

## Requirements
To run this project, install the following Python libraries:
```bash
pip install pandas matplotlib seaborn
