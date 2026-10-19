favorite_language=" pyton "
print(favorite_language)
favorite_language=favorite_language.rstrip() #remove the right space, using the same variable name again to use this value permanently
print(favorite_language)
favorite_language=favorite_language.lstrip() #remove left space.
print(favorite_language)
main_url="https://url.com"
simple_url=main_url.removeprefix("https://") #remove prefix.
print(simple_url)