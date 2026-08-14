import json
import ollama

from config import OLLAMA_MODEL
from quiz.prompt import general_quiz_prompt

def generate_general_quiz(topic,title,difficulty,num_questions):
    prompt = general_quiz_prompt.format(
        topic = topic,
        title=title,
        difficulty=difficulty,
        num_questions=num_questions
    )

    response = ollama.chat(
        model=OLLAMA_MODEL,
        messages=[{
            "role":"user",
            "content":prompt
        }],
        options = {
            "temperature":0.3
        }
    )

    content = response["message"]["content"]

    try:
        quiz = json.loads(content)
        return quiz

    except json.JSONDecodeError:
        start = content.find("{")
        end = content.rfind("}") + 1

        if start != -1 and end !=-1:
            quiz = json.loads(content[start:end])
            return quiz

        raise ValueError("Model Returned Invalid Json.")