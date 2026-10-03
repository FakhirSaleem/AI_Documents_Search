from ollama import chat

def query_rewriter(query,history):

    if history is None:
        return query




    history_content=""

    for question,answer in history[-3:]:
        history_content+=f"""
Previous Question:  {question}
Previous Answer: {answer}

"""





    response=chat(
        model="llama3.2:3b",
        messages=[
            {
                "role": "user",
                "content":f"""
Rewrite the current question into a standalone question.

Use the conversation history to understand references such as:
"it", "they", "this", "that", or "those".

Do not answer the question.
Return only the rewritten question.

Conversation History:
{history_content}

Current Question:
{query}

"""
            }

        ]
    )

    return response.message.content.strip()

