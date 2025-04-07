# OpenAI MCQ Generator

This project uses the OpenAI API to automatically generate **5 multiple-choice questions (MCQs)** from a block of input text. Each question includes 3 options: one correct and two incorrect. The output is printed in both a human-readable and JSON format.

## 🔧 Features

- Parses unstructured text into structured MCQs using OpenAI GPT-4o
- Each question contains:
  - 3 choices
  - Exactly 1 correct answer
- Outputs:
  - Pretty-printed questions and choices
  - JSON-formatted result

---

## 📦 Requirements

Install dependencies with:

```bash
pip install -r requirements.txt
```

Your `requirements.txt` should contain:

```
openai
pydantic
python-dotenv
```

---

## 🔐 Setup

1. Create a `.env` file in the root directory:
    ```env
    OPENAI_API_KEY=your-api-key-here
    ```

2. Activate your virtual environment (if using one), then run:

    ```bash
    python app.py
    ```

---

## 📄 Example Input

```text
Albert Einstein was a theoretical physicist born in Germany in 1879. He is best known for his theory of relativity and the famous equation E=mc². In 1921, he won the Nobel Prize in Physics for his explanation of the photoelectric effect. Einstein moved to the United States in 1933 to escape the Nazis and worked at Princeton. He was also known for his work in civil rights and advocacy for peace. He died in 1955.
```

---

## ✅ Example Output

```text
Question 1: When was Albert Einstein born?
  ✅ 1879
  ❌ 1921
  ❌ 1955

...

{
  "questions": [
    {
      "question": "When was Albert Einstein born?",
      "choices": [
        {"option": "1879", "is_correct": true},
        {"option": "1921", "is_correct": false},
        {"option": "1955", "is_correct": false}
      ]
    },
    ...
  ]
}
```

---

## 🧠 Technologies Used

- Python
- OpenAI SDK (`openai`)
- Pydantic for structured validation
- `dotenv` for environment variable loading

---

## 📂 File Structure

```
├── app.py             # Main script
├── .env               # API key storage (not checked into Git)
├── requirements.txt   # Python dependencies
├── README.md          # Project documentation
```

---

## ✍️ License

This project is free to use and modify. No license restrictions.
