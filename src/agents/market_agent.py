import os
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

load_dotenv()

def create_agent():
    hf_token = os.getenv("HF_TOKEN")
    
    model = LiteLLMModel(
        model_id="huggingface/meta-llama/Meta-Llama-3-8B-Instruct", 
        api_key=hf_token
    )
    
    return CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=model,
        max_steps=25,
        verbosity_level=1
    )

# Создаем экземпляр для экспорта
agent = create_agent()