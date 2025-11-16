''' Actual Greet Method'''
def greet(name=None):
    if name:
        return f"Welcome, {name}!"
    else:
        return "Welcome!"
