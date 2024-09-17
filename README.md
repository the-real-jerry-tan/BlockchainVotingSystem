
# Blockchain Voting System - Minimal Viable Product (MVP)

## Overview

This project is a **minimal viable product (MVP) for a blockchain-based voting system**. It provides a basic implementation of a distributed and tamper-proof voting mechanism using blockchain technology. The system allows voters to cast their votes, which are recorded as transactions on a blockchain, ensuring that all votes are securely stored and that the integrity of the voting process is maintained.

The system uses **proof-of-work (PoW)** as the core mechanism for maintaining blockchain integrity and validating new blocks. PoW is a consensus mechanism that helps secure the blockchain and ensures that computational effort is required to mine new blocks.

## Features

- **Vote Submission**: Voters can submit votes through a REST API, ensuring that each vote is uniquely identified.
- **Blockchain Security**: Each vote is part of a transaction stored in blocks and protected by the PoW algorithm, ensuring tamper-proof voting records.
- **Block Mining**: Votes are added to the blockchain once a new block is mined, providing transparency in how votes are handled.
- **Full Chain View**: The entire blockchain can be queried via an API to review all transactions (votes) and blocks.

## Proof-of-Work vs Raft Consensus

The current system uses **Proof-of-Work (PoW)** to validate and secure transactions, similar to how Bitcoin and other decentralized systems work. However, PoW is computationally intensive and may not be suitable for certain distributed applications that need faster consensus without the need for high computational resources.

For more advanced distributed systems, consensus algorithms like **Raft** can be implemented. Raft is a leader-based consensus algorithm that ensures all nodes in a distributed network agree on the current state of the blockchain. It is more efficient and practical for applications that require consistency across distributed nodes without the need for intensive computational resources like PoW.

### Future Development: Implementing Raft Consensus
In future iterations, **implementing Raft consensus** would be a natural next step to make this system more distributed and fault-tolerant. Raft would ensure that all nodes in the network agree on the blockchain's state, even in the presence of network partitions or node failures. This would make the system more suitable for distributed voting applications where consistency and reliability are critical.

## How to Run the Project

### Step 1: Set Up and Run the Blockchain Voting System

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/the-real-jerry-tan/BlockchainVotingSystem.git
   cd BlockchainVotingSystem
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install Flask
   ```

4. **Run the Application**:
   ```bash
   python src/server.py
   ```

### Step 2: Interact with the Blockchain Voting System

Once the server is running, use the following commands to interact with the blockchain:

1. **Vote Submission**:
   ```bash
   curl -X POST http://127.0.0.1:5000/vote -H "Content-Type: application/json" -d '{"voter_id":"voter123", "vote":"candidateA"}'
   ```

2. **Mine a Block**:
   ```bash
   curl http://127.0.0.1:5000/mine
   ```

3. **View the Entire Blockchain**:
   ```bash
   curl http://127.0.0.1:5000/chain
   ```

## Running Unit Tests

Unit tests for the blockchain logic are available in `test_blockchain.py`. You can run them using the following command:

```bash
python -m unittest src/test_blockchain.py
```

## License

This project is © 2024 Jerry Tan. All Rights Reserved.

