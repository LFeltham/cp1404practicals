COLOUR_HEXES = {"beige": "#f5f5dc", "bisque1": "#ffe4c4", "aliceblue": "#f0f8ff", "antiquewhite2": "#eedfcc",
                "antiquewhite1": "#ffefdb", "aquamarine2": "#76eec6", "aquamarine1": "#7fffd4",
                "azure1": "#f0ffff", "azure3": "#c1cdcd", "azure4": "#838b8b"}

colour_name = input("Enter a colour name: ").lower()
while colour_name != "":
    print(f"The code for \"{colour_name}\" is {COLOUR_HEXES.get(colour_name)}")
    colour_name = input("Enter a colour name: ").lower()
