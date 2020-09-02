import os
import yaml
from config import BASE_PATH


def read_yaml(filename):
    filepath = BASE_PATH + os.sep + 'data' + os.sep + filename
    with open(filepath, 'r', encoding='utf-8') as f:
        datas = yaml.safe_load(f)
        arrs = []
        for data in datas.values():
            arrs.append(tuple(data.values()))
        return arrs


if __name__ == '__main__':
    read_yaml('login.yaml')
