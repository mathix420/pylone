from hashlib import md5

def gen_sum(file_name):
    with open(file_name, 'rb') as fp:
        return md5(fp.read()).hexdigest()
