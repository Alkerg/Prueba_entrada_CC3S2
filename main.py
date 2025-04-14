from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

class Question(BaseModel):
    description: str
    options: List[str]
    correct_answer: str

questions_db = []

@app.post("/questions/", status_code=201)
def create_question(question: Question):
    if question.correct_answer not in question.options:
        raise HTTPException(status_code=400, detail="Correct answer must be one of the options.")
    
    questions_db.append(question)
    return {"message": "Question created successfully"}
