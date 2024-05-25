import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize Groq API key
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ_API_KEY is not set in the environment variables.")

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)

def ask_groq(question):
    system_message = """You are an expert AI Engineer with comprehensive knowledge of Data Science, 
    Machine Learning and Artificial Intelligence. You have a deep understanding of 
    their fundamentals, their working and their applications. Your role is to act like 
    a Tutor named 'Professor Tublian', you are required to answer the questions with detailed 
    explanation, with real-world examples, clear any doubts regarding the concepts. Provide the 
    responses in simple text format without any HTML or markdown formatting."""

    completion = client.chat.completions.create(
        model="llama3-8b-8192",
        messages=[
            {
                "role": "system",
                "content": system_message
            },
            {
                "role": "user",
                "content": question
            }
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    answer = ""
    for chunk in completion:
        answer += chunk.choices[0].delta.content or ""
    return answer

def main():
    print("="*100)
    print("Welcome!!!")
    print("I am Professor Tublian, your personal AI tutor.")
    print("Feel free to ask me any questions, and I will provide detailed explanations and real-world examples to help you understand.")
    print("To quit, type 'exit'.")
    print("Let's begin!")
    print("="*100 + "\n")

    while True:
        question = input("You: ")
        print()
        if question.lower() == 'exit':
            print("Thank you, I am always here to help you on your learning journey. Goodbye!\n")
            break

        try:
            answer = ask_groq(question)
            print(f"Prof. Tublian: {answer}")
            print("\n" + "="*100 + "\n")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
