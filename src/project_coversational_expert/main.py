#!/usr/bin/env python
# src/project_coversational_expert/main.py
import sys
from project_coversational_expert.crew import Chat

# Main Chat Loop
def chat_loop():
    print("Welcome to the Kunway Coversational Agent!")
    while True:
        user_input = input("Enter your query (type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Thank you for using the chatbot. Goodbye!")
            break

        inputs = {
            'topic': user_input.strip()
        }

        result = Chat().crew().kickoff(inputs=inputs)
        print(result)


        # Ask for feedback
        feedback = input("Would you like to refine this response? (Yes/No): ").strip().lower()
        if feedback == "yes":
            refined_input = input("Please provide your feedback or additional query: ")

            refined_input = {
            'topic': refined_input.strip()
            }
            result = Chat().crew().kickoff(inputs=refined_input)
            print(result)
        else:
            print("Okay, let's continue.")

def run():
    print("Running the CrewAI project")
    chat_loop()

if __name__ == "__main__":
    chat_loop()

# #!/usr/bin/env python
# # src/project_ai_reporter/main.py
# import sys
# from crew import Chat

# # Main Chat Loop
# def chat_loop(self, message):
#     print("Welcome to the Kunway Chatbot!")
#     while True:
#         user_input = input("Enter your query (type 'exit' to quit): ")
#         user_input = message.payload.get("Enter your query (type 'exit' to quit): ")
#         session_id = message.payload.get("session_id", "")

#         history = self.get_session_history(session_id)


#         if user_input.lower() == 'exit':
#             print("Thank you for using the chatbot. Goodbye!")
#             break

#         inputs = {
#             'topic': user_input.strip()
#         }

#         result = Chat().crew().kickoff(inputs=inputs)
#         print(result)

#         def build_prompt_with_history(self, history, user_input):
#             prompt = ""
#             for entry in history:
#                 role = entry["role"]
#                 content = entry["content"]
#                 prompt += f"{role}: {content}\n"

#             prompt += f"user: {user_input}\n"
#             return prompt



#         # Ask for feedback
#         feedback = input("Would you like to refine this response? (Yes/No): ").strip().lower()
#         if feedback == "yes":

#             refined_input = input("Please provide your feedback or additional query: ")
#             context = self.build_prompt_with_history(history, refined_input)

#             refined_input = {
#             'topic': context.strip()
#             }
#             result = Chat().crew().kickoff(inputs=refined_input)
#             print(result)
#         else:
#             print("Okay, let's continue.")

# if __name__ == "__main__":
#     chat_loop()
