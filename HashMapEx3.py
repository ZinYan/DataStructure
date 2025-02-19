word_dict = {}
with open('Files/poem.txt','r') as f:
    for line in f:
        word_lst = line.split(' ')
        for word in word_lst:
            word = word.replace('\n','')
            if word in word_dict:
                word_dict[word] += 1
            else:
                word_dict[word] = 1
for key,value in word_dict.items():
    print(f'{key} : {value}')