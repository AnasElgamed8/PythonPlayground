# ==================================================================
#    ANAS' REVIEW MAKER
# ==================================================================
name = input("What is the game called?\n")
fileName = f"{name}.md"

storyThoughts = input("What are your thoughts about the story?\n")
story = int(input("What's the story's rating? (0 - 100)\n")) * .2

visualsThoughts = input("Any thoughts about the visuals?\n")
visuals = int(input("Were the visuals any good? (0 - 100)\n")) * .2

audioThoughts = input("What do you think of the audio?\n")
audio = int(input("How good was the audio? (0 - 100)\n")) * .2

charactersThoughts = input("What do you think of the characters?\n")
characters = int(input("How much did you like the characters? (0 - 100)\n")) * .15

narrativeThoughts = input("Any comments on the narrative/atmosphere/pacing/execution?\n")
narrative = int(input("Give it a rating (0 - 100)\n")) * .15

enjoymentThoughts = input("How enjoyable was the experience?\n")
enjoyment = int(input("Did you enjoy the game? (0 - 100)\n")) * .1

finalScore = (story + visuals + audio + characters + narrative + enjoyment) / 10
print(f"Final Score: {finalScore}")

with open(fileName, "a") as f:
    f.write(f"# {name}\n\n")

    f.write("## Story\n")
    f.write(f"{storyThoughts}\n")
    f.write(f"Story rating: {story}/20\n\n")

    f.write("## Visuals\n")
    f.write(f"{visualsThoughts}\n")
    f.write(f"Visuals rating: {visuals}/20\n\n")

    f.write("## Audio\n")
    f.write(f"{audioThoughts}\n")
    f.write(f"Audio rating: {audio}/20\n\n")

    f.write("## Characters\n")
    f.write(f"{charactersThoughts}\n")
    f.write(f"Characters rating: {characters}/15\n\n")

    f.write("## Narrative\n")
    f.write(f"{narrativeThoughts}\n")
    f.write(f"Narrative rating: {narrative}/15\n\n")

    f.write("## Enjoyment\n")
    f.write(f"{enjoymentThoughts}\n")
    f.write(f"Enjoyment rating: {enjoyment}/10\n\n")

    f.write(f"## Final score: {finalScore}\n")
