
# AWS Task Tracker

A Python Flask-based task management web application developed as a hands-on cloud engineering portfolio project.

The project focuses on backend development, database persistence, version control, and future deployment to Amazon Web Services (AWS).

## Project Overview

AWS Task Tracker allows users to create and view tasks through a simple web interface. Tasks are stored in an SQLite database, allowing them to persist after application restarts.

This project is being developed incrementally to demonstrate practical skills in Python, Flask, databases, Git, GitHub, and AWS cloud infrastructure.

## Technologies Used

- Python 3
- Flask
- SQLite
- Git and GitHub
- Ubuntu (WSL)
- AWS EC2 (planned)
- Docker (planned)

## Current Features

- Add new tasks through a web interface
- View saved tasks
- Store tasks in an SQLite database
- Preserve tasks after application restarts
- Validate task titles with a 200-character limit

## Run Locally

Clone the repository:

```bash
git clone https://github.com/SOUFIANEEDDERMOUNE/aws-task-tracker.git
cd aws-task-tracker
```

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
python -m pip install -r requirements.txt
```

Start the application:

```bash
python app.py
```

Open http://127.0.0.1:5000 in your browser.

Note: The current application uses Flask's development server and is intended for local development only.

## Development Roadmap

- [x] Create Flask application
- [x] Implement task creation and listing
- [x] Integrate SQLite persistent storage
- [x] Set up Git and GitHub version control
- [ ] Add task completion and deletion
- [ ] Improve the user interface
- [ ] Containerize the application with Docker
- [ ] Deploy to AWS EC2
- [ ] Configure production web serving and security
- [ ] Add monitoring and deployment automation

## Documentation

Screenshots and technical implementation notes are being collected throughout development. They will be added to this repository as the project progresses.

## Author

Soufiane Ed-dermoune

Cloud Computing graduate building practical skills in Cloud Engineering, IT Infrastructure, and DevOps.
