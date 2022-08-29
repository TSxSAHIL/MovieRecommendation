import random
import numpy as np
import pandas as pd
import pickle

from gensim.matutils import jensen_shannon

np.seterr(divide='ignore', invalid='ignore')

df_input = pd.read_csv('../Datasets/wiki_movie_plots_deduped.csv')

titles = df_input.Title

title_list = df_input["Title"].tolist()

with open("movie_ldabow.txt", "rb") as fp:
    lda_bow = pickle.load(fp)

file = open('movie_titles.txt', "r", encoding="utf8")
lines = file.read()
lines = lines.split("\n")
data_titles = []
i = 0
for line in lines:
    data_titles.append(line)
    i += 1

start = random.randint(0, i - 20)
end = start + 20

print("Enter movie title copied from movie_titles.txt or copy tem from below\n" +
      "Some random examples are: %s \n" % (data_titles[start:end]))

while True:
    check = input("Insert:\n" +
                  "-->'1' to get a random movie and it's recommendation\n" +
                  "-->'2' to see some of the titles in the dataset\n" +
                  "-->'3' or 'STOP' to end sequence\n" +
                  "-->Title copied from dataset\n" +
                  "Input: ")

    df_res = pd.DataFrame({"title": [],
                           "rec": []})

    df_title = pd.DataFrame({"title": [],
                             "dist": []})

    if check == '1':
        num = random.randint(0, i - 25)
        print("Getting recommendations. Please wait\n")
        df_curr = pd.DataFrame({"title" : [titles[num]]})
        for j in range(len(lda_bow)):
            if j != num:
                dst = jensen_shannon(lda_bow[num], lda_bow[j], 130)
                df_individual = pd.DataFrame({"title": [titles[j]],
                                              "dist": [dst]})
                df_title = df_title.append(df_individual, ignore_index=True)

        df_title = df_title.sort_values(by=['dist'])
        df_rec = pd.DataFrame({"rec": [df_title['title'][0:50]]})
        rec = df_rec["rec"][0].tolist()
        title = titles[num]
        rec = rec[0:10]
        print("Movie: %s\nTop 10 Recommendations: %s" % (title, rec))

    elif check == '2':
        start = random.randint(0, i - 20)
        end = start + 20
        print("Some random examples are: %s \n" % (data_titles[start:end]))

    elif check == 'STOP' or check == '3':
        print("============================================> Terminating\nThank you for using")
        break

    else:
        title = check
        if title in title_list:
            print("Getting recommendations. Please wait\n")
            num = title_list.index(title)
            df_curr = pd.DataFrame({"title": [titles[num]]})
            for j in range(len(lda_bow)):
                if j != num:
                    dst = jensen_shannon(lda_bow[num], lda_bow[j], 130)
                    df_individual = pd.DataFrame({"title": [titles[j]],
                                                  "dist": [dst]})
                    df_title = df_title.append(df_individual, ignore_index=True)

            df_title = df_title.sort_values(by=['dist'])
            df_rec = pd.DataFrame({"rec": [df_title['title'][0:50]]})
            rec = df_rec["rec"][0].tolist()
            title = titles[num]
            rec = rec[0:10]
            print("Movie: %s\nTop 10 Recommendations: %s\n" % (title, rec))

        else:
            print("Error: Wrong input or Movie title does not match dataset.\n" +
                  "Please check or use 1 to get random recommendations\n")

