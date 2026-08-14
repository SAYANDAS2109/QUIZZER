import json
import ollama

from quiz.rag.retriever import retrieve_documents


def generate_rag_quiz(
    vectorstore,
    title,
    difficulty,
    num_questions,
    query
):

    documents = retrieve_documents(
        vectorstore=vectorstore,
        
        query=query,
        k=20
    )

    if not documents:
        raise ValueError(
            "No relevant information was found in the uploaded documents."
        )

    context_parts = []

    for document in documents:

        source = document.metadata.get(
            "source",
            "Unknown source"
        )

        page = document.metadata.get(
            "page",
            "Unknown page"
        )

        context_parts.append(
            f"""
SOURCE: {source}
PAGE: {page}

CONTENT:
{document.page_content}
"""
        )

    context = "\n\n".join(context_parts)

    prompt = f"""
You are an expert quiz generator.

Your task is to create a balanced multiple-choice quiz
from the supplied document context.

IMPORTANT RULES:

1. Use ONLY information contained in the document context.
2. Do NOT use outside knowledge.
3. The quiz title is ONLY a display name.
4. Do NOT use the quiz title to determine the subject.
5. Determine concepts from the document content.
6. Generate exactly {num_questions} questions.
7. Every question must have exactly four options.
8. There must be exactly one correct answer.
9. Questions must match the requested difficulty.
10. Do not repeat questions.
11. Avoid asking several questions about the same small piece of text.
12. Cover DIFFERENT concepts, principles, definitions, mechanisms,
    relationships and important facts whenever possible.
13. Distribute questions across different document sections/chunks.
14. Prefer important concepts over minor details.
15. Every question must be directly answerable from the supplied context.
16. Include a short explanation.
17. Identify the specific concept tested.
18. Include the source filename.
19. Include the page number where the answer was obtained.
COVERAGE REQUIREMENT:

Before generating questions, internally identify the important
concepts present in the document context.

Then distribute the questions across those concepts.

For example, if the context contains:

- Concept A
- Concept B
- Concept C
- Concept D

do NOT generate most questions from Concept A.

Instead, create a balanced quiz covering A, B, C and D
according to the amount and importance of information available.

Do not invent concepts that are not present in the context.
Quiz title:
{title}

Difficulty:
{difficulty}

Requested questions:
{num_questions}

Document context:
{context}

Return ONLY valid JSON.

Use exactly this structure:
{{
    "title": "{title}",
    "difficulty": "{difficulty}",
    "questions": [
        {{
            "question": "Question text",
            "options": [
                "Option A",
                "Option B",
                "Option C",
                "Option D"
            ],
            "correct_answer": "Option A",
            "explanation": "Explanation based only on the document.",
            "topic": "Specific concept tested",
            "source": "Source filename",
            "page": 1
        }}
    ]
}}
"""

    response = ollama.chat(
        model="gemma3:4b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        format="json"
    )

    content = response["message"]["content"]

    quiz = json.loads(content)

    return quiz