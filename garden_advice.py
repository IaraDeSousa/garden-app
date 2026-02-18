# This is a simple gardening advice application which provides gardening tips
#  based on the season and type of plant. The user will be able to input the 
# season and plant type and then the application will give the user 
# appropriate advice.

# User input for season
season = "winter"  # TODO: Replace with input() to allow user interaction.

# Hardcoded plant type for now, will be replaced with user input later
plant_type = "flower"  # TODO: Replace with input() to allow user interaction.

# Variable to hold gardening advice, which will be built based on the season and plant type.
advice = ""

# Determine advice based on the user input of summer or winter.
if season == "summer":
    advice += "Water your plants regularly and provide some shade.\n"
elif season == "winter":
    advice += "Protect your plants from frost with covers.\n"
else:
    advice += "No advice for this season.\n"

# Determine advice based on the plant type. This is currently hardcoded to "flower" but will be updated to take user input in the future.
if plant_type == "flower":
    advice += "Use fertiliser to encourage blooms."
elif plant_type == "vegetable":
    advice += "Keep an eye out for pests!"
else:
    advice += "No advice for this type of plant."

# Print the generated advice
print(advice)

# TODO: Examples of possible features to add:
# - Refactor the code into functions for better readability and modularity.
# - Store advice in a dictionary for multiple plants and seasons.
# - Recommend plants based on the entered season.
