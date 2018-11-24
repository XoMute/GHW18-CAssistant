import emoji

def me_in_text(text):
    words_len = 0
    full_len = 0
   # print(text)
    for elem in text:
       # print(elem)
        words_len += int(elem['text'].count("Я")) + int(elem['text'].count(" я")) + int(elem['text'].count(".я")) + int(elem['text'].count(",я")) + int(elem['text'].count("?я"))+ int(elem['text'].count("!я"))+ int(elem['text'].count("(я"))+ int(elem['text'].count("-я"))+ int(elem['text'].count("+я"))+ elem['text'].count(":я") + int(elem['text'].count(";я"))
        full_len += len(elem['text'])
                          
    return (words_len / full_len) * 100.0
            
def questions(text):
    # Should correct on the test case:
    # ??
    # 2, must be  - 1
    q_len = 0
    full_len = 0                      
    for elem in text:
        q_len += int(elem['text'].count("?"))
        full_len +=float(len(elem['text']))
        
    return (q_len / full_len) * 100.0

def smiles(text):

    emoji_len = 0
    full_len = 0
    for elem in text:
        emoji_len += int(emoji.emoji_count(elem['text']))
        full_len  += float(len(elem['text']))
        
    return (emoji_len / full_len) * 100.0

def nonNormalLexic(text):
    dic = []
    
    return 0
    

def without_me(text):
    dic = []

    return 0

def direct_words(text):
    dic = []
    
    return 0
    
def animals_words(text):
    counter = 0
    animals_len = 0
    full_len = 0
    dic = ["крыса","тварь","животное","баран","олень","змея","сука"]                          
    for elem in text:
        lst = elem['text'].replace('.', '').split()        
        for i in lst:
            if aproximation(dic, i):
                animals_len += len(i)
        full_len += len(elem['text'])
            
    return (animals_len / full_len)*100.0


# Функция приближенно определяет, то ли это слово:
#   рыба
#   рыбq
#   совпадение есть, тогда вернет, что слово подходит

def aproximation(string, word):
    counter = 0
    for w in string:
        for i in range(len(word)):
            if (len(w) > i) and (word[i] == w[i]):
                counter +=1
        if counter / float(len(word)) > 0.7:
            return 1
    return 0
