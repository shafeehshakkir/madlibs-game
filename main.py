# Madlibs Word Game

print("Welcome to the Madlibs Word Game!.\n")

# Collecting user inputs
adjective1 = input("Enter an adjective (describing a noun, e.g., 'funny', 'beautiful'): ")
noun1 = input("Enter a noun (a person, place, or thing, e.g., 'cat', 'mountain'): ")
verb1 = input("Enter a verb ending with 'ing' (an action, e.g., 'running', 'dancing'): ")
adjective2 = input("Enter another adjective: ")
noun2 = input("Enter another noun: ")
verb2 = input("Enter another verb ending with 'ing': ")
place = input("Enter a place (e.g., 'beach', 'museum'): ")
emotion = input("Enter an emotion (e.g., 'happy', 'surprised'): ")

#madlibs story
print(f"Today, I went to a {adjective1} {place}.")
print(f"As I walked around, I stumbled upon a {noun1}.")
print(f"I was really {emotion} when I saw it because the {noun1} was {verb1}.")
print(f"Not only that, but there was also a {adjective2} {noun2} nearby!")
print(f"It was {verb2} all around, which made the day even more exciting!")
print(f"In the end, I left the {place} feeling so {emotion} and couldn't wait to come back.")

print("\nHope you enjoyed the story! do more for more fun!")
