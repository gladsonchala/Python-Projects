def take_input(type: str):
	return input(f"Enter word of type {type}: ")


def main():
	adjective1 = take_input("adjective")
	adjective2 = take_input("adjective")
	adjective3 = take_input("adjective")
	adjective4 = take_input("adjective")
	adjective5 = take_input("adjective")
	adjective6 = take_input("adjective")
	verb1 = take_input("verb-ing")
	noun1 = take_input("plural noun")
	adverb1 = take_input("adverb")

	story = f"""Once upon a time, Lovebird met Sweetie on a {adjective1} day. They felt a {adjective2} connection and spent days {verb1} in {adjective3} meadows. Lovebird proposed under the {adjective4} stars, and Sweetie said "Yes!" Their {adjective5} wedding was filled with {noun1}, and they danced {adverb1} ever after. Their love was as strong as the {adjective6} mountains."""
	print(story)

if __name__ == '__main__':
	main()