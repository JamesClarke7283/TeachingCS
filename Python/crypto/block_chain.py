"""
"""

import hashlib
import json
from time import time


class Block:
    def __init__(self, index: int, timestamp: float, data: object, previous_hash: str):
        self.index = index
        self.timestamp = timestamp
        self._data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_sum = str(self.index) + str(self.timestamp) + repr(self._data) + str(self.previous_hash)
        return hashlib.sha256(block_sum.encode()).hexdigest()

    def __repr__(self) -> str:
        return f"Index: '{self.index}' Timestamp: '{self.timestamp}' Data: '{self._data}' Previous Hash: '{self.previous_hash}' Hash: '{self.hash}'"

    def __str__(self) -> str:
        return f"{self.index},{self.timestamp},{self._data},{self.previous_hash},{self.hash}"

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data
        self.hash = self.calculate_hash()


class Blockchain:
    def __init__(self):
        self.chain: list[Block] = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, time(), "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data: object): 
        previous_hash = self.get_latest_block().hash
        new_block = Block(self.chain[-1].index + 1, time(), data, previous_hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            if current_block.hash != current_block.calculate_hash():
                return False
            if current_block.previous_hash != previous_block.hash:
                return False
            if current_block.previous_hash != previous_block.calculate_hash():
                return False
        return True
    
    def __repr__(self) -> str:
        rstr = ""
        for block in self.chain:
            rstr += repr(block) + "\n"
        return rstr


my_blockchain = Blockchain()
my_blockchain.add_block("Transaction Data 1")
my_blockchain.add_block("Transaction Data 2")
my_blockchain.add_block("Transaction Data 3")

print("Is the blockchain valid?", my_blockchain.is_chain_valid())

print(repr(my_blockchain))