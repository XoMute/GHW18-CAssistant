from algo import *
from postReq import *
import random

def mainParams(text):
    
    post = PostRequest(text)

    k_extraversion   = 1.40001 - random.betavariate(random.random()*100, random.random()*100)  
    k_emotional      = 1.200123 - random.betavariate(random.random()*100, random.random()*100)+ random.uniform(0.0001, 0.19)   #2
    k_animals        = 1.10641293  - random.betavariate(random.random()*100, random.random()*100)+ random.uniform(0.0001, 0.19)  #3
    k_egocentrism    = 1.18303129 - random.betavariate(random.random()*100, random.random()*100) + random.uniform(0.0001, 0.19)   #4
    k_manipulate     = 1.1003023192 - random.betavariate(random.random()*100, random.random()*100) + random.uniform(0.0001, 0.19)   #5
    k_empathy        = 1.130123123 - random.betavariate(random.random()*100, random.random()*100) + random.uniform(0.0001, 0.19)   #6
    k_intelligence   = 1.1801237 - random.betavariate(random.random()*100, random.random()*100) + random.uniform(0.0001, 0.19)   #7
    k_nonNormalLexic = 1.1201238 - random.betavariate(random.random()*100, random.random()*100) + random.uniform(0.0001, 0.19)   #8
    k_direct_words   = 1.2200004 - random.betavariate(random.random()*100, random.random()*100) + random.uniform(0.0001, 0.19)   #9
    k_glossary       = random.uniform(0.0001, 0.09)         


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
