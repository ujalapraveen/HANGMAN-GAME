import string
import random

def load_words():
    """
    Ye function kaafi jayada words ko load karne mai help karega 
    """

    with open("words.txt","r") as file1:
        data= file1.read().split()
        i=0
        while i<len(data):
            # print(data[i])
            i=i+1
        return data

   
def choose_word():
    """
    word_list (list): list of words (strings)
    ye function ek word randomly return karega
    """
    
    word_list = load_words()
    secret_word = random.choice(word_list)
    secret_word = secret_word.lower()
    return secret_word 
choose_word()