"""
 * © 2024 Jerry Tan. All Rights Reserved.
 *
 * This software is the confidential and proprietary information of Jerry Tan
 * ("Confidential Information"). You shall not disclose such Confidential Information
 * and shall use it only in accordance with the terms under which this software
 * was distributed or otherwise published, and solely for the prior express purposes
 * explicitly communicated and agreed upon, and only for those specific permissible purposes.
 *
 * This software is provided "AS IS," without a warranty of any kind. All express or implied
 * conditions, representations, and warranties, including any implied warranty of merchantability,
 * fitness for a particular purpose, or non-infringement, are disclaimed, except to the extent
 * that such disclaimers are held to be legally invalid.
 *
 * This file contains unit tests for the blockchain functionality.
"""

import unittest
from blockchain import Blockchain

class TestBlockchain(unittest.TestCase):
    def setUp(self):
        self.blockchain = Blockchain()

    def test_genesis_block(self):
        # Test that the genesis block is created properly
        self.assertEqual(len(self.blockchain.chain), 1)

    def test_new_transaction(self):
        # Test that new transactions are added correctly
        index = self.blockchain.new_transaction('voter1', 'candidateA')
        self.assertEqual(index, 2)  # Expect the new block to be at index 2

    def test_proof_of_work(self):
        # Test that proof of work generates a valid proof
        last_proof = self.blockchain.last_block['proof']
        proof = self.blockchain.proof_of_work(last_proof)
        self.assertTrue(self.blockchain.valid_proof(last_proof, proof))

if __name__ == '__main__':
    unittest.main()
