import nltk
from nltk.corpus import wordnet

nltk.download('wordnet')

def is_animal_noun(word):
    synsets = wordnet.synsets(word, pos=wordnet.NOUN)
    return any('animal' in synset.lexname() for synset in synsets)

def filter_words(input_file, output_animals_file, output_non_animals_file):
    animal_words = set()
    non_animal_words = set()

    # 读取输入文件
    with open(input_file, 'r', encoding='utf-8') as input_file:
        all_words = [line.strip().lower() for line in input_file]

    # 分类词汇为动物和非动物
    for word in all_words:
        if is_animal_noun(word):
            animal_words.add(word)
        else:
            non_animal_words.add(word)

    # 将结果写入两个输出文件
    with open(output_animals_file, 'w', encoding='utf-8') as output_animals:
        output_animals.write('\n'.join(sorted(animal_words)))

    with open(output_non_animals_file, 'w', encoding='utf-8') as output_non_animals:
        output_non_animals.write('\n'.join(sorted(non_animal_words)))

# 用法示例
input_file_path = 'your_input_file.txt'
output_animals_file_path = 'output_animal_words.txt'
output_non_animals_file_path = 'output_non_animal_words.txt'

filter_words(input_file_path, output_animals_file_path, output_non_animals_file_path)
