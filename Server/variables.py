from algo import *
from postReq import *


def mainParams(text):
    
    post = PostRequest(text)

    k_extraversion   = 1.47  #1
    k_emotional      = 1.23  #2
    k_animals        = 1.3  #3
    k_egocentrism    = 1.203  #4
    k_manipulate     = 1.1003  #5
    k_empathy        = 1.13  #6
    k_intelligence   = 1.22  #7
    k_nonNormalLexic = 1.25  #8
    k_direct_words   = 1.3200004  #9
    k_glossary       = 0.21        


    # All global variables
    # that describes circle toggle bars
    # 
    return (
        #extraversion
        me_in_text(text)        * k_extraversion,
        #emotional    =
        smiles(text)            * k_emotional,
        #empathy      =
        questions(text)         * k_empathy,
        #intelligence =
        smiles(text)            * (-k_emotional) + nosea*3.333             *k_intelligence + glossary * k_glossary,
        #aggresive    =
        animals_words(text)     * k_animals      + nonNormalLexic(text) *k_nonNormalLexic   + direct_words(text)*k_direct_words,
        #manipulate   =
        questions(text)         * k_manipulate   + direct_words(text)*k_direct_words,
        #egocentrism  = 
        me_in_text(text)        * k_egocentrism
        )
    

def NIKITA(text):
    return mainParams(text)
