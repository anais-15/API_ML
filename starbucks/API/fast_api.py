from fastapi import FastAPI
import uvicorn
import joblib

app = FastAPI()
model = joblib.load("../linear_starbucks.joblib")

@app.get("/")
def root():
		return {'message': 'Hello World'}

@app.get("/predict/")
def index(fats=15, carbs=50, prots=10, fibers=5):
		fats = int(fats)
		carbs = int(carbs)
		prots = int(prots)
		fibers = int(fibers)
		prediction = model.predict([[fats, carbs, prots, fibers]])
		predict = int(prediction[0])
		return {"message": predict}
		