#!/usr/bin/env python3

import sys
import random

articles = ["a", "the", "another", "some"]
subjects = ["boy", "girl", "man", "women", "dog", "cat", "monkey", "dinosaur", "alien"]
verbs = ["sang","ran","jumped","hit","kissed"]
adverbs = ["beautifully","badly","well","loudly","quietly","abruptly","elegantly"]

lines = 5
if len(sys.argv)>1:
    try:
        temp = int(sys.argv[1])
        if 1<= temp <= 10:
            lines = temp
        else:
            print("The poem must consist of 1 to 10 lines")
    except ValueError:
        print("Usage: badpoetry.py [number of lines]")

while lines:
    article = random.choice(articles)
    subject = random.choice(subjects)
    verb = random.choice(verbs)
    adverb = random.choice(adverbs)

    structure = random.randint(1,2)
    if structure == 1:
        print(article, subject, verb, adverb)
    if structure == 2:
        print(article, subject, verb)
    lines -= 1
