# Blockchain类用来管理链条，它能存储交易，加入新块等

import hashlib
import json
from datetime import time


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)
        self.nodes = set()

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        self.current_transactions = []
        self.chain.append(block)
        return block

    # 向列表中添加一个交易记录，并返回该记录将被添加到的区块的索引
    def new_transaction(self, sender, recipient, amount):
        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    # PoW
    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    # PoW验证，修改零开头的个数来控制难度
    @staticmethod
    def valid_proof(last_proof, proof):
        guess = str(last_proof * proof).encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:5] == "00000"
