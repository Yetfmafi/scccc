from fastapi import FastAPI, HTTPException
from mangum import Mangum
import requests
from typing import List, Dict

app = FastAPI(
    title="FREE STALCRAFT API",
    description="Прокси для работы с Production API Stalcraft.",
    version="1.0.0",
)

BASE_URL = "https://eapi.stalcraft.net"
API_TOKEN = "eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJhdWQiOiI5MDgiLCJqdGkiOiI5YzgzMWRkNmQyNTVmOTJmYTYyMmM0OGQyNTJiZTdiYjNkZGRkNDA0MjJlNTUxMTAwOWFmY2E5OGNiYTZkYjNhY2ZkODcxNDVjYmMwNzliOCIsImlhdCI6MTczMzA2NjAwOS4xMzM4MywibmJmIjoxNzMzMDY2MDA5LjEzMzgzNCwiZXhwIjoxNzY0NjAyMDA5LjAyMDAyNSwic3ViIjoiIiwic2NvcGVzIjpbXX0.QtWALi-tafeWtSrPPrm4AY8OE82jPcK5SyZAmDdp7T0xqA2PHZaK7-Y4cUnoIjXSH7CUz5gkHMfSWeKPbbewnzFSxgDv5HDmTTb3Z4weNM5WD0a6xzhdwogzIqDo_Rx7Zl2NnV_zF9FaSBF5gm6484locDV2PuszIADP52o1-k3VQLQeF65uV8CAvA4DZ2El-zRs2K_O3S-WpVLdxzo6m1AGX0CQNcy2KZCQs47FgobkYJxbiCxCjKV0xYjLXojbTgiiZ_QaRnYIebIRMq3ACZWcwAZBLu-UyyBgauzBqzIpAhjQS-YRFBAAaUrsteS82RTuP2mcSccDYYgrYKTR7GjskdAgDFRfMQqNavd2DJrEr2CbAEMurHChtyN_C5VREHtmASuZ1KklcPsrzFvjFTa1d81bTvqulj16DXfZTzMMl-INjtZhfmepM_gDcSKWcUm0NSjBKOnDkPu8Tp0xP8-y1m4x5ac6vTnhFvjs6KmEquH9cnoWWpyfvIZJj3loQuUXsZaTExaISITfPLmSPGI-9K6cjM-cYYnFqbB2n-ilM6huFmMeKilvIqS08wueGtrYGkzah_vUdQn0EYzfSYcwrhaapU-mSRsyRuA593jq-eH2eyioF710LRZQ727g1Z6CzHy70lB7ky_EvSggDliQPJgJjaJ4CKS-6UAXaSM"  # Замените на ваш токен

@app.get("/api/regions", summary="Список регионов")
async def get_regions() -> List[Dict[str, str]]:
    try:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        response = requests.get(f"{BASE_URL}/regions", headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/{region}/emission", summary="Статус выбросов в регионе")
async def get_emission_status(region: str) -> Dict[str, str]:
    try:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        url = f"{BASE_URL}/{region}/emission"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/{region}/friends/{character}", summary="Список друзей персонажа")
async def get_friends_list(region: str, character: str) -> List[str]:
    try:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        url = f"{BASE_URL}/{region}/friends/{character}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/api/{region}/auction/{item}/history", summary="История цен на аукционе")
async def get_item_price_history(region: str, item: str, limit: int = 20, offset: int = 0) -> Dict[str, List[Dict[str, str]]]:
    try:
        headers = {"Authorization": f"Bearer {API_TOKEN}"}
        url = f"{BASE_URL}/{region}/auction/{item}/history"
        params = {"limit": limit, "offset": offset}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(status_code=500, detail=str(e))

handler = Mangum(app)
