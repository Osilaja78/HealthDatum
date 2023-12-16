# Contributing guide.

This project has its `main` branch protected, so, whatever change you're proposing should be done in a personal branch which will then be reviwed and merged into the `main` branch. Follow these steps to get started.

- Clone the repository.
```bash
git clone https://github.com/Osilaja78/HealthDatum.git
```
- Create and use a new branch.
```bash
git checkout -b branch-name
```
Replace `branch-name` with a suitable name, most preferrably, it should refer to the current feature you're working on.
- Then continue to whatever part of the project you would like to make changes, frontend or backend.


## Frontend.

The frontend is built using Next.js and Tailwind CSS, so basic knowledge of these two frameworks is required before being able to contribute.

### Requirements.
You need to have the following installed on your PC.
- Node.js (v20.5.0 of higher).

### To run the project.
- Once you clone the repo, move to the frontend directory
```bash
cd frontend
```
- Install the requred dependencies
```bash
npm install
```
- Create a `.env` file in the root directory of the frontend and copy the environment variables from the `.env.example`, fill the vars with the appropriate values.
- Finally, run the project.
```bash
npm run dev
```

## Backend

The backend is built using FastAPI, so basic knowledge of the framework is required before being able to contribute.

### Requirements.
You need to have the following installed on your PC
- Python (v3.10.0 or higher).
- MySQL

### To run the project.
- Once you clone the repository, move to the backend directory.
```bash
cd backend
```
- Create a python virtual environment.
```bash
python -m venv env
```
- Activate your virtual environment.
```bash
env\scripts\activate
```
- Install all requred dependencies.
```bash
pip install -r requirements.txt
```
- Finally run the project.
```bash
python main.py
# or
uvicorn main:app --reload
```
