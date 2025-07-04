from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd


# Import the ML Model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)


# Fast Api APP Object
app = FastAPI()


tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = ["Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore", "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi", "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik", "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli", "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal", "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"]


# Pydantic Model to Validate Incoming Data
class UserInput(BaseModel):
    
    age: Annotated[int, Field(..., gt=0, lt=120, description='Age of the User')]
    weight: Annotated[float, Field(..., gt=0, description='Weight of the User')]
    height: Annotated[float, Field(..., gt=0, description='Height of the User')]
    income_lpa: Annotated[float, Field(..., gt=0, description='Annual Salary of the User')]
    smoker: Annotated[bool, Field(..., description='Is the User a smoker?')]
    city: Annotated[str, Field(..., description='City of the User')]
    
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job', 'business_owner', 'unemployed', 'private_job'], Field(..., description='Occupation of the User')]
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.weight/(self.height**2), 2)
    
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
    
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3


# Fast API Endpoint
@app.post('/predict')
def predict_premium(data: UserInput):
    
    input_df = pd.DataFrame([{
        'bmi': data.bmi,
        'age_group': data.age_group,
        'lifestyle_risk': data.lifestyle_risk,
        'city_tier': data.city_tier,
        'income_lpa': data.income_lpa,
        'occupation': data.occupation
    }])
    
    prediction = model.predict(input_df)[0]
    
    return JSONResponse(status_code=200, content={'predicted_category': prediction})



# myenv\Scripts\activate
# python -m uvicorn app:app --reload