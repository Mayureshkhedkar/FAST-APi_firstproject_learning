# this model file is used to create a pydantic model for the 
# data that we want to receive from the client.
from pydantic import BaseModel
class Products(BaseModel):
    id: int
    name: str  
    description: str
    price: float
    quantity: int

    