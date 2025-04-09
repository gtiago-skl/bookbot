def get_book_text(filepath):
	with open(filepath) as f:
		text = f.read()
	return text

def count_words(book_text):
	split_words = book_text.split()
	counted_words = len(split_words)
	return counted_words

def count_chars(text):
	char_count = {}
	for char in text:
		char = char.lower() #lowercase
		if char in char_count:
			char_count[char] +=1
		else:
			char_count[char] = 1
	return char_count

def retrieve_sorted(char_count, counted_words, filepath):
	# Convert dictionary to a list of tuples and sort it
	sorted_dictionary = sorted(
	[{"char": char, "count": count} for char, count in char_count.items() if char.isalpha()],
	key=lambda x: x["count"],
	reverse=True
	)
	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {filepath}...")
	print("----------- Word Count ----------")
	print(f"Found {counted_words} total words")
	print("--------- Character Count -------")
	for entry in sorted_dictionary:
		print(f"{entry['char']}: {entry['count']}")	
