answer = input("お名前は？")

with open("answer.txt", "w", encoding="utf-8") as f:
    f.write(answer)
