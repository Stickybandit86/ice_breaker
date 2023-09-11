import os
from langchain import PromptTemplate
from langchain import ChatOpenAI

information = """
    Name: John Doe"""

if __name__ == '__main__':
    print("Hello, world!")
    print(os.environ['OPENAI_API_KEY'])

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary of the person
        2. Two interesting facts about the person
    """

    summary_prompt_template = PromptTemplate(input_variables= ["information"], template=summary_template)

    llm = ChatOpenAI(temperature=0.7, model_name="gpt-3.5-turbo")
    
    chain = LLMChain(llm=llm,prompt= summary_prompt_template)