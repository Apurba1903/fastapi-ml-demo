# 🏥 Insurance Premium Category Predictor

A machine learning web application that predicts insurance premium categories based on user demographics, health indicators, and lifestyle factors.

## 📋 Project Overview

This project demonstrates a complete ML pipeline from model training to deployment, featuring:
- **Machine Learning Model** for premium category prediction
- **FastAPI** backend with RESTful API endpoints  
- **Pydantic** for robust data validation
- **Streamlit** frontend for user interaction

## 🛠️ Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| **ML Model** | Scikit-learn/Custom | Premium category prediction |
| **Backend API** | FastAPI | RESTful API endpoints |
| **Data Validation** | Pydantic | Request/response validation |
| **Frontend** | Streamlit | Interactive web interface |
| **Data Processing** | Pandas | Data manipulation |

## 🏗️ Architecture

```
┌─────────────────┐    HTTP Request    ┌─────────────────┐
│   Streamlit     │ ─────────────────> │   FastAPI       │
│   Frontend      │                    │   Backend       │
│                 │ <───────────────── │                 │
└─────────────────┘    JSON Response   └─────────────────┘
                                              │
                                              │ Pydantic
                                              │ Validation
                                              ▼
                                       ┌─────────────────┐
                                       │   ML Model      │
                                       │   Prediction    │
                                       └─────────────────┘
```

## 📊 Features

### Machine Learning Model
- Predicts insurance premium categories (Low, Medium, High)
- Uses features like age, BMI, lifestyle, income, and occupation
- Trained on insurance dataset with demographic and health data

### FastAPI Backend
- RESTful API with `/predict` endpoint
- Automatic API documentation with Swagger UI
- JSON request/response handling
- Error handling and status codes

### Pydantic Data Validation
- Automatic request validation
- Type checking and data conversion
- Clear error messages for invalid inputs
- Schema documentation

### Streamlit Frontend
- Interactive web interface
- Real-time input validation
- Visual feedback for predictions
- Clean, professional design

## 🚀 Getting Started

### Prerequisites
```bash
Python 3.8+
pip package manager
```


### 📁 Project Structure
```
insurance-premium-predictor/
│
├── app.py                 # FastAPI application
├── streamlit_app.py       # Streamlit frontend
├── model.pkl              # Trained ML model
├── requirements.txt       # Dependencies
└── README.md             # This file
```

## 🏃‍♂️ Running the Application

### 1. Start FastAPI Backend
```bash
uvicorn app:app --reload --port 8000
```
- API will be available at: `http://localhost:8000`
- Interactive docs at: `http://localhost:8000/docs`

### 2. Start Streamlit Frontend
```bash
streamlit run streamlit_app.py
```
- Web app will be available at: `http://localhost:8501`

## 📡 API Endpoints

### POST `/predict`
Predicts insurance premium category based on user input.

**Request Body:**
```json
{
    "age": 30,
    "weight": 70.0,
    "height": 1.75,
    "income_lpa": 5.0,
    "smoker": false,
    "city": "Mumbai",
    "occupation": "private_job"
}
```

**Response:**
```json
{
    "predicted_category": "Medium"
}
```

## 🔧 Data Validation Schema

The application uses Pydantic models for data validation:

```python
class UserInput(BaseModel):
    age: int
    weight: float
    height: float
    income_lpa: float
    smoker: bool
    city: str
    occupation: str
```

## 📈 Model Features

The ML model considers the following factors:

| Feature | Description | Type |
|---------|-------------|------|
| **Age** | User's age | Integer |
| **BMI** | Calculated from weight/height | Float |
| **Income** | Annual income in LPA | Float |
| **Lifestyle Risk** | Derived from smoking status | Boolean |
| **City Tier** | Urban classification | Categorical |
| **Occupation** | Job category | Categorical |

## 🎯 Premium Categories

- **Low**: Budget-friendly premiums for low-risk profiles
- **Medium**: Standard rates for average risk profiles  
- **High**: Premium rates for high-risk profiles

## 🛡️ Error Handling

The application includes comprehensive error handling:
- **Input validation** errors with clear messages
- **API connection** error handling
- **Model prediction** error catching
- **HTTP status code** management

## 🔄 Development Workflow

1. **Model Development**: Train and validate ML model
2. **API Development**: Create FastAPI endpoints with Pydantic validation
3. **Frontend Development**: Build Streamlit interface
4. **Integration Testing**: Test API-Frontend communication
5. **Deployment**: Deploy to production environment

## 📝 Future Enhancements

- [ ] Add model performance metrics dashboard
- [ ] Implement user authentication
- [ ] Add data visualization charts
- [ ] Include model explainability features
- [ ] Add batch prediction capability
- [ ] Implement caching for faster responses

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/new-feature`)
3. Commit changes (`git commit -am 'Add new feature'`)
4. Push to branch (`git push origin feature/new-feature`)
5. Create Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@apurba1903](https://github.com/apurba1903)
- Email: apurba1903@gmail.com

## 🙏 Acknowledgments

- Thanks to @campusx for the amazing content
- FastAPI and Streamlit documentation teams

---

*Built with ❤️ using FastAPI, Pydantic, and Streamlit*