#!/usr/bin/python3
# Author: 沈麻呆
# Date: 2021-10-3

import random
import pathlib


class Generator:
    def __init__(self, file_list):
        self._library = []
        self._load_file(file_list)

    def _load_file(self, file_list):
        for filename in file_list:
            with open(filename, 'r', encoding='utf-8') as f:
                self._library.append(list(l.strip() for l in f.readlines()))

    def generate_one(self) -> str:
        return "".join((random.choice(candidates) for candidates in self._library))


_inst = Generator(file_list=[pathlib.Path(__file__).parent.joinpath(f) for f in ['prefix.txt', 'suffix.txt']])
generate_one = _inst.generate_one
