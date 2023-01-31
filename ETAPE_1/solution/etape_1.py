##
## EPITECH PROJECT, 2023
## undefined
## File description:
## etape_1
##

import hashlib
import time

class Block:
    def __init__(self, prev_hash, data):
        self.prev_hash = prev_hash
        self.data = data
        self.timestamp = time.time()
        self.hash = self.calculate_hash()
        
    def calculate_hash(self):
        sha = hashlib.sha256()
        sha.update(str(self.prev_hash).encode('utf-8') + 
                   str(self.data).encode('utf-8') + 
                   str(self.timestamp).encode('utf-8'))
        return sha.hexdigest()

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        
    def create_genesis_block(self):
        return Block("0", "Genesis Block")
    
    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        block = Block(prev_hash, data)
        self.chain.append(block)
        
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            block = self.chain[i]
            prev_block = self.chain[i - 1]
            if block.hash != block.calculate_hash():
                return False
            if block.prev_hash != prev_block.hash:
                return False
        return True

blockchain = Blockchain()
blockchain.add_block("Ptdr")
blockchain.add_block("Data for block 2")
print("Is Blockchain Valid?:", blockchain.is_chain_valid())