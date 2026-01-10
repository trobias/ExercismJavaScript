def response(hey_bob):
    texto = hey_bob.strip()
    if texto == "":
        return "Fine. Be that way!"
    elif texto.endswith("?") and texto.isupper():
        return "Calm down, I know what I'm doing!"
    elif texto.endswith("?"):
        return "Sure."
    elif texto.isupper():
        return "Whoa, chill out!"
    else:
        return "Whatever."