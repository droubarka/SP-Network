# /modules/spnetwork.py

import functions

def substitute(block: bytes, table: bytes, reverse: bool = False) -> bytes:
	"""
	Perform byte substitution on a block of bytes in either direction.

	Args:
		block: A block of bytes to be substituted.
		table: A bytes object representing the substitution table.
		inverse: A boolean flag to determine the direction of substitution.

	Returns:
		A block of bytes resulting from the substitution.
	"""
	if not isinstance(block, bytes):
		raise ValueError("block argument must be a bytes object")

	if not isinstance(table, bytes):
		raise ValueError("table argument must be a bytes object")

	if len(set(table)) != 256:
		raise ValueError("table argument must contain exactly 256 unique elements")

	if reverse:
		substituted_block = [table.index(byte) for byte in block]
	else:
		substituted_block = [table[byte] for byte in block]

	return bytes(substituted_block)

def permute(block: bytes, table: list, reverse: bool = False) -> bytes:
	block_bits = list(map(int, functions.bytes_to_bits(block)))
	block_bits_len = len(block_bits)

	if reverse:
		permuted_block = [block_bits[table.index(pb_idx)] for pb_idx in range(block_bits_len)]
	else:
		permuted_block = [block_bits[table[pb_idx]] for pb_idx in range(block_bits_len)]

	return int.to_bytes(int(''.join(map(str, permuted_block)), 2), length=16, byteorder='big')
