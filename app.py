import os
from pydantic import BaseModel
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Input text for generating multiple-choice questions
text = (
    "Albert Einstein was a theoretical physicist born in Germany in 1879. "
    "He is best known for his theory of relativity and the famous equation E=mc². "
    "In 1921, he won the Nobel Prize in Physics for his explanation of the photoelectric effect. "
    "Einstein moved to the United States in 1933 to escape the Nazis and worked at Princeton. "
    "He was also known for his work in civil rights and advocacy for peace. "
    "He died in 1955."
)

# Define the Pydantic models for the response
class Choice(BaseModel):
    option: str
    is_correct: bool

class MCQ(BaseModel):
    question: str
    choices: list[Choice]

class MCQResponse(BaseModel):
    questions: list[MCQ]

completion = client.beta.chat.completions.parse(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are an expert at generating multiple-choice questions. You will be given a text and must return exactly 5 questions. Each question must have 3 choices, with one correct and two incorrect options. The correct option must be marked using the `is_correct` field."},
        {"role": "user", "content": text}
    ],
    response_format=MCQResponse,
)

quiz = completion.choices[0].message.parsed

# Print the questions and choices in a pretty format
for i, q in enumerate(quiz.questions, 1):
    print(f"\nQuestion {i}: {q.question}")
    for choice in q.choices:
        marker = "✅" if choice.is_correct else "❌"
        print(f"  {marker} {choice.option}")


# print the JSON Response
print(quiz.model_dump_json(indent=2))
