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

def getIndex(char):
    char = char.upper()
    return ord(char) - 64

test = ['rafael', 'aaa', 'panela', 'computacao', 'computador', 'ar', 'bola', 'massa', 'zebra', 'paralelepipedo']
test_2 = ['aba', '@bc', 'nan', 'ada']
test_chars = ['a', 'b', 'z', 'g', 'j', 'i', 'c']

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


#CODIGO INTERNET
def countingSort(arr, charIndex):

    arr_len = len(arr)
    #Array de contagem
    count = 27*[0]

    for i in arr:
        count[getIndex(i[charIndex])] += 1

    # Array de acumulação
    for i in range(1,27):
        count[i] += count[i-1]

    # Array output
    output = arr_len*[0]
    for i in reversed(range(0, arr_len)):
        acc_pos = getIndex(arr[i][charIndex])
        output_pos = count[acc_pos]

        output[output_pos -1] = arr[i]
        count[acc_pos] -= 1

    return output


def radixSort(arr):
    for i in reversed(range(0, max_len(arr) - 1)):
        arr = countingSort(frank_array, i)

frank_array = textToArray(frankestein)
fill_words(frank_array)

for i in reversed(range(0,max_len(frank_array)-1)):
    frank_array = countingSort(frank_array, i)

#result = countingSort(frank_array,0)
print(frank_array)