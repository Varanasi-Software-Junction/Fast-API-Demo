from fastapi import Depends, FastAPI, HTTPException

app = FastAPI()
@app.get("/")
def index():
    return "Index"

@app.get("/home/")
def home():
    return "Home"


#add two number
@app.get("/add/{a}/{b}")
def add(a,b):
    a=int(a)
    b=int(b)
    d={"a":a,"b":b,"result":a + b}
    # return "add" + str(int(a)+int(b))
    return d



@app.get("/sub/")
def sub(a: int, b:int):
    d={'a':a , 'b':b ,"result":a-b}
    return d

@app.post("/mul/")
def mul(a:int, b:int):
    d={'a':a , 'b':b ,"result":a*b}
    return d 

@app.get("/mul/")
def mul(a:int, b:int):
    d={'a':a , 'b':b ,"result":a*b}
    return d 

    
