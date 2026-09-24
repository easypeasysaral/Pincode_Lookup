from fastapi import FastAPI

app = FastAPI(
    title= "Pincode Lookup API",
    description="This will auto-fill state and city using the pincode"
)

@app.get("/")
def root():
    return{
        "message" : "Pincode-Lookup API"
    }