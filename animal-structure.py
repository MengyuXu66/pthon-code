import nltk
from nltk.corpus import wordnet
import pandas as pd
import os

# 下载 WordNet 数据
nltk.download('wordnet')

def is_animal_structure(word):
    # 获取词汇的主同义词集合
    synsets = wordnet.synsets(word)

    # 动物结构的上位词、下位词、同义词列表
    animal_structure_related_words = ["feather", "hair", "hoof", "wing", "scale", "mane", "tail", "fin", 
                                      "beak", "gill", "claw", "horn", "snout", "skeleton", "abdominal muscles", 
                                      "skin", "tentacle", "dorsal fin", "tail fin", "mouth", "carapace", 
                                      "plume", "crawl", "leg", "neck", "eye", "ear", "lip", "tooth", "chest", 
                                      "forelimb", "hind limb", "bristles"]

    # 判断词汇是否属于动物结构
    for synset in synsets:
        # 获取前两个含义
        meanings = [lemma.name() for lemma in synset.lemmas()[:1]]
        
        # 判断是否有词汇在动物结构相关词汇列表中
        if any(meaning in animal_structure_related_words for meaning in meanings):
            return True

    return False

# 文件路径替换为实际的文件名，如果在同一目录下可以使用相对路径
path_to_animal_words_file = "animal_words.txt"

# 读取 animal words 文档中的单词列表
with open(path_to_animal_words_file, "r", encoding="utf-8") as file:
    animal_word_list = [word.strip() for word in file.readlines()]

# 判断每个词汇是否属于动物结构
results = []
for word in animal_word_list:
    if is_animal_structure(word):
        results.append({"Word": word, "Category": "Animal Structure"})
    else:
        results.append({"Word": word, "Category": "Not Animal Structure"})

# 获取当前工作目录
current_dir = os.getcwd()

# 将结果转换为数据框
df = pd.DataFrame(results)

# 将数据框保存为 Excel 文件，路径为相对路径
excel_path = os.path.join(current_dir, "results.xlsx")
df.to_excel(excel_path, index=False)

print(f"结果已保存到 Excel 文件：{excel_path}")
