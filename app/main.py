from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello, world!"}

#     @app.post()
#     @app.put()
#     @app.delete()
# And the more exotic ones:

#     @app.options()
#     @app.head()
#     @app.patch()
#     @app.trace()


# @app.options(): This decorator defines a special route that handles OPTIONS requests.
# OPTIONS requests are used in cross-origin resource sharing(CORS) to check if a server
# will accept the requested cross-origin request.

# ex
# @app.options("/")
# async def options_root(request: Request):
#     return {
#         "Allow": "GET, POST, OPTIONS",
#         "Access-Control-Allow-Origin": "*",  # Replace with your actual allowed origins
#         "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
#         "Access-Control-Allow-Headers": "X-Requested-With, Content-Type, Accept"
#     }


# @app.options("/items/{item_id}")
# async def options_item(request: Request):
#     return {
#         "Allow": "GET, PUT, DELETE, OPTIONS",
#         "Access-Control-Allow-Origin": "*",  # Replace with your actual allowed origins
#         "Access-Control-Allow-Methods": "GET, PUT, DELETE, OPTIONS",
#         "Access-Control-Allow-Headers": "X-Requested-With, Content-Type, Accept"
#     }
