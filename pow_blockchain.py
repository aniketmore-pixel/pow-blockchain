# Import necessary libraries
import time
import hashlib

class Block:
    """
    Represents a single block in the blockchain.
    Each block contains an index, timestamp, transactions, previous block's hash, nonce, and its own hash.
    """
    def __init__(self, index, transactions, previous_hash, nonce=0):
        self.index = index  # Block index in the chain
        self.timestamp = time.time()  # Timestamp when block is created
        self.transactions = transactions  # List of transactions
        self.previous_hash = previous_hash  # Hash of the previous block
        self.nonce = nonce  # Counter for proof-of-work
        self.hash = self.find_hash()  # Compute block hash

    def find_hash(self):
        """Generates the SHA-256 hash of the block's contents."""
        block_data = f"{self.index}{self.timestamp}{self.transactions}{self.previous_hash}{self.nonce}"
        return hashlib.sha256(block_data.encode()).hexdigest()

    def mine_block(self, difficulty):
        """Performs proof-of-work by finding a hash that meets the required difficulty."""
        while self.hash[:difficulty] != "0" * difficulty:
            self.nonce += 1
            self.hash = self.find_hash()
        print(f"Block {self.index} mined: {self.hash}")

    def __str__(self):
        """Returns a formatted string representation of the block."""
        return (
            f"\nBlock {self.index}:\n"
            f"Timestamp: {self.timestamp}\n"
            f"Transactions: {self.transactions}\n"
            f"Previous Hash: {self.previous_hash}\n"
            f"Hash: {self.hash}\n"
            f"Nonce: {self.nonce}\n"
            "-----------------------------"
        )


class Blockchain:
    """
    Represents the blockchain, which is a series of linked blocks.
    """
    def __init__(self, difficulty=2):
        self.chain = [self.create_genesis_block()]
        self.difficulty = difficulty  # Difficulty level for proof-of-work

    def create_genesis_block(self):
        """Creates and returns the first block in the blockchain."""
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        """Returns the most recently added block."""
        return self.chain[-1]

    def add_block(self, transactions):
        """Creates, mines, and appends a new block to the blockchain."""
        latest_block = self.get_latest_block()
        new_block = Block(index=len(self.chain), transactions=transactions, previous_hash=latest_block.hash)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        """Validates the integrity of the blockchain."""
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i-1]

            # Verify the hash of the current block
            if current_block.hash != current_block.find_hash():
                return False

            # Verify the previous hash linkage
            if current_block.previous_hash != previous_block.hash:
                return False

        return True

    def print_blockchain(self):
        """Prints all blocks in the blockchain."""
        print("\nBlockchain Details:")
        for block in self.chain:
            print(block)


if __name__ == "__main__":
    # Create a new blockchain with a specified difficulty level
    aniket_blockchain = Blockchain(difficulty=3)

    # Adding multiple blocks to the blockchain
    print("\nAdding first block...")
    aniket_blockchain.add_block(["Aniket pays Pankaj 24 BTC", "Pankaj pays Kunal 7 BTC"])

    print("\nAdding second block...")
    aniket_blockchain.add_block(["Digvijay pays Satvik 3 BTC"])

    print("\nAdding third block...")
    aniket_blockchain.add_block(["Vedant pays Janhavi 42 BTC"])

    print("\nAdding fourth block...")
    aniket_blockchain.add_block(["Sara pays Aniket 12 BTC"])

    # Print the entire blockchain
    aniket_blockchain.print_blockchain()

    # Validate the blockchain
    print("\nChecking blockchain validity:", aniket_blockchain.is_chain_valid())

    # Simulating a blockchain tampering attempt
    print("\nTampering with blockchain...")
    aniket_blockchain.chain[1].transactions = ["Amit pays Tuhin 30 BTC"]  # Modify transaction data
    aniket_blockchain.chain[1].hash = aniket_blockchain.chain[1].find_hash()  # Recalculate hash after modification
    print("\nBlock 1 tampered!")

    # Print the blockchain after tampering attempt
    aniket_blockchain.print_blockchain()

    # Revalidate the blockchain
    print("Checking blockchain validity after tampering:", aniket_blockchain.is_chain_valid())