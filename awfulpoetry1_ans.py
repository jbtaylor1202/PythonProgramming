#!/usr/bin/env python3

import random

articles = ["a", "the", "another", "some"]
subjects = ["boy", "girl", "man", "women", "dog", "cat", "monkey", "dinosaur", "alien"]
verbs = ["sang","ran","jumped","hit","kissed"]
adverbs = ["beautifully","badly","well","loudly","quietly","abruptly","elegantly"]

loop = 0
while loop < 5:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    structure = random.randint(1,2)
    if structure == 1:
        print(article, subject, verb, adverb)
    if structure == 2:
        print(article, subject, verb)
    loop += 1
