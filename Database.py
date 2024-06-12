from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud
import models
import database

app = FastAPI()
DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/Wordgame"

@app.get("/word")
async def read_random_word(db: Session = Depends(database.get_db)):
    word = crud.get_random_word(db)
    return {"word": word.word, "rating": word.rating}

@app.post("/guess")
async def evaluate_guess(guess: str, db: Session = Depends(database.get_db)):
    word = crud.get_random_word(db)
    result = crud.check_guess(word.word, guess)
    return {"correct_letters": result.correct_letters, "correct_positions": result.correct_positions}
