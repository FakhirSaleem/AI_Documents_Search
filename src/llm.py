from ollama import chat

def generate_answer(context,query,history=None):
    history_text=""




    if history:
        for question,answer in history:
            history_text+=f"""
Previous Question:{question}
Previous Answer:{answer}
"""




    response=chat(
        model="llama3.2:3b",
        messages=[
            {
                "role":"user",
                "content":f"""
Answer the question using the context below and the conversation history to understand references such as "it", "they", or "this".
Do not use any outside knowledge. Answer the question using only the provided context and conversation history.

If the answer is not supported by the provided context, say exactly:
"I don't know based on the provided documents."



CITATION RULES:

1. Every factual sentence must have a citation immediately after it.

2. Use only source numbers that appear in the context, such as [1], [2], or [3].

3. A citation means that the source directly supports the sentence immediately before it.

4. Do NOT cite a source just because it is related to the topic.

5. If one source supports a sentence, cite only that source.
   Example:
   Python is a programming language. [1]

6. If two or more sources directly contain the same information, you may cite both.
   Example:
   Python is commonly used in data science. [1] [2]

7. If different sentences come from different sources, cite them separately.
   Example:
   Python is a programming language. [1]
   Python is commonly used in data science. [2]

8. Do not put one citation at the end of multiple sentences.

9. Never invent a source number.

10. Do not make a factual statement unless the provided context directly supports it.

11. Before writing each sentence, verify that the cited source directly contains or clearly states the information in that sentence.

12. Never combine information from one source with a citation from another source.

13. If the context does not directly answer the question, say exactly:
"I don't know based on the provided documents."

14. Keep the answer concise.

15. The citation number must exactly match the source number in the context.


Example of correct formatting:
Python is a programming language. [1]
Python is easy to learn. [1]
Python is commonly used in data science. [1] [2]

Conversation History:
{history_text}

Context:
{context}

Question:
{query}

"""

            }
        ]
    )

    return response.message.content




