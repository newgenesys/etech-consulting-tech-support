import json
from fastapi import FastAPI, APIRouter

description = """
Deloitte API helps communicate with other services. 🚀

## Welcome

You can **read our welcome from /**.

## Rooot

You will be able to:

* **Create xyz** (_implemented_).
* **Update xyz** (_implemented_).
* **Read xyz** (_implemented_).
* **Read a particular xyz** (_implemented_).
* **Search xyz by other properties** (_not implemented_).
* **Delete xzy** (_not implemented_).
"""

tags_metadata = [
    {
        "name": "default",
        "description": "The root endpoint of this API.",
    },
    {
        "name": "Word Search",
        "description": "Operations with Word Search.",
    },
    {
        "name": "Deloitte Externall",
        "description": "Manage Deloitte External. So _fancy_ they have their own docs.",
        "externalDocs": {
            "description": "Deloitte data set external docs",
            "url": "https://fastapi.tiangolo.com/",
        },
    },
]

app = FastAPI(title="Deloitte API",
              description=description,
              version="0.0.1",
              terms_of_service="http://example.com/terms/",
              contact={
                  "name": "John Doe",
                  "url": "http://linkedin.com/in/contact/",
                  "email": "jdoe@example.com",
              },
              license_info={
                  "name": "Apache 2.0",
                  "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
              },
              openapi_tags=tags_metadata,
              openapi_url="/api/v1/openapi.json",
              docs_url="/documentation",
              redoc_url="/redocumentation",
              )

api_router = APIRouter()


# Root endpoint: it is the first point of entry
#  for the app when someone access the web app
# example.com/

@api_router.get("/", status_code=200)
def root() -> dict:
    """
    Root GET
    """
    return {"message": "Welcome to our API root endpoint."}


# Search and return update string after replacements
@api_router.get("/wordsearch/{text}/", status_code=200, tags=["Word Search"])
def search_replace(*, text: str) -> dict:
    """
    Receives a text as input, searches for specific words and returns an updated string with those words replaced
    """
    text = text.replace("Oracle", "Oracle\xa9") 
    text = text.replace("Google", "Google\xa9")
    text = text.replace("Microsoft", "Microsoft\xa9")
    text = text.replace("Amazon", "Amazon\xa9")
    text = text.replace("Deloitte", "Delloitte\xa9")    
	
    return {"results": str(text)}


app.include_router(api_router)

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")
