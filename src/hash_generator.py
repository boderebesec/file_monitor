"""
Hash Generator module for generating and verifying file hashes.
"""

import hashlib

class HashGenerator:
    """
    Generates and verifies file hashes.
    """
    def __init__(self, algorithm='sha256'):
        self.algorithm = algorithm

    def generate_hash(self, file_path):
        """
        Generates a hash for the given file.
        """
        hash_obj = hashlib.new(self.algorithm)
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_obj.update(chunk)
        return hash_obj.hexdigest()

    def verify_hash(self, file_path, stored_hash):
        """
        Verifies the hash of the given file against a stored hash.
        """
        current_hash = self.generate_hash(file_path)
        return current_hash == stored_hash