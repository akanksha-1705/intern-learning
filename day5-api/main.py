from fastapi import FastAPI

app = FastAPI(title="Day 5 API")


@app.get("/about")
def about():
    return {
        "name": "Aakanksha",
        "skills": [
            "Python",
            "Git",
            "React"
        ]
    }