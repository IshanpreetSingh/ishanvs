from datetime import datetime, timedelta, timezone
from fastapi import FastAPI, Depends, HTTPException, status, Request
from fastapi.responses import JSONResponse, HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
import jwt

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

JWT_SECRET_KEY = "your_jwt_secret_key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRY_MINUTES = 15

fake_users_db = {
    "jatin": {
        "username": "jatin",
        "password": "2020"
    }
}

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def create_access_token(payload: dict, expires_delta: timedelta):
    expire = datetime.now(tz=timezone.utc) + expires_delta
    payload.update({"exp": expire})
    encoded_jwt = jwt.encode(payload, JWT_SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

@app.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if username not in fake_users_db or fake_users_db[username]["password"] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRY_MINUTES)
    access_token = create_access_token(payload={"sub": username}, expires_delta=access_token_expires)
    response = JSONResponse(content={"access_token": access_token, "token_type": "bearer"})
    response.set_cookie(key="access_token", value=access_token, httponly=True, path="/")
    return response

@app.get("/welcome", response_class=HTMLResponse)
async def welcome(request: Request):
    return """
    <html>
    <head>
        <title>Welcome Page</title>
        <meta http-equiv="refresh" content="10;url=/">
    </head>
    <body>
        <h1>Hey! Nice to see you again.</h1>
    </body>
    </html>
    """

@app.get("/")
async def home(request: Request):
    access_token = request.cookies.get("access_token")
    if access_token and is_jwt_valid(access_token):
        return {"message": "Welcome!"}
    else:
        return JSONResponse(content={"message": "No valid token found"}, status_code=status.HTTP_401_UNAUTHORIZED)

def is_jwt_valid(jwtoken):
    try:
        jwt.decode(jwtoken, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return True
    except jwt.PyJWTError:
        return False

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
