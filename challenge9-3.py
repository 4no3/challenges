import csv

lis = [["Top Gun", "The Revenant", "Minority Report"],
       ["Titanic", "The Revenant", "Inception"],
       ["Training Day", "Man of Fire", "Flight"]]
# newline パラメータは、windows で必要
with open("answer9-3.csv", "w", newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for char in lis:
        w.writerow(char)

lis2 = [["トップガン", "レベナント", "マイノリティリポート"],
        ["タイタニック", "レベナント", "インセプション"],
        ["トレーニングデイ", "マンオブファイア", "フライト"]]
with open("answer9-4.csv", "w", newline='', encoding="utf-8") as f:
    w = csv.writer(f, delimiter=",")
    for char in lis2:
        w.writerow(char)

movies = [["Top Gun", "Risky Business", "Minority Report"],
          ["Titanic", "The Revenant", "Inception"],
          ["Training Day", "Man on Fire", "Flight"]]

with open("movies.csv", "w") as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=",")
    for movie_list in movies:
        spamwriter.writerow(movie_list)
