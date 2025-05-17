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
            pokemon_data={
                'name':data['name'].capitalize,
                'image':data['sprites']['front_default'],
                'types':[t['type']['name'] for t in data['types']],
                'stats':{s['stat']['name']: s['base_stat'] for s in data['stats']},
                'abilities':[a['ability']['name'] for a in data['abilities']],

            }
        else:
            pokemon_data={'error':'Pokemon not found :( Try again!'}

    return render(request, 'dexapp/pokedex.html',{'pokemon':pokemon_data})


