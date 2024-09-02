# Flashcard API

A simple Django REST Framework API for managing flashcards.

## Features

- List all flashcards
- View details of a specific flashcard
- Create new flashcards
- Update existing flashcards
- Delete flashcards

## Setup

1. Clone the repository
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run migrations:
   ```
   python manage.py migrate
   ```
4. Start the development server:
   ```
   python manage.py runserver
   ```

## API Endpoints

- GET `/api/card-list`: List all flashcards
- GET `/api/card-detail/<str:pk>/`: View details of a specific flashcard
- POST `/api/card-create/`: Create a new flashcard
- POST `/api/card-update/<str:pk>`: Update an existing flashcard
- DELETE `/api/card-delete/<str:pk>`: Delete a flashcard

## Models

The `Flashcards` model includes:
- `question`: The question or prompt
- `answer`: The answer to the question
- `category`: The category of the flashcard

## Technologies Used

- Django
- Django REST Framework
- SQLite (default database)


