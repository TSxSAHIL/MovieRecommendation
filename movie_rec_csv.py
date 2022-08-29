import numpy as np
import pandas as pd
import pickle
import time

from gensim.matutils import jensen_shannon

np.seterr(divide='ignore', invalid='ignore')

df_input = pd.read_csv('../Datasets/wiki_movie_plots_deduped.csv')

titles = df_input.Title

with open("movie_ldabow.txt", "rb") as fp:
    lda_bow = pickle.load(fp)

df_res = pd.DataFrame({"title": [],
                       "rec": []})

df_title = pd.DataFrame({"title": [],
                         "dist": []})

for i in range(34, len(titles)):
    df_title.empty
    df_curr = pd.DataFrame({"title": [titles[i]]})
    start = time.time()
    for j in range(len(lda_bow)):
        if j != i:
            dst = jensen_shannon(lda_bow[i], lda_bow[j], 130)
            df_individual = pd.DataFrame({"title": [titles[j]],
                                          "dist": [dst]})
            df_title = df_title.append(df_individual, ignore_index=True)

    df_title = df_title.sort_values(by=['dist'])
    df_rec = pd.DataFrame({"rec": [df_title['title'][0:50]]})
    rec = df_rec["rec"][0].tolist()
    df_rec = pd.DataFrame({"rec": [rec]})
    df_ind_res = pd.merge(df_curr, df_rec, left_index=True, right_index=True, how='inner')
    df_res = df_res.append(df_ind_res, ignore_index=True)
    if i == 0:
        df_ind_res.to_csv('movie_recommendation.csv', index=False)
    else:
        df_ind_res.to_csv('movie_recommendation.csv', mode='a', index=False, header=False)
    if i == 99:  # remove this or change this as requirement | Here i is number of movies in CSV
        break
    end = time.time()
    print(i, end - start)


