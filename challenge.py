# Create a function that accepts a Star Wars character's name and returns the color of that character's lightsaber. The function should return "unknown" when the character is not in the list.

def lightsaber_color(character):
    if character == "Luke Skywalker":
        return "green"
    if character == "Yoda":
        return "green"
    if character == "Mace Windu":
        return "purple"
    if character == "Darth Vader":
        return "red"
    if character == "Darth Maul":
        return "red"
    if character == "Obi-Wan Kenobi":
        return "blue"
    return "unknown"