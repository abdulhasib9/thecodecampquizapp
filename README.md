
# TheCodeCamp Quiz App

Welcome to **TheCodeCamp Quiz App** – a Django-based quiz application designed primarily for **YouTube MCQ video creations**. This app allows users to take quizzes based on different IT exams, featuring multiple-choice questions, correct answer display, and a dynamic, interactive interface for an engaging experience. The app is built to help creators develop and present MCQs for their educational YouTube content.

## Purpose

This app is designed to assist YouTube content creators in generating and presenting Multiple-Choice Question (MCQ) quizzes for IT exam practice. The goal is to create an easy-to-use platform that allows users to take quizzes, display correct answers, and view detailed question descriptions in a user-friendly interface, all while being responsive and engaging for viewers.

## Tech Stack

- **Backend:** Django (Python-based web framework)
- **Frontend:** HTML5, CSS3, JavaScript, Bootstrap 5, Font Awesome 5
- **Database:** SQLite (or any database supported by Django)
- **Image Handling:** Django's built-in support for image uploads
- **Version Control:** Git

## Features

- **Dynamic Quizzes:** Create and take quizzes based on multiple exams and subjects.
- **Multiple Question Types:** Supports multiple-choice questions with single or multiple correct answers.
- **Exhibits Support:** Attach images to questions and options for a more engaging quiz experience.
- **Progress Tracking:** Track quiz progress with a progress bar.
- **Toggle Answer Visibility:** Show correct answers and question descriptions with a button toggle.
- **Responsive Design:** A fully responsive UI built with Bootstrap 5 for seamless experience across devices.

## Requirements

- Python 3.x
- Django 4.x
- SQLite (or any other database of your choice)
- Bootstrap 5
- Font Awesome 5

## Installation

### Step 1: Clone the repository

```bash
git clone https://github.com/your-username/thecodecamp-quiz-app.git
cd thecodecamp-quiz-app
```

### Step 2: Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Step 3: Install required dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Set up the database

Run the following commands to create the database and apply migrations:

```bash
python manage.py migrate
```

### Step 5: Create a superuser

To access the admin panel, create a superuser account:

```bash
python manage.py createsuperuser
```

Follow the prompts to set up the superuser.

### Step 6: Run the development server

Start the Django development server:

```bash
python manage.py runserver
```

You can now access the app at [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Project Structure

- `quiz_app/`: Contains all the main logic for the quiz, including models, views, and templates.
- `templates/`: Holds the HTML files used for rendering the quiz.
- `static/`: Includes CSS, JavaScript, and image files used across the project.
- `requirements.txt`: List of dependencies to install for the project.
- `manage.py`: Command-line utility for Django tasks.
  
## Models

### Exam Model
Represents an exam with a name and unique code.

```python
class Exam(models.Model):
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
```

### Question Model
Represents a question, associated with an exam, and supports exhibits and descriptions.

```python
class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    text = models.TextField()
    exhibit = models.ImageField(upload_to='static/exhibits/', blank=True, null=True)
    is_multiple = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)
```

### Option Model
Represents options for each question. Options can be marked as correct and can also contain exhibits.

```python
class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.CharField(max_length=255, blank=True, null=True)
    is_correct = models.BooleanField(default=False)
    exhibit = models.ImageField(upload_to='static/exhibits/', blank=True, null=True)
```

### Quiz Model
Associates a quiz with an exam and multiple questions.

```python
class Quiz(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    code = models.CharField(max_length=50, unique=True)
    questions = models.ManyToManyField(Question)
```

## Features & Functionality

- **Admin Panel:** Easy-to-use interface to manage quizzes, exams, questions, and options.
- **Question Display:** Display questions with options and support for exhibits.
- **Toggle Show Answers:** Click to toggle the display of correct answers and question descriptions.
- **Question Navigation:** Move between questions with 'Next' and 'Previous' buttons.
- **Responsive Design:** Mobile-friendly design for quiz taking.

## Screenshots

Here are some screenshots of the app in action:

![Quiz Question](https://example.com/screenshot1.png)
*Question page with options and exhibit*

![Quiz Progress](https://example.com/screenshot2.png)
*Progress bar displaying quiz progress*

## Future Enhancements

- **User Authentication:** Allow users to sign up and track their quiz progress.
- **Question Randomization:** Randomize questions and options for each quiz attempt.
- **Analytics:** Display user performance analytics for taken quizzes.
  
## Contributing

We welcome contributions to improve the project! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

## License

This project is licensed under the MIT License.
