# ----------------- ARQUIVOS -----------------------
# Leitura de arquivo de entrada -> cada vetor será inserido em lists
frankestein = open('frankestein_clean.txt', 'r')



def textToArray(file):
    read = file.readlines()
    words = []
    for line in read:
        cleanLine = line.strip().split()  # remove \n da linha
        for word in cleanLine:
            if len(word)>=4:
                words.append(word)
    return words

def max_len(arr):
    max_size = 0
    for word in arr:
        if len(word)> max_size:
            max_size = len(word)
    return max_size
#print(textToArray(frankestein))

test = ['rafael', 'aaa', 'panela', 'computacao', 'computador', 'ar', 'bola', 'massa', 'zebra', 'paralelepipedo']

def fill_words(arr):
    size = max_len(arr)
    for index, word in enumerate(arr):
        word_len = len(word)
        if word_len < size:
            filler = []
            for i in range(word_len,size):
                filler.append('@')
            filler_string = ''.join(filler)
            arr[index] = word + filler_string

# Python program for implementation of Radix Sort
# A function to do counting sort of arr[] according to
# the digit represented by exp.






frank_array = textToArray(frankestein)
fill_words(frank_array)
print(frank_array)
