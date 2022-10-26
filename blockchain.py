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
    
