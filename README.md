# FastAPI Project – Quick Start Guide

## Prerequisites

Before running the project, ensure you have **Python 3.10+** installed.

### 1. Install Python

Download and install the latest Python version from:  
https://www.python.org/downloads/

After installation, verify it using:

```bash
python --version
pip --version
```

If both commands return version numbers, Python and pip are installed successfully.

---

## Getting Started

### 2. Clone the Repository

```bash
git clone https://github.com/your-username/your-fastapi-project.git
cd your-fastapi-project
```

*(Replace the link with your actual repository URL.)*

---

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

Activate it:

- **Windows:**
  ```bash
  venv\Scripts\activate
  ```

- **macOS/Linux:**
  ```bash
  source venv/bin/activate
  ```

---

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

This installs all dependencies listed in `requirements.txt`.

If `requirements.txt` doesn’t exist, install FastAPI and Uvicorn manually:

```bash
pip install fastapi uvicorn
```

---

### 5. Run the Server

```bash
uvicorn app.main:app --reload
```

By default, the app runs at:  
http://127.0.0.1:8000

---

### 6. API Documentation

FastAPI automatically generates two interactive documentation UIs:

- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc

---

### 7. Environment Variables (Optional)

Create a `.env` file in your root directory:

```env
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
SECRET_KEY=your_secret_key
```

Use `python-dotenv` to load these values if required:
```bash
pip install python-dotenv
```

---

### 8. Build for Production (Optional)

For production, run:

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000
```

Or use **Gunicorn + Uvicorn workers**:

```bash
gunicorn app.main:app -w 4 -k uvicorn.workers.UvicornWorker
```

---

## Summary

1. Install Python  
2. Clone the repository  
3. Create & activate a virtual environment  
4. Run `pip install -r requirements.txt`  
5. Start the app with `uvicorn app.main:app --reload`  
6. Visit the docs at `/docs`

That’s it! Your FastAPI backend is up and running 
