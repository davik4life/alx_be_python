noun = str(input("Enter a noun: "))
verb = str(input("Enter a verb: "))
adjective = str(input("Enter an adjective: "))

story = (f"On a beautiful {adjective} day, I went to the zoo. I saw a funny {adjective} monkey swinging from the trees. Then, I spotted a majestic {adjective} lion lounging in the sun.  What a wild and {adjective} experience! ")

if verb.lower() == "run":
    story += f"I decided to {verb} around the zoo to see more animals!"
elif verb.lower() == "jump":
    story += f"I couldn't help but {verb} with excitement seeing all these animals!"
else:
    story += f"I wanted to {verb} but I was too amazed by the animals!"
story += f" Finally, I bought a souvenir {noun} to remember my visit."
print(story)


print("Welcome to the Mad Libs generator!")