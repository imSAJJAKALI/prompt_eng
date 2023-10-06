import os
import openai
from dotenv import load_dotenv, find_dotenv

_=load_dotenv(find_dotenv())

# openai.api_key=os.environ["OPEN_API_KEY"]

from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

response = ChatOpenAI(openai_api_key="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",temperature=0.3)

# customer_mail="Hey ! Where are you? Why did you miss board meeting.Come right now We need to talk You behaviour to miss the meeting was disgusting"

# customer_style="Indian english is very calm and respecatful tone"

# prompt="""Translate the text that is delimated by tripple backticks into a style is {style}, trxt : ```{text}``` """

# prompt_template = ChatPromptTemplate.from_template(prompt)

# customer_message = prompt_template.format_messages(
#     style=customer_style,
#     text=customer_mail
# )

# customer_response = response(customer_message)



# chat = response.predict("3-8 ?")


from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

memory = ConversationBufferMemory()

Conversation = ConversationChain(
    llm= response,
    memory=memory,
    verbose=True

)

res1 = Conversation.predict(input="Hi my name is Sajjak Ali")

res2 = Conversation.predict(input="What is 2-10")

res3 = Conversation.predict(input="What is my name ?")

print(memory.buffer)






# ------------------> LangChani Chat_Models Start <-------------------

# from langchain.chat_models import ChatOpenAI
# from langchain.schema import (
#     AIMessage,
#     HumanMessage,
#     SystemMessage
# )

# chat = ChatOpenAI(openai_api_key="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",temperature=0.3)

# print(chat([AIMessage(content="Translate this sentence from English to French: I love programming.")]))

# --------------------> LangChain Chat Models end <-------------------------




# -------------> OPENAI START <-----------------

# def get_completion(prompt,model="gpt-3.5-turbo"):
#     messages=[{"role":"user","content":prompt}]
#     response = openai.ChatCompletion.create(
#         model=model,
#         messages=messages,
#         temperature=1
#     )

#     return response.choices[0].message["content"]

# response = get_completion("what is 3+1")

# print(response)

# ----------------> OPEN AI END <------------------