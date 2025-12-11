import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import HTMLResponse
from app.utils.renderer import render_markdown

router = APIRouter()

NOTES_DIRECTORY = "app/storage/notes"
os.makedirs(NOTES_DIRECTORY, exist_ok=True)


# TODO : Upload File
@router.post("/upload")
async def upload_note(file: UploadFile = File(...)):
    if not file.filename.endswith(".md"):
        raise HTTPException(
            status_code=400,
            detail="Invalid file type. Only Markdown files are allowed.",
        )

    file_path = os.path.join(NOTES_DIRECTORY, file.filename)

    with open(file_path, "wb") as f:
        f.write(await file.read())

    return {"message": "File Uploaded", "filename": file.filename}


# TODO : List Saved Notes
@router.get("/list")
async def list_notes():
    notes = [f for f in os.listdir(NOTES_DIRECTORY) if f.endswith(".md")]
    return {"notes": notes}


# TODO : Render .md as .html
@router.get("/{filename}/render", response_class=HTMLResponse)
async def render_note(filename: str):
    path = os.path.join(NOTES_DIRECTORY, filename)

    if not os.path.isfile(path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        with open(path, "r", encoding="utf-8") as f:
            md_text = f.read()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error : {str(e)}")

    try:
        html = render_markdown(md_text)
        return HTMLResponse(content=html)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Markdown Render Error : {str(e)}")


# TODO : Grammer Check
