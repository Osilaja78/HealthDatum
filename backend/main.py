from fastapi import FastAPI
from api.routers import auth, admin, onboarding
from fastapi.middleware.cors import CORSMiddleware
# from api.models import users
from api.database import engine
import uvicorn
from api.models import models


app = FastAPI(title="HealthDatum")


origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    # Frontend deplyment link should be added here
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Initialize database migration
models.Base.metadata.create_all(bind=engine)


@app.get('/')
def index():
    """
    Index page.

    Return:
        message: welcome message.
    """

    return {
        'message': 'Welcome to HealthDatum, an electronic health record system that provides easy means of managing clinical data.'
    }

# Include routes from other router files
# app.include_router(auth.router)
app.include_router(admin.router)
app.include_router(onboarding.router)


# Run uvicorn server
if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, reload=True)
