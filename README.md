# Data-Cleaning-and-Analysis-of-Movie-Ratings-City-Temperatures

This exercise focuses on developing skills in data analysis, visualization, and entity resolution using Python. It involves two main tasks:

Movie Title Entity Resolution - Cleaning and matching movie titles for accurate rating aggregation.

Cities: Temperatures and Density - Analyzing correlations between population density and temperature using real-world datasets.

🎬 Movie Title Entity Resolution

Objective

Given a list of correctly spelled movie titles and a dataset with user-provided (often misspelled) ratings, the goal is to match the ratings to the correct movies and compute the average rating for each movie.

📂 Input Files

movie_list.txt: Contains the correctly spelled movie titles, one per line.

movie_ratings.csv: Contains movie titles (which may be misspelled) along with user ratings.

🛠 Process

Match misspelled titles to the correct ones using difflib.get_close_matches.

Ignore completely incorrect titles that do not match anything in movie_list.txt.

Compute average ratings for each correctly matched movie.

Sort results alphabetically by movie title.

🚀 Running the Script

python3 average_ratings.py movie_list.txt movie_ratings.csv output.csv

📊 Output Format (CSV)

title,rating
Bad Moms,8.0
Gone in Sixty Seconds,6.75

🏙️ Cities: Temperatures and Density

Objective

Analyze whether there is a correlation between population density and average maximum temperature in cities by matching city data with weather station data.

📂 Input Files

stations.json.gz: Line-by-line compressed JSON file containing weather station data.

city_data.csv: Contains city names, population, and area details.

🛠 Process

Data Cleaning:

Remove cities with missing population or area.

Convert area from m² to km² and exclude cities with an area > 10,000 km².

Match Cities to Weather Stations:

Use latitude/longitude to find the nearest weather station.

Extract avg_tmax (average maximum temperature) from the closest station.

Compute Population Density:

Density = Population / Area (people per km²).

Generate a Scatterplot

Plot Avg Max Temperature (°C) vs. Population Density (people/km²).

🚀 Running the Script

python3 temperature_correlation.py stations.json.gz city_data.csv output.svg

📊 Output: Scatterplot

X-axis: Population Density (people/km²)

Y-axis: Avg Max Temperature (°C)

Output file: output.svg

📜 Entity Resolution Methods

String Matching: difflib.get_close_matches for movie title correction.

Geospatial Matching: Finding the closest station to a city using latitude/longitude.

Performance Optimization: Using Pandas’ vectorized operations and NumPy’s efficient calculations.
