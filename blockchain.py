#timestamp

import datetime

# hash to add digital fingerprints to the blocks
import hashlib

#to store data in the blockchain
import json

#Flask is for the web app for displaying the blockchain
from flask import Flask, jsonify

class Blockchain:
    
    #fuction to create first block and set its hash to 0
    def __init__(self):
        self.chain = []
        self.create_block(proof=1, previous_hash='0')
    
    #function to add more blocks to the chain    
    def create_block(self, proof, previous_hash):
        block={'index': len(self.chain) + 1,
               'timestamp': str(datetime.datetime.now()),
               'proof': proof,
               'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    def create_block(self, proof, previous_hash):
        block={'index': len(self.chain) + 1,
               'timestamp': str(datetime.datetime.now()),
               'proof': proof,
               'previous_hash': previous_hash}
        self.chain.append(block)
        return block
    
    #function to get the previous block
    def get_previous_block(self):
        return self.chain[-1]
    
    #function to get the proof of work
    def proof_of_work(self, previous_proof):
        new_proof=1
        check_proof=False
        while check_proof is False:
            hash_operation=hashlib.sha256(str(new_proof**2 - previous_proof**2).encode()).hexdigest()
            if hash_operation[:4]=='0000':
                check_proof=True
            else:
                new_proof += 1
        return new_proof
    
    def hash(self, block):
        encoded_block=json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(encoded_block).hexdigest()
    
    def chain_valid(self, chain):
        previous_block = chain[0]
        block_index = 1
         
        while block_index < len(chain):
            block = chain[block_index]
            if block['previous_hash'] != self.hash(previous_block):
                return False
               
            previous_proof = previous_block['proof']
            proof = block['proof']
            hash_operation = hashlib.sha256(
                str(proof**2 - previous_proof**2).encode()).hexdigest()
             
            if hash_operation[:5] != '00000':
                return False
            previous_block = block
            block_index += 1
         
        return True
    
    
