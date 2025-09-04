# Zemen Cars

**Zemen Cars** is a Django-based backend for a car dealership platform. Admins can add, update, and delete cars, while users can browse available cars and register accounts.

---

## Features

### Admin
- Add new cars
- Update car details
- Delete cars
- Manage users

### User
- View list of cars
- View individual car details
- Register an account (signup)

### Optional/Future
- Favorite cars
- Search and filter cars
- JWT authentication for secure login

---

## Database Schema (ERD)

The project has the following main entities:

1. **User**
   - id, username, email, password, is_admin

2. **Car**
   - id, make, model, year, price, mileage, condition, description, image, created_at, created_by (FK → User)

3. **Favorite** (Optional)
   - id, user_id (FK → User), car_id (FK → Car)

Relationships:
- One User → Many Cars (admin adds cars)
- One User → Many Favorites
- One Car → Many Favorites (many users can favorite the same car)

> See ERD diagram in the Google Doc for visualization.

---

## API Endpoints

### Auth
- `POST /api/auth/signup/` → Register a new user

### Cars
- `GET /api/cars/` → List all cars
- `GET /api/cars/<id>/` → Retrieve a single car
- `POST /api/cars/` → Add a new car (admin only)
- `PUT /api/cars/<id>/` → Update a car (admin only)
- `DELETE /api/cars/<id>/` → Delete a car (admin only)

### Favorites (Optional)
- `POST /api/favorites/` → Add a car to favorites
- `GET /api/favorites/` → List user’s favorite cars
- `DELETE /api/favorites/<id>/` → Remove a favorite

---

## Setup Instructions

1. **Clone the repository**

```bash
git clone https://github.com/elaZgrt/zemen_cars.git
cd zemen_cars
```

2. **Create virtual environment**

```bash
python -m venv env
env\Scripts\activate      # Windows
# source env/bin/activate   # Mac/Linux
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Apply migrations**

```bash
python manage.py makemigrations
python manage.py migrate
```

5. **Create superuser (admin)**

```bash
python manage.py createsuperuser
```

6. **Run the server**

```bash
python manage.py runserver
```

7. **Access the admin panel**

```
http://127.0.0.1:8000/admin/
```

8. **Test API endpoints**
Use Postman or a browser:
- List cars: `http://127.0.0.1:8000/api/cars/`
- Signup: `http://127.0.0.1:8000/api/auth/signup/`

---

## Notes
- Images uploaded for cars are stored in the `media/` folder.
- Admin-only endpoints require a superuser account.
- Database is currently SQLite (can switch to PostgreSQL for production).

---

## License
This project is open source and free to use.
