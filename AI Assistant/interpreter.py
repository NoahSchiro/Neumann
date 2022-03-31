import nltk

class interpreter:

    # Takes a phrase and a key word. If phrase contains the 
    # keyword, the method tags what part of speech each word 
    # is in, and then returns a list of tuples containing 
    # the word and the part of speech
    @staticmethod
    def is_command(command, keyWord):

        # Break up phrase into list
        words = nltk.word_tokenize(command)

        # If the key word is present, then 
        # put in the work of tagging
        if keyWord in words:
            tagged_words = nltk.pos_tag(words)
            return tagged_words

if __name__ == "__main__":

    t_w = interpreter.is_command()

    print(t_w)

    # phrase = "The boy got the dog at the mall"
    # tagged = nltk.pos_tag(nltk.word_tokenize(phrase))
    # print(tagged)