import os
path = r"C:\Users\91342\Desktop\test"
# f_name='bag_of_words_explicit.txt'
for f_name in os.listdir(path):
    f_name=os.path.join(path, f_name)
    with open(f_name, 'r') as f:
        lines = f.readlines()
        new_lines=[]
        for line in lines:
            if line[0]!='\n' and line[0]!='#':
                new_lines.append(line)
    with open(os.path.join(path,"tmp"), 'w') as tmp:
        tmp.writelines(new_lines)
    os.remove(os.path.join(path, f_name))
    os.rename(os.path.join(path, "tmp"), os.path.join(path, f_name))
'''
        flag = False
        for line in lines:
            if line[0]=='\n' or line[0]=='#':
                if flag:
                    print(line)
                    continue
                else:
                    new_lines.append("\n")
                    flag = True
            else:
                flag = False
                new_lines.append(line)
'''





