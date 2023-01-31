##
## EPITECH PROJECT, 2023
## undefined
## File description:
## etape_2
##

import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, nonce):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.nonce = nonce
        
    def hash(self):
        block_data = str(self.index) + self.previous_hash + str(self.timestamp) + self.data + str(self.nonce)
        block_data_bytes = block_data.encode()
        return hashlib.sha256(block_data_bytes).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]
        self.difficulty = 5
        
    def create_genesis_block(self):
        return Block(0, "0", time.time(), "Genesis Block", 0)
    
    def add_block(self, data):
        previous_block = self.chain[-1]
        index = previous_block.index + 1
        previous_hash = previous_block.hash()
        timestamp = time.time()
        nonce = proof_of_work(Block(index, previous_hash, timestamp, data, 0), self.difficulty)
        block = Block(index, previous_hash, timestamp, data, nonce)
        self.chain.append(block)
        
    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]
            
            if current_block.hash() != current_block.hash():
                return False
            
            if current_block.previous_hash != previous_block.hash():
                return False
                
        return True

def proof_of_work(block, difficulty):
    target = '0' * difficulty
    for nonce in range(100000000):
        hash_data = str(block.index) + block.previous_hash + str(block.timestamp) + block.data + str(nonce)
        hash_data_bytes = hash_data.encode()
        hash = hashlib.sha256(hash_data_bytes).hexdigest()
        if hash[:difficulty] == target:
            return nonce
    return None


blockchain = Blockchain()
blockchain.add_block("Ptdr")
blockchain.add_block("Data for block 2")
blockchain.add_block("Data for block 3")

for block in blockchain.chain:
    print("Index:", block.index)
    print("Previous Hash:", block.previous_hash)
    print("Timestamp:", block.timestamp)
    print("Data:", block.data)
    print("Nonce:", block.nonce)
    print("Hash:", block.hash())
    print()

print("Is Blockchain Valid?:", blockchain.is_chain_valid())