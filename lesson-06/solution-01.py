import collections

text = "Eдиный стиль оформления делает код понятным для самого программиста и его коллег с разным уровнем подготовки. " \
       "В идеале наиболее сложный фрагмент кода должен быть понятен с первого прочтения. " \
       "Это упрощает командную разработку и обучение новичков, позволяет вам быстро возвращаться к собственным давним проектам."
words = text.split()
counter = collections.Counter(words)
most_common, occurrences = counter.most_common()[0]
longest = max(words, key=len)
print(most_common, longest)
