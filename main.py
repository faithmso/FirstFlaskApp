from flask import Flask
from helper import pets

app = Flask(__name__)

@app.route('/')
def index():
  return f'''
  <h1> Adopt a pet! </h1>
  <p> Browse through the links below to find your new furry friend:</p>
  <ul>
    <li><a href="/animals/dogs">Dogs</a></li>
    <li><a href="/animals/cats">Cats</a></li>
    <li><a href="/animals/rabbits">Rabbits</a></li>
  </ul>
  '''

@app.route('/animals/<pet_type>')
def animals(pet_type):
  html = '<h1> List of {} </h1>'.format(pet_type)
  html += '<ul>'
  for index, pet in enumerate(pets.get(pet_type, [])):
    name = pet.get('name', '')
    html += f'<li><a href="/animals/{pet_type}/{index}">{name}</a></li>'

  html += '</ul>'
  return html

@app.route('/animals/<pet_type>/<int:pet_id>')
def pet(pet_type, pet_id):
  #pet_list = pets.get(pet_type)
  #pet = pet_list[pet_id]
  pet = pets.get(pet_type, [])[pet_id] 

  name = pet.get('name', '')
  age = pet.get('age', '')
  breed = pet.get('breed', '')
  description = pet.get('description', '')
  url = pet

  return f'''
  <h1> {pet['name']} </h1>
  <img src="{pet['url']}" />
  <p>{pet['description']}</p>
  <ul>
    <li>Breed: {pet['breed']}</li>
    <li>Age: {pet['age']}</li>
  </ul>
  '''