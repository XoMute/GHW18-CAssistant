from algo import *
from postReq import *


def mainParams(text):
    
    post = PostRequest(text)

    k_extraversion   = 0.25  #1
    k_emotional      = 0.25  #2
    k_animals        = 0.25  #3
    k_egocentrism    = 0.25  #4
    k_manipulate     = 0.25  #5
    k_empathy        = 0.25  #6
    k_intelligence   = 0.25  #7
    k_nonNormalLexic = 0.25  #8
    k_direct_words   = 0.25  #9



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
        smiles(text)            * (-k_emotional) + nosea                *k_intelligence,
        #aggresive    =
        animals_words(text)     * k_animals      + nonNormalLexic(text) *k_nonNormalLexic   + direct_words(text)*k_direct_words,
        #manipulate   =
        questions(text)         * k_manipulate,
        #egocentrism  =
        me_in_text(text)        * k_egocentrism
        )
    

def NIKITA(text):
    return mainParams(text)
