file_name = "alice.txt"

try:
    with open(file_name) as file_object:
        contents = file_object.read()
except FileNotFoundError:
    message = "Sorry,the file "+file_name + " does not exist."
    print(message)
else:
    #计算文件大致包含多少个单词
    words = contents.split()
    number_words = len(words)
    print("The file " + file_name +" has about "+str(number_words) + " words")
