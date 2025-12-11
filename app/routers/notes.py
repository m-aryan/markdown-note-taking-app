import os
from fastapi import APIRouter, UploadFile, File, HTTPException, Query
from fastapi.responses import HTMLResponse
from app.utils.renderer import render_markdown
from app.services.grammer import check_grammar

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
    return {f"notes : {notes}"}


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
@router.post("/grammar-check")
async def grammar_check(
    md_text: str = None,
    filename: str = Query(None),
):

    if md_text:
        mistakes = check_grammar(md_text)
        return {"mistakes": mistakes}

    if filename:
        file_path = os.path.join(NOTES_DIRECTORY, filename)

        if not os.path.isfile(file_path):
            raise HTTPException(status_code=404, detail="File not found")

        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error : {str(e)}")

        mistakes = check_grammar(text)
        return {"mistakes": mistakes}

    raise HTTPException(status_code=400, detail="No text or filename provided")
