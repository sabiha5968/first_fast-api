# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


from fastapi import FastAPI
app= FastAPI()
@app.get("/")
async def root():
    return {"message":"Hello world"}

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
