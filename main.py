from fastapi import FastAPI
from pdf2image import convert_from_path
from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)


from pydantic import BaseModel


class URL(BaseModel):
    pdf_url: str
    

from pathlib import Path
from glob import glob
app=FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello World from STOPS!!"}

@app.post("/")
async def pdftoimage(url: URL):
    images = convert_from_path(url, first_page=1, last_page=1)
    for i, image in enumerate(images):
        fname = "image" + str(i) + ".png"
        image.save(fname, "PNG")