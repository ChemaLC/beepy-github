from functions import *

def print_cards(functions):
	for function in functions:
		function()
		print("=================")


functions = [
	buberto_bunzales,
]

print_cards(functions)