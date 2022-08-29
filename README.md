For information on how to create the model, refer my other repository "[English Topic Model](https://github.com/arnav-deep/EnglishTopicModel)".

# Dataset
The dataset used is taken from Kaggle and can be found [here](https://www.kaggle.com/jrobischon/wikipedia-movie-plots).

# Preprocess dataset
The dataset is required to be preprocessed. This is done through the python script [movie_lda_bow.py](https://github.com/arnav-deep/MovieRecommendation/blob/master/movie_lda_bow.py). This outputs a gensim lda2bow which is a txt file storing values of the probability distribution value of its topic which has been assigned to every word in the dataset.<br>
Probabilty distribution value between two plots can be calculated using Jensen-Shannon Divergence.<br>
Output of this script, the lda2bow data, is stored in [model_ldabow.txt](https://github.com/arnav-deep/MovieRecommendation/blob/master/movie_ldabow.txt)

# Method to get recommendations
I have created two different methods to get recommendations. 

Note: The CSV method is computationaly very heavy, so that's not recommended unless being used for production. It takes around 27 hours for 1000 movies and our movie dataset contains over 35,000 movies.

## A. Directly from terminal
Video showing how this method works can be found [here](https://drive.google.com/open?id=1zKI9-WiZsM4FT4043dBx4PGDZ4NXI4As).

The python script, [get_rec.py](https://github.com/arnav-deep/MovieRecommendation/blob/master/get_rec.py) has been written to get recommendations. It can be run and tested by giving movie tiltes present in the dataset as input.<br>
Note: You can get the movies present in the dataset from [movie_titles.txt](https://github.com/arnav-deep/MovieRecommendation/blob/master/movie_titles.txt) or you can run simply run [get_rec.py](https://github.com/arnav-deep/MovieRecommendation/blob/master/get_rec.py) and the terminal will help you get the movie titles.
```python
python get_rec.py
```
Instructions to use the script can be found in the terminal when script is run.

## B. Save it to CSV
Model takes words as input. Each word of an input data must be fed. The code can be found in [movie_rec_csv.py](https://github.com/arnav-deep/MovieRecommendation/blob/master/movie_rec_csv.py). This outputs a CSV with movie title and its top 50 recommendations in order.<br>
Note: Dataset must be downloaded before running this script. The output CSV after running this script for i=100 movies is already stored in [movie_recommendation.csv](https://github.com/arnav-deep/MovieRecommendation/blob/master/movie_recommendation.csv).

# What more can be done
1. Any other Dataset can be taken, just like the movie dataset is taken and used to get recommendations.<br>
The procedure will be very simple and the steps to be followed will be the same as that of this movie recommendation.<br>

2. A movie plot in the form of a string can be input in get_rec.py and the model can be run on it to get recommendations from the data.<br>

3. A website can be based using this model, but using the CSV method will be better and give fast results.

## License
GNU GENERAL PUBLIC LICENSE Version 2

Arnav Deep © June 2020. All rights reserved.
