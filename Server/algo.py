import emoji

def me_in_text(text):
    return 100.0*(text.count("Я") + text.count(" я") + text.count(".я") + text.count(",я") + text.count("?я")+ text.count("!я")+ text.count("(я")+ text.count("-я")+ text.count("+я")+ text.count(":я") + text.count(";я")) / float(len(text))
            
def questions(text):
    # Should correct on the test case:
    # ??
    # 2, must be  - 1
    return (text.count("?") / float(len(text))) * 100.0

def smiles(text):
    return (emoji.count() / float(len(text))) * 100.0

def nonNoramlLexic(text):
    dict = ()
    
    return 0
    

def without_me(text):
    dict = ()

    return 0

def direct_words(text):
    dict = ()
    
    return 0
    
def animals_words(text):
    counter = 0
    lst = text.replace('.', '').split()
    dict = ("крыса","тварь","животное","баран","олень","змея","сука")
    for i in lst:
        if aproximation(dict, i):
            counter += len(i)
            
    return (counter / len(text))*100.0


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
