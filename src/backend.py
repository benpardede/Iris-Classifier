from fastapi import FastAPI, Request, Response, status
import pickle

app = FastAPI()
model_path = 'model/classifier.pkl'

@app.get("/")
def root():
    return {"message": "your API si UP!"}

#check model
@app.get('/check-model')
def check_model(response: Response): 
    try:
        with open(model_path, 'rb') as model :
            model = pickle.load(model)
            result = {'status' : 'ok', 'message' : 'model is ready to use'}
            return result
    except Exception as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status' : 'eror', 'message' : 'model is not found', 'detail_error': str(e)}

#predict    
@app.post('/predict')
async def predict(response: Response, request: Request):
    try:
        data = await request.json()
        
        sepal_length = data['sepal_length']
        sepal_width = data['sepal_width']
        petal_length = data['petal_length']
        petal_width = data['petal_width']
        
        #read model
        with open(model_path, 'rb') as model :
            model = pickle.load(model)
            
        #label prediction
        label = ['iris-setosa', 'iris-versicolor', 'iris-virginica']
        
        #predict
        try: 
            result = model.predict([[sepal_length, sepal_width, petal_length, petal_width]])[0]
            result = label[result]
            return {
                'status' : 'ok',
                'message' : 'return prediction',
                'result' : result
            }        
            
        except Exception as e :
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {
                'status' : 'error',
                'message' : 'data is not valid',
                'detail_error' : str(e)
            }
            
    except Exception as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {'status' : 'eror', 'message' : 'model is not found', 'detail_error': str(e)}