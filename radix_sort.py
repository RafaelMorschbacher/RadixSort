# ----------------- ARQUIVOS -----------------------
# Leitura de arquivos de entrada e saída
frankestein = open('frankestein_clean.txt', 'r')
warAndPeace = open('war_and_peace_clean.txt', 'r')
frankestein_output = open('frankenstein_ordenado.txt', 'w')
war_peace_output = open('war_and_peace_ordenado.txt', 'w')


# Funções Auxiliares
def textToArray(file):
    read = file.readlines()
    words = []
    for line in read:
        cleanLine = line.strip().split()  # remove \n da linha
        for word in cleanLine:
            if len(word) >= 4:
                words.append(word)
    fill_words(words)
    return words


# Tamanho da maior palavra do array
def max_len(arr):
    max_size = 0
    for word in arr:
        if len(word) > max_size:
            max_size = len(word)
    return max_size


# getIndex: char => posição (de 0 (@) até 26 (Z))
def getIndex(char):
    char = char.upper()
    return ord(char) - 64


# Preeche palavras com @'s para um tamanho padrão (tamanho da maior palavra)
def fill_words(arr):
    size = max_len(arr)
    for index, word in enumerate(arr):
        word_len = len(word)
        if word_len < size:
            filler = []
            for i in range(word_len, size):
                filler.append('@')
            filler_string = ''.join(filler)
            arr[index] = word + filler_string


def countingSort(arr, charIndex):
    arr_len = len(arr)
    # Array de contagem
    count = 27 * [0]

    for i in arr:
        count[getIndex(i[charIndex])] += 1

    # Array de acumulação
    for i in range(1, 27):
        count[i] += count[i - 1]

    # Array output
    output = arr_len * [0]
    for i in reversed(range(0, arr_len)):
        acc_pos = getIndex(arr[i][charIndex])
        output_pos = count[acc_pos]

        output[output_pos - 1] = arr[i]
        count[acc_pos] -= 1

    # arr = output
    for i in range(0, arr_len):
        arr[i] = output[i]


def radixSort(arr):
    for i in reversed(range(0, max_len(arr) - 1)):
        countingSort(arr, i)


def output_write(arr, output_file):
    arr_len = len(arr)
    for i in range(0, arr_len):
        if i == 0 or arr[i] != arr[i - 1]:
            counter = 0
            j = i
            while arr[j] == arr[i] and j < arr_len-1:
                counter += 1
                j += 1

            word = arr[i].replace('@', '')
            output_file.write(word + ' ' + str(counter) + '\n')


# Main:
war_array = textToArray(warAndPeace)
radixSort(war_array)
output_write(war_array, war_peace_output)

frank_array = textToArray(frankestein)
radixSort(frank_array)
output_write(frank_array, frankestein_output)


