from fastapi import fastAPI
app=fastAPI()

@app.get("/home")
def homeapi():
  return {"messege":"hello"}
