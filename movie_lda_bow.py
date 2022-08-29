import numpy as np
import pandas as pd
import pickle

from gensim.corpora import Dictionary
from gensim.test.utils import datapath
from gensim.models.ldamodel import LdaModel
from gensim.models import TfidfModel
from gensim.matutils import jensen_shannon
from gensim.corpora import Dictionary, HashDictionary, MmCorpus, WikiCorpus
from gensim.parsing.preprocessing import remove_stopwords, preprocess_string, strip_non_alphanum, strip_numeric, \
    strip_short

np.seterr(divide='ignore', invalid='ignore')

df_input = pd.read_csv('../Datasets/wiki_movie_plots_deduped.csv')

titles = df_input.Title
plots_raw = df_input.Plot
links = df_input.Wikilink

plots = []
for plot in plots_raw:
    temp = plot.lower()
    temp = strip_non_alphanum(temp)
    temp = strip_numeric(temp)
    temp = remove_stopwords(temp)
    temp = strip_short(temp)
    temp = preprocess_string(temp)
    plots.append(temp)

model_location = datapath("D:/HazMat/Projects/ML/Models/model_130")  # add complete path here
model = LdaModel.load(model_location)

bow_plot = []
lda_bow = []
for plot in plots:
    bow_plot.append(model.id2word.doc2bow(plot))

for bow in bow_plot:
    lda_bow.append(model[bow])

with open("movie_ldabow.txt", "wb") as fp:
    pickle.dump(lda_bow, fp)
