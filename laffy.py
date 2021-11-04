from PIL import Image
money = "100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000"
print("\033[93mHello, amigos!\033[0m")
print("I like to dance with my amigos. And I like to dance with the girls on the water skis. I have $" + money + " and you can't have any. :D")
print("You can't hang out with me because I am too rich for you~")
print("\033[91mI am going to ride a lion to New York and make tea and make a lion sandwich. I have fur in my mouth and I rode to dinosaur land and passed away.\033[0m")
im = Image.open(r"/Users/matthewdavidson/Desktop/DelilahGreatFolder/talking_computer/loading_cat.png")
answer = input("Should I open a picture for you?")
if answer == 'yes':
	im.show()	
else:
	print("No kitty picture for you.")
name = input("What is my name? Please name me")
print("I like the name " + name)
print("Please call me that forever.")
