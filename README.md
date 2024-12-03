# Student Management System Backend Cosmocloud-backend-task

A FastAPI-powered backend for managing student data with MongoDB Atlas as the database. This API allows for easy management of student information including creation, retrieval, updating, and deletion.

## 🛠️ Tech Stack

- **Language**: Python
- **Framework**: FastAPI
- **Database**: MongoDB Atlas (M0 Free Cluster)
- **Async Library**: Motor (for MongoDB async operations)

## 🌐 Deployment

The app is deployed and accessible at [Your Base URL](https://cosmocloud-backend-task-1diz.onrender.com/) (replace this with your actual deployed URL).

## 🚀 Features

- **CRUD Operations**: Create, Read, Update, and Delete student records.
- **MongoDB Integration**: All data is stored and retrieved from a cloud-based MongoDB Atlas database.
- **FastAPI Documentation**: Automatically generated interactive documentation available at `/docs`.

## 🔧 Installation

### Clone the repository:

```bash
git clone https://github.com/yourusername/student-management-api.git
cd student-management-api
```
Create a virtual environment and install dependencies:
```
python -m venv env
source env/bin/activate  # On Windows: .\env\Scripts\activate
pip install -r requirements.txt
```
Run the app locally:
```
uvicorn main:app --reload
```
Your app will be running at http://127.0.0.1:8000.

# 🗄️ MongoDB Configuration
Set up the MONGO_URI in the .env file with your MongoDB Atlas connection string.
```
env
MONGO_URI="mongodb+srv://<username>:<password>@cosmocloudtask.gkbif.mongodb.net/?retryWrites=true&w=majority"
```
📄 API Endpoints
```
GET /students: Fetch all student records.
GET /students/{id}: Fetch a specific student by ID.
POST /students: Create a new student record.
PUT /students/{id}: Update an existing student by ID.
DELETE /students/{id}: Delete a student by ID.
```
👨‍💻 Developer
Project by: Mridul Goel
GitHub: github.com/mridulgoel03
