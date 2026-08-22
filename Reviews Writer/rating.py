# ==================================================================
#   ANAS' REVIEW MAKER
# ==================================================================
name = input("What is the game called?\n")
fileName = f"{name}.md"

introThoughts = input("Write a brief introduction for the review:\n")

storyThoughts = input("What are your thoughts about the story?\n")
story = int(input("What's the story's rating? (0 - 100)\n")) * .20

visualsThoughts = input("Any thoughts about the visuals?\n")
visuals = int(input("Were the visuals any good? (0 - 100)\n")) * .15

audioThoughts = input("What do you think of the audio?\n")
audio = int(input("How good was the audio? (0 - 100)\n")) * .10

charactersThoughts = input("What do you think of the characters?\n")
characters = int(input("How much did you like the characters? (0 - 100)\n")) * .15

narrativeThoughts = input("Any comments on the pacing or atmosphere?\n")
narrative = int(input("Give it a rating (0 - 100)\n")) * .10

endingsThoughts = input("What did you think about the endings?\n")
endings = int(input("How would you rate the endings? (0 - 100)\n")) * .20

enjoymentThoughts = input("How enjoyable was the experience?\n")
enjoyment = int(input("Did you enjoy the game? (0 - 100)\n")) * .10

finalThoughts = input("What are your final thoughts/conclusion?\n")

finalScore = (story + visuals + audio + characters + narrative + endings + enjoyment) / 10
print(f"Final Score: {finalScore:.2f}")

with open(fileName, "a", encoding="utf-8") as f:
    f.write(f"# {name}\n\n")
    
    if introThoughts.strip():
        f.write(f"{introThoughts}\n\n")
    
    f.write("## Story\n")
    f.write(f"{storyThoughts}\n")
    f.write(f"Story rating: {story}/20\n\n")

    f.write("## Visuals\n")
    f.write(f"{visualsThoughts}\n")
    f.write(f"Visuals rating: {visuals}/15\n\n")

    f.write("## Audio\n")
    f.write(f"{audioThoughts}\n")
    f.write(f"Audio rating: {audio}/10\n\n")

    f.write("## Characters\n")
    f.write(f"{charactersThoughts}\n")
    f.write(f"Characters rating: {characters}/15\n\n")

    f.write("## Narrative\n")
    f.write(f"{narrativeThoughts}\n")
    f.write(f"Narrative rating: {narrative}/10\n\n")

    f.write("## Endings\n")
    f.write(f"{endingsThoughts}\n")
    f.write(f"Endings rating: {endings}/20\n\n")

    f.write("## Enjoyment\n")
    f.write(f"{enjoymentThoughts}\n")
    f.write(f"Enjoyment rating: {enjoyment}/10\n\n")

    f.write("## Final Thoughts\n")
    f.write(f"{finalThoughts}\n\n")
    f.write(f"### Final score: {finalScore:.2f}\n")
