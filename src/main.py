import httpx
from fastapi import FastAPI, Query

app = FastAPI()

CLIENT_ID = "q103ptqx0eu9ufghux6jq3fv1m3d8i"
CLIENT_SECRET = "your-secret" # do not hardcode this
REDIRECT_URI = "http://localhost:8000"
AUTH_URL = "https://id.twitch.tv/oauth2/token"


@app.get("/")
async def read_root(
    code: str | None = Query(None),
    scope: str | None = Query(None),
    state: str | None = Query(None),
):  
    print(f"parameters received: {code}, {scope}, {state}")
    auth_params = {
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET,
        "code": code,
        "grant_type": "authorization_code",
        "redirect_uri": REDIRECT_URI,
    }
    print(f"making authentication request to {AUTH_URL} with params {auth_params}")
    client = httpx.Client()
    resp = client.request(
        method="POST",
        url=AUTH_URL,
        params=auth_params,
    )
    print(f"response received: {resp.json()}")
    return {"message": "Hello, this is the root URI!"}
