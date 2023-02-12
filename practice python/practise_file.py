import practise_loop

file = open("E:\Python Code\Viper.txt",'a',encoding="UTF-8")
print(type(file))
#print(file.read(10))
# print(file.read())
print("--------------------")
file.write('\n chaos')
file.flush()
# print(file.readlines())
file.close()
from practise_loop import chaos_len

print(chaos_len("123"))
