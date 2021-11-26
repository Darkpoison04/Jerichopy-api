import random

def UniversalRandomizer(PostValueObject=None):
    tempValueObject = None
    if PostValueObject and type(PostValueObject) is dict:
        tempValueObject = list(PostValueObject)
    elif PostValueObject and (type(PostValueObject) is list or type(PostValueObject) is tuple):
        tempValueObject = PostValueObject
    else:
        tempValueObject = ['true', None]
    RandomChoice = random.choice(tempValueObject)
    return RandomChoice
