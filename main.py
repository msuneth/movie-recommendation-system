import pandas as pd

movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')
credits = pd.read_csv('credits.csv')

m = movies['vote_count'].quantile(0.9)
print(m)
C = movies['vote_average'].mean()
print(C)
movies_filtered = movies.copy().loc[movies['vote_count'] >= m]


def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v / (v + m) * R) + (m / (m + v) * C)


movies_filtered['weighted_rating'] = movies_filtered.apply(weighted_rating, axis=1)
movies_filtered = movies_filtered.sort_values('weighted_rating', ascending=False)
selected_columns = ['title','weighted_rating']
print(movies_filtered[selected_columns])
