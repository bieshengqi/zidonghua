

def save_file(file_path='./conf/user_token.txt',content=''):
    """
    保存字符串到文件
    """
    with open(file_path,'w') as f:
        f.writelines(content)


def read_file(file_path='./conf/user_token.txt'):
    """
    读取txt文件
    """
    with open(file_path,'r') as f:
        content = f.read()
     
    return content