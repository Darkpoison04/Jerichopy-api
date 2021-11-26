import requests
import json
import random
#https://some-random-api.ml/endpoints

class animals:

    def dog(self):
        res = requests.get('https://some-random-api.ml/animal/dog')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image
        
    def cat(self):
        res = requests.get('https://some-random-api.ml/animal/cat')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image

    def panda(self):
        res = requests.get('https://some-random-api.ml/animal/panda')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image


    def fox(self):
        res = requests.get('https://some-random-api.ml/animal/fox')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image


    def red_panda(self):
        res = requests.get('https://some-random-api.ml/animal/red_panda')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image


    def koala(self):
        res = requests.get('https://some-random-api.ml/animal/koala')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image

    def bird(self):
        res = requests.get('https://some-random-api.ml/animal/birb')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image

    def raccoon(self):
        res = requests.get('https://some-random-api.ml/animal/raccoon')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image
    
    def kangaroo(self):
        res = requests.get('https://some-random-api.ml/animal/kangaroo')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image


    def random_animal(self):
        list = ["kangaroo","dog","cat","panda","fox","red_panda","koala","birb","raccoon"]
        animal = list[random.randint(0, 8)]
        res = requests.get(f'https://some-random-api.ml/animal/{animal}')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        image = response.get('image')
        return fact , image , animal

    def get_animal_image(self, animal_name):
        if animal_name == 'bird': animal_name = 'birb'
        if animal_name == 'red panda': animal_name = 'red_panda'
        res = requests.get(f'https://some-random-api.ml/animal/{animal_name}')
        if not res : return "Error"
        response = json.loads(res.text)
        image = response.get('image')
        return image
    
    def get_animal_fact(self, animal_name):
        if animal_name == 'bird': animal_name = 'birb'
        if animal_name == 'red panda': animal_name = 'red_panda'
        res = requests.get(f'https://some-random-api.ml/animal/{animal_name}')
        if not res : return "Error"
        response = json.loads(res.text)
        fact = response.get('fact')
        return fact
    


