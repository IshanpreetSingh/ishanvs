from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud

app = FastAPI()

@app.get("/word")
async def read_random_word(db: Session = Depends(get_db)):
    word = crud.get_random_word(db)
    return {"word": word.word, "rating": word.rating}

@app.post("/guess")
async def evaluate_guess(guess: str, db: Session = Depends(get_db)):
    word = crud.get_random_word(db)
    result = crud.check_guess(word.word, guess)
    return {"correct_letters": result.correct_letters, "correct_positions": result.correct_positions}   