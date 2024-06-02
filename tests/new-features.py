# /tests/new-features.py

def substitute_bits(block: bytes, table: bytes, reverse: bool = False) -> bytes:
	pass

def permute(block: bytes, table: bytes, reverse: bool = False) -> bytes:
	pass

def key_generate(passphrase: bytes) -> bytes:
	pass

def key_shedule(key: bytes, rounds: int) -> list[bytes]:
	pass

def encrypt_block(block: bytes):
	pass

def dectypt_block(block: bytes):
	pass

def encrypt_file(input_file: str, output_file: str, key: bytes):
	pass

def decrypt_file(input_file: str, output_file: str, key: bytes):
	pass
