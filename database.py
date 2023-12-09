class Database:
    def __init__(self):
        self.data = {}
        self.transaction_data = {}
        self.transaction_in_progress = False

    def begin_transaction(self):
        if self.transaction_in_progress:
            raise Exception("Transaction already in progress")
        self.transaction_in_progress = True

    def put(self, key, value):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.transaction_data[key] = value

    def get(self, key):
        if key in self.transaction_data:
            return self.transaction_data[key]
        return self.data.get(key, None)

    def commit(self):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.data.update(self.transaction_data)
        self.transaction_data = {}
        self.transaction_in_progress = False

    def rollback(self):
        if not self.transaction_in_progress:
            raise Exception("No transaction in progress")
        self.transaction_data = {}
        self.transaction_in_progress = False
