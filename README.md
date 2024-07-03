# Real-Time Attendance Monitoring System

## Objective
Develop an attendance monitoring system enabling real-time attendance tracking and data management.

## Project Description
This project implements a real-time attendance monitoring system using ARUCO tags for accurate tracking and Django for user registration and database management. The system updates the attendance records in real-time, significantly reducing manual labor and improving efficiency.

## Features
- **Accurate Tracking:** Utilizes ARUCO tags for precise attendance tracking.
- **Real-Time Updates:** Integrates OpenCV with Django for real-time ARUCO marker detection and website updates.
- **User Management:** Implements user registration and database management using Django.
- **Efficiency Improvement:** Reduces tracking time by 60% for 200+ users and improves attendance efficiency.

## Project Structure
- **tests.py:** Contains the test cases for the Django application.
- **urls.py:** Defines the URL patterns for routing in the Django application.
- **views.py:** Handles the logic for rendering templates and processing requests.

## Requirements
To run this project, you need the following dependencies:
- Python 3.x
- Django
- OpenCV
- NumPy
- ARUCO library

You can install the required Python packages using:
```sh
pip install django opencv-python numpy opencv-contrib-python
```

## Running the Project
1. Ensure all project files (`tests.py`, `urls.py`, `views.py`, etc.) are in the appropriate Django project structure.
2. Apply migrations to set up the database:
```sh
python manage.py migrate
```
3. Run the Django development server:
```sh
python manage.py runserver
```
4. Access the application in your web browser at `http://127.0.0.1:8000/`.

## Acknowledgements
This project was inspired by the need for efficient and accurate attendance tracking systems, leveraging modern computer vision techniques and web development frameworks.