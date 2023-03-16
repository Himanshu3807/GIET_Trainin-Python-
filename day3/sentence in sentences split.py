#using for loop
sentences = ["a new world record was set",
             "in the holy city of ayodhya",
             "on the eve of diwali on tuesday",
             "with over three lakh diya or earthen lamps",
             "lit up simultaneously on the banks of the sarayu river"]
stopwords = ['for', 'a', 'of', 'the', 'and', 'to', 'in', 'on', 'with','was']
words = []
for sentence in sentences:
    sentence_words = sentence.split()# Split the sentence into words
    for word in sentence_words:      # Check if each word is a stop word or not
        if word not in stopwords:    # If the word is not a stopword, add it to the list of words
            words.append(word)
print(words)
#using list comprehension
words = [word for sentence in sentences for word in sentence.split() if word not in stopwords]
print(words)
