from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow your frontend to call this backend
origins = ["*"]  # for testing; later you can restrict to your frontend URL
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/tariff")
def get_tariff(hs_code: str, country: str):
    # This is a placeholder. Replace with real tariff data logic later
    return {
        "hs_code": hs_code,
        "country": country,
        "tariff": "5% duty"
    }
