import os
from django_cassiopeia import cassiopeia as cass
from django.http import JsonResponse

#summoner = Summoner(name='куколдовод', region='RU')
#api_key = os.getenv('API_KEY')
# cass.set_riot_api_key(api_key)
# cass.set_default_region('RU')


def get_summoner(name: str, region: str):
    summoner = cass.Summoner(name=name, region=region)
    return {'name': summoner.name, 'level': summoner.level, 'avatar': summoner.profile_icon.url}
