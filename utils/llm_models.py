import os

from dotenv import load_dotenv
from openai import AsyncAzureOpenAI, AsyncOpenAI, OpenAI

from agents import OpenAIChatCompletionsModel

envpath = ".env"
load_dotenv(dotenv_path=envpath, override=True)


def azure_openai_model():
    azure_modelname = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
    azure_client = AsyncAzureOpenAI(
        api_key=os.getenv("AZURE_OPENAI_API_KEY"),
        azure_endpoint=os.getenv("AZURE_OPENAI_API_ENDPOINT"),
        api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    )
    azure_llm = OpenAIChatCompletionsModel(
        model=azure_modelname, openai_client=azure_client
    )
    return azure_llm


def mistral_nemon_model():
    model_name = "mistralai/mistral-nemo-instruct-2407"
    mistral_client = AsyncOpenAI(
        api_key=os.getenv("MISTRAL_NEMONADE_API_KEY"),
        base_url=os.getenv("MISTRAL_NEMONADE_API_URL"),
    )
    mistral_llm = OpenAIChatCompletionsModel(
        model=model_name, openai_client=mistral_client
    )
    return mistral_llm
