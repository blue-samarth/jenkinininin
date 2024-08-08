import fire

def greeting(name = "World"):
    # return f"Hello, {name}!"
    # we will greet in French like a gentleman 
    return f"Bonjour, {name}!"

if __name__ == "__main__":
    fire.Fire(greeting)