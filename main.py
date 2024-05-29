#!/usr/bin/python3

def schedule_key(key: int, rounds: int) -> list[int]:
	"""
	This function takes a key and the number of rounds as arguments
	and returns a list of scheduled keys using a simple equation.
	"""

	scheduled_keys = [key]

	for _ in range(1, rounds):
		scheduled_keys.append(
			scheduled_keys[-1] ^ (scheduled_keys[-1] >> 3)
		)

	return scheduled_keys
