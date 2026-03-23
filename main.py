from fastapi import FastAPI, Body
from fastapi.responses import PlainTextResponse
from google import genai

client = genai.Client(api_key="AIzaSyD5bbOl1opNLtv4_8xSqDCQyPitHooqrU8")

app = FastAPI()

@app.post("/solve", response_class=PlainTextResponse)
def solve_problem(question: str = Body(...)):

    prompt = f"""
    Generate ONLY Java code.
    No explanation.
    No markdown.
    Proper indentation required.

    Problem:
    {question}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    output = response.text.strip()

    # Remove markdown if present
    output = output.replace("```java", "").replace("```", "").strip()

    return output

