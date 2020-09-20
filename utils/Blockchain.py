# Blockchain类用来管理链条，它能存储交易，加入新块等


class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

    def new_block(self):
        # Creates a new Block and adds it to the chain
        pass

    def new_transaction(self, sender, recipient, amount):
        """
            向列表中添加一个交易记录，并返回该记录将被添加到的区块的索引
            :param sender: <str> Address of the Sender
            :param recipient: <str> Address of the Recipient
            :param amount: <int> Amount
            :return: <int> The index of the Block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': amount,
        })

        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # Hashes a Block
        pass

    @property
    def last_block(self):
        # Returns the last Block in the chain
        pass