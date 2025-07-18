def word_counter(book):
    words = book.split()
    number = len(words)
    return number

def character_counter(book):
   
    chardict = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,"n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"y":0,"x":0,"z":0,"æ":0,"â":0,"ê":0,"ë":0,"ô":0}
    for char in book.strip().lower():
        char = char.lower()
        if char in chardict:
            chardict[char] +=1
    return chardict

def sort_chars(chars_dict):
    return chars_dict[1]


