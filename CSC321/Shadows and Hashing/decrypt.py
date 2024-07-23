import nltk
import bcrypt
import time

nltk.download('words')

def main():
    wordList = nltk.corpus.words.words()
    validWords = [w for w in wordList if len(w) < 11 and len(w) > 5]
    hash = b'$2b$08$J9FW66ZdPI2nrIMcOxFYI.6B7jUcPdnqJz4tIUwKBu8lNMs5NdT9q'
    start = time.time()
    print(len(validWords))

    end = time.time()
    print('Time: ', end - start)

if __name__== "__main__":
    main()