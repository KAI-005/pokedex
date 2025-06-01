from django.shortcuts import render
import requests

# Create your views here.

def search(request):
    pokemon_data={}
    query=request.GET.get("pokemon")
    if query:
        url=f'https://pokeapi.co/api/v2/pokemon/{query.lower()}'
        response=requests.get(url)
        if response.status_code==200:
            data=response.json()
            pokemon_data = {
    'name': data['name'].capitalize(),
    'image': data['sprites']['front_default'],
    'types': [t['type']['name'] for t in data['types']],
    'abilities': [a['ability']['name'] for a in data['abilities']],
    'hp': data['stats'][0]['base_stat'],
    'attack': data['stats'][1]['base_stat'],
    'defense': data['stats'][2]['base_stat'],
    'special_attack': data['stats'][3]['base_stat'],
    'special_defense': data['stats'][4]['base_stat'],
    'speed': data['stats'][5]['base_stat'],
}
        else:
            pokemon_data={'error':'Pokemon not found :( Try again!'}

    return render(request, 'dexapp/pokedex.html',{"pokemon":pokemon_data})


