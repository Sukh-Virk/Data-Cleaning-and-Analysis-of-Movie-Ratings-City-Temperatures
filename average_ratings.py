import pandas as pd
import difflib


filename1 = 'movie_list.txt'
filename2 = 'movie_ratings.csv'


movie_list = pd.read_csv(filename1, header=None, names=["title"])

def clean(movie_list):
    name= movie_list["title"] = movie_list["title"].str.strip().tolist()
    return name


titles = clean(movie_list)

rate = pd.read_csv(filename2)


import difflib

def matching(word):
    
    same = difflib.get_close_matches(word, titles, n=1, cutoff=0.6)

    if same:  
        return same[0] 
    else:  
        return None  





rate['matched'] = rate['title'].apply(matching)
rate= rate.dropna().copy()  


ratings = rate.groupby('matched', as_index=False)['rating'].mean()
ratings = ratings.round(2)

ratings.rename(columns={'matched': 'title', 'rating': 'avg_rating'}, inplace=True)


ratings.to_csv('output.csv', index=False)
