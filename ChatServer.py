from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import JSONResponse
import db_lib
#uvicorn ChatServer:app --reload
app = FastAPI()

inprogress_orders={}

@app.post("/")
async def handle_request(request: Request):
    payload= await request.json()
    intent= payload['queryResult']['intent']['displayName']
    parameters=payload['queryResult']['parameters']
    output_contexts=payload['queryResult']['outputContexts']
    
    
    intent_handler_dict = {
        'order.add-context:ongoing-order': add_to_order,
        #'order.remove - context: ongoing-order': remove_from_order,
        #'order.complete - context: ongoing-order': complete_order,
        'track.order - context: ongoing-tracking': track_order
    }
    return intent_handler_dict[intent](parameters)


def add_to_order(parameters:dict):
    food_items=parameters['food-item']
    quantities=['number']
    if len (food_items) != len(quantities):
        fulfillmentText="Sorry I didn't understand. Can you please specify food items and quantities"
    else:
        fulfillmentText=f"Recevied {food_items} and {quantities} in the  backend"
    return JSONResponse(content={'fulfillmentText':fulfillmentText})





def track_order(parameters:dict):
    order_id=parameters['order_id']
    
    order_status=db_lib.get_order_status(order_id)
    
    if order_status:
        fulfillmentText=f"The order status for order id: {order_id} is: {order_status}"
    else:
        fulfillmentText=f"No order found with order id: {order_id}"
    
    return JSONResponse(content={'fulfillmentText':fulfillmentText})
    


