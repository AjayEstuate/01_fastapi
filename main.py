from fastapi import FastAPI

#Creating an instance of FastAPI
app = FastAPI()

#Creating function
#Using an instance of Fast API and creating get mapping
@app.get('/')
def index():
    return {'data':{'name':'Ajay Kumar'}}

@app.get("/about")
def about():
    return {"data" : {"About page"}}
