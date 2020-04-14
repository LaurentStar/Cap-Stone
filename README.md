# Detecting Fake News for Donald Trump
Donald Trump has pointed out a lingering issues in media, the publication of fake news. I decided to take on his issue with media reliability by creating a model that is capable of detecting if a news story is fake or real.

## Summary Contents
* [Data](https://github.com/LaurentStar/Cap-Stone/tree/master/data) - The data sources used in this project and all cleaned/prepared data sets
* [Vectorizer](https://github.com/LaurentStar/Cap-Stone/blob/master/vectorizer.pkl) - This is a python object I used to quickly vectorize articles to be feed into my obejct.
* [Prepare Data](https://github.com/LaurentStar/Cap-Stone/blob/master/prep.ipynb) - I prepare cleaned data, I feature select/extend any columns I need, I scrap additional data using the urls initially provided and concatanated everything into one final dataframe.
* [Master](https://github.com/LaurentStar/Cap-Stone/blob/master/master.ipynb) - I perform all my modeling in master using the final data frame from the prep.ipynb notebook. The final dataframe was too big to put on git hub
* [Final Model](https://github.com/LaurentStar/Cap-Stone/blob/master/final_model.pkl) - The final model is saved for usage in the web application. 
* [EDA](https://github.com/LaurentStar/Cap-Stone/blob/master/exploratory_data_analysis.ipynb) - Exploring the data to see what I'm working with.
* [Cleaning](https://github.com/LaurentStar/Cap-Stone/blob/master/cleaning.ipynb) - Cleaning the data removing all null values and parsing all observations into a finalized form
* [Scripts](https://github.com/LaurentStar/Cap-Stone/tree/master/scripts) Scripts built to scrape websites or other supportive task that would be too slow in jupyter notebooks
* [Image](https://github.com/LaurentStar/Cap-Stone/tree/master/image) - Presentation material

## Try the web app
https://i-found-you-faker.herokuapp.com/
