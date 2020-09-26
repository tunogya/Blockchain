import hashlib
import json
import time
from urllib.parse import urlparse
from django.contrib.sites import requests

'''
    Blockchain类用来管理链条，它能存储交易，加入新块等。
'''


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
        self.new_block(previous_hash=1, proof=100)
        self.nodes = set()

    # Creates a new Block and adds it to the chain
    def new_block(self, proof, previous_hash=None):
        # 一个区块的结构
        block = {
            # 索引
            'index': len(self.chain) + 1,
            # 前一个区块的Hash值
            'previous_hash': previous_hash or self.last_block.hash,
            # Unix时间戳
            'create_time': int(time.time()),
            # 交易列表
            'transactions': self.current_transactions,
            # 工作量证明
            'proof': proof,
        }
        # 将当前的交易列表清空
        self.current_transactions = []
        # 将当前区块上链
        self.chain.append(block)
        # 返回当前区块
        return block

    # Adds a new transaction to the list of transactions
    def new_transaction(self, state, events, data):
        transaction = {
            # '交易状态，”VALID” 表示合法交易，其它值表示非法交易',
            'state': state,
            # '交易所产生的区块链事件列表',
            'events': events,
            # '交易的详细内容，数据结构为交易中的 common.Payload',
            'data': data,
        }
        # 将当前交易插入到列表
        self.current_transactions.append(transaction)
        # 返回下一个区块的块高
        return self.last_block['index'] + 1

    # Hashes a Block
    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    # Returns the last Block in the chain
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

        return guess_hash[:4] == "0000"

    # 检查是否是有效链，遍历每个块验证hash和proof
    def valid_chain(self, chain):
        last_block = chain[0]
        current_index = 1
        while current_index < len(chain):
            block = chain[current_index]
            if block.previous_hash != last_block.hash:
                return False

            # Check that the Proof of Work is correct
            if not self.valid_proof(last_block.proof, block.proof):
                return False

            last_block = block
            current_index += 1

        return True

    # 用来解决冲突，遍历所有的邻居节点，并用上一个方法检查链的有效性， 如果发现有效更长链，就替换掉自己的链
    def resolve_conflicts(self):
        neighbours = self.nodes
        new_chain = None

        max_length = len(self.chain)

        for node in neighbours:
            response = requests.get('http://%s/blocks/' % node)

            if response.status_code == 200:
                length = json.loads(response)['length']
                chain = json.loads(response)['chain']

                # Check if the length is longer and the chain is valid
                if length > max_length and self.valid_chain():
                    max_length = length
                    new_chain = chain

        # Replace our chain if we discovered a new, valid chain longer than ours
        if new_chain:
            # 插入到数据库
            self.chain = new_chain
            return True

        return False

    # 注册节点
    def register_node(self, address):
        parsed_url = urlparse(address)
        self.nodes.add(parsed_url.netloc)
