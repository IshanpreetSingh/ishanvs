from sqlalchemy.orm import Session
from sqlalchemy.sql.expression import func as sql_func
from models import Word
import random

class GuessResult:
    def _init_(self, correct_letters, correct_positions):
        self.correct_letters = correct_letters
        self.correct_positions = correct_positions

def get_random_word(db: Session) -> Word:
    return db.query(Word).order_by(sql_func.rand()).first()

def check_guess(word: str, guess: str) -> GuessResult:
    correct_letters = 0
    correct_positions = 0
    for i in range(len(word)):
        if guess[i] == word[i]:
            correct_positions += 1
        elif guess[i] in word:
            correct_letters += 1
    return GuessResult(correct_letters, correct_positions)