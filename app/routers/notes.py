import os
from fastapi import APIRouter, UploadFile, File, HTTPException

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
