print('The temperature in the room is 25 degree celsiuus')
temp_celsius = 25
print(f"The room temperature is {temp_celsius} degrees celsiuus")
word = 'temperature'
canonical_form = word.capitalize()
print(f"The cannonical form of '{word}' is '{canonical_form}'")
temp_in_celsius = 25
temp_in_fahrenheot = (temp_in_celsius * (9/5)) + 32

def analysis_temp(temp):
    if temp < 0:
        return "It's Freezing!"
    elif 0 <= temp < 20:
        return "It's Cool!"
    else:
        return "It's Warm!"

temp = 25
analysis = analysis_temp(temp)
print(f"The temperature of {temp} degree celsius : {analysis}.")
