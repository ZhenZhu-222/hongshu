from prompt_template import system_template_text,user_template_text
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from output_exmple import XIAOHONGSHU



def genereate_xiaohongshu(subject,api):
    prompt = ChatPromptTemplate.from_messages([
        ("system",system_template_text),
        ("user",user_template_text)
    ])

    model = ChatOpenAI(model = "gpt-3.5-turbo",api_key = api)
    #!!!!!!!!!!!!! 这一步有点难 pydantic 传入的是一个类
    output_parser = PydanticOutputParser(pydantic_object = XIAOHONGSHU)

    generatechain = prompt|model|output_parser
    result = generatechain.invoke({
        "parser_instructions":output_parser.get_format_instructions(),
        "theme":subject
    })

    return result

