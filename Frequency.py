import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
def freq_analysis(message):

    alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z','?','/','']
    # builds empty count_list ([0,0,0...0,0])
    count_list = []
    i = 0
    while i < 29:
        count_list.append(0)
        i += 1
    # converts message string to array
    array = []
    for i in message.lower():
        array.append(i)
    n = len(array) + 0
    # counts occurences of each letter
    for x in array:
        i = 0
        while i < 29:
            if x == alphabet[i]:
                count_list[i] += 1
            i += 1
    # normalizes frequencies
    freq_list = []
    for x in count_list:
        freq_list.append(x)
    return freq_list



#Tests
import numpy as np
def making_chart(text):
  objects = freq_analysis(text)
#print(objects)

  label = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
                'n','o','p','q','r','s','t','u','v','w','x','y','z','?','/','']

  index = np.arange(len(label))
  plt.bar(index, objects)
  plt.xlabel('Aplhabet', fontsize=10)
  plt.ylabel('Relative Frequency', fontsize=10)
  plt.xticks(index, label, fontsize=8, rotation=30)
  plt.title('Frequency Analysis (Encrypted)')
  plt.show()
