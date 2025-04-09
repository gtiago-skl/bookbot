import sys
from stats import count_words, get_book_text, count_chars, retrieve_sorted


def main():
	if len(sys.argv) != 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)
	else:
		filepath = sys.argv[1]
		book_text = get_book_text(filepath)
		counted_words = count_words(book_text)
		counted_chars = count_chars(book_text)
		retrieve_sorted(counted_chars, counted_words, filepath)
main()

