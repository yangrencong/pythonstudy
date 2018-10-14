def count_words(file_name):
    """ 计算一个文件大致包含多少个单词 """
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        pass
    else:
        #计算文件含有多少个单词
        words = contents.split()
        number_words = len(words)
        print("The file "+ file_name +" has about "+str(number_words)+" words")


filenames = ["alice.txt","siddhartha.txt","moby_dict.txt","little_women.txt"]
for filename in filenames:
    count_words(filename)
