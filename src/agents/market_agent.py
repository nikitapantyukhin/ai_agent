import os
from dotenv import load_dotenv
from smolagents import CodeAgent, DuckDuckGoSearchTool, LiteLLMModel

load_dotenv()

def create_agent():
    hf_token = os.getenv("HF_TOKEN")
    
    model = LiteLLMModel(
    # model_id="huggingface/Qwen/Qwen2.5-72B-Instruct",
    model_id="huggingface/Qwen/Qwen2.5-Coder-32B-Instruct",
    api_key=hf_token
)
    
    return CodeAgent(
        tools=[DuckDuckGoSearchTool()],
        model=model,
        max_steps=20,
        verbosity_level=1
    )

agent = create_agent()