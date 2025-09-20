from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow frontend to talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows any frontend URL, good for testing
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/tariff")
def get_tariff(hs_code: str, country: str):
    mock_data = {
        "1006": {"India": "5% duty", "USA": "2% duty"},
        "0901": {"India": "10% duty", "USA": "0% duty"},
    }
    result = mock_data.get(hs_code, {}).get(country, "No data available")
    return {"hs_code": hs_code, "country": country, "tariff": result}

