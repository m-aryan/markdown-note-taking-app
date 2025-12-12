# Markdown Note-Taking App (FastAPI)

This project is a simple Markdown Note-Taking API built using **FastAPI**.
It allows you to:

* upload Markdown files
* list saved notes
* render Markdown as HTML
* run grammar checks using LanguageTool

This is the solution for the **Markdown Note-Taking App** project from Roadmap.sh.
**Project URL:** [https://roadmap.sh/projects/markdown-note-taking-app](https://roadmap.sh/projects/markdown-note-taking-app)

---

# Features

* **Upload .md files** to the server
* **List all notes** stored on the backend
* **Render markdown → HTML**
* **Grammar Check** using LanguageTool (supports raw text or saved file)
* **File-based storage**, no database required

---

# Project Structure

```
markdown_note_app/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── notes.py
│   ├── services/
│   │   └── grammar.py
│   ├── utils/
│   │   └── renderer.py
│   ├── storage/
│   │   └── notes/
├── .gitignore
├── requirements.txt
└── README.md
```

---

# Requirements

* Python 3.10+
* FastAPI
* Uvicorn
* LanguageTool (installed automatically via `language_tool_python`)

---

# Running the Project Locally

## 1. Create and activate a virtual environment

```
python -m venv venv
```

Activate it:

### Windows:

```
venv\Scripts\activate
```

### macOS/Linux:

```
source venv/bin/activate
```

---

## 2. Install dependencies

```
pip install -r requirements.txt
```

---

## 3. Start the FastAPI server

```
uvicorn app.main:app --reload
```

Your server runs at:

```
http://127.0.0.1:8000
```

Interactive API docs:

```
http://127.0.0.1:8000/docs
```

---

# API Endpoints

## **1. Create Note from Raw Markdown**

```
POST /notes/create
```

Body example:

```json
{
  "md_text": "# Hello World"
}
```

---

## **2. Upload a Markdown File**

```
POST /notes/upload
```

Form-data field:

* `file`: `.md` file

---

## **3. List Notes**

```
GET /notes
```

---

## **4. Render Markdown as HTML**

```
GET /notes/{filename}/render
```

---

## **5. Grammar Check**

Supports raw Markdown or saved filename.

```
POST /notes/grammar-check
```

### Option A — Raw Markdown

```json
{
  "md_text": "This are bad sentence."
}
```

### Option B — File in storage

```
POST /notes/grammar-check?filename=test.md
```

---

# Testing

Use the built-in SwaggerUI docs:

```
http://localhost:8000/docs
```

---

# Storage

All saved `.md` files are stored in:

```
app/storage/notes/
```

These files persist unless the folder is deleted.
