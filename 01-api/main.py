from fastapi import FastAPI, Response
from config.config import Config
from llama_cpp import Llama
from services.services import *
from typing_extensions import Annotated



# starting the app
app = FastAPI()

# loading the models
# llama
llama_7b = Llama(Config.LLAMA_7B_PATH, n_ctx = Config.CONTEXT_SIZE, n_threads= Config.N_THREADS)
llama_13b = Llama(Config.LLAMA_13B_PATH, n_ctx = Config.CONTEXT_SIZE, n_threads= Config.N_THREADS)

# # alpaca
alpaca_7b = Llama(Config.ALPACA_7B_PATH, n_ctx = Config.CONTEXT_SIZE, n_threads= Config.N_THREADS)
alpaca_13b = Llama(Config.ALPACA_13B_PATH, n_ctx = Config.CONTEXT_SIZE, n_threads= Config.N_THREADS)

# # koala
koala_7b = Llama(Config.KOALA_7B_PATH, n_ctx = Config.CONTEXT_SIZE, n_threads= Config.N_THREADS)
koala_13b = Llama(Config.KOALA_13B_PATH, n_ctx = Config.CONTEXT_SIZE, n_threads= Config.N_THREADS)

# # vicuna
vicuna_7b = Llama(Config.VICUNA_7B_PATH, n_ctx = Config.CONTEXT_SIZE, n_threads= Config.N_THREADS)
vicuna_13b = Llama(Config.VICUNA_13B_PATH, n_ctx = Config.CONTEXT_SIZE, n_threads= Config.N_THREADS)

@app.get("/")
async def hello_world():
  return {"message":"hello world"}

@app.get("/models/llama/7b/")
async def request_llama_7b(
    query : str,
    response: Response,
    temperature: Annotated[float,None] = 0.9,
    stop_tokens: str = "</s>,resposta:,resposta",
    max_tokens: Annotated[int,None] = 400
  ):

  try:
    return await make_request_llama_cpp(
      model = llama_7b, 
      query = query,
      temperature = temperature,
      stop = stop_tokens,
      max_tokens = max_tokens
    )
  except ValueError:
    response.status_code = 400
    return { "detail": [{ "loc": ["query","temperature"],"msg": f"the size of the query plus the max tokens must be lower than {Config.CONTEXT_SIZE} tokens"}] } 

@app.get("/models/llama/13b/")
async def request_llama_13b(
    query : str,
    response: Response,
    temperature: Annotated[float,None] = 0.9,
    stop_tokens: str = "</s>,resposta:,resposta",
    max_tokens: Annotated[int,None] = 400
  ):

  try:
    return await make_request_llama_cpp(
      model = llama_13b, 
      query = query,
      temperature = temperature,
      stop = stop_tokens,
      max_tokens = max_tokens
    )
  except ValueError:
    response.status_code = 400
    return { "detail": [{ "loc": ["query","temperature"],"msg": f"the size of the query plus the max tokens must be lower than {Config.CONTEXT_SIZE} tokens"}] } 
  
@app.get("/models/alpaca/7b/")
async def request_alpaca_7b(
    query : str,
    response: Response,
    temperature: Annotated[float,None] = 0.9,
    stop_tokens: str = "</s>,resposta:,resposta",
    max_tokens: Annotated[int,None] = 400
  ):

  try:
    return await make_request_llama_cpp(
      model = alpaca_7b, 
      query = query,
      temperature = temperature,
      stop = stop_tokens,
      max_tokens = max_tokens
    )
  except ValueError:
    response.status_code = 400
    return { "detail": [{ "loc": ["query","temperature"],"msg": f"the size of the query plus the max tokens must be lower than {Config.CONTEXT_SIZE} tokens"}] } 
  
@app.get("/models/alpaca/13b/")
async def request_alpaca_13b(
    query : str,
    response: Response,
    temperature: Annotated[float,None] = 0.9,
    stop_tokens: str = "</s>,resposta:,resposta",
    max_tokens: Annotated[int,None] = 400
  ):

  try:
    return await make_request_llama_cpp(
      model = alpaca_13b, 
      query = query,
      temperature = temperature,
      stop = stop_tokens,
      max_tokens = max_tokens
    )
  except ValueError:
    response.status_code = 400
    return { "detail": [{ "loc": ["query","temperature"],"msg": f"the size of the query plus the max tokens must be lower than {Config.CONTEXT_SIZE} tokens"}] } 
  
@app.get("/models/koala/7b/")
async def request_koala_7b(
    query : str,
    response: Response,
    temperature: Annotated[float,None] = 0.9,
    stop_tokens: str = "</s>,resposta:,resposta",
    max_tokens: Annotated[int,None] = 400
  ):

  try:
    return await make_request_llama_cpp(
      model = koala_7b, 
      query = query,
      temperature = temperature,
      stop = stop_tokens,
      max_tokens = max_tokens
    )
  except ValueError:
    response.status_code = 400
    return { "detail": [{ "loc": ["query","temperature"],"msg": f"the size of the query plus the max tokens must be lower than {Config.CONTEXT_SIZE} tokens"}] } 
  
@app.get("/models/koala/13b/")
async def request_koala_13b(
    query : str,
    response: Response,
    temperature: Annotated[float,None] = 0.9,
    stop_tokens: str = "</s>,resposta:,resposta",
    max_tokens: Annotated[int,None] = 400
  ):

  try:
    return await make_request_llama_cpp(
      model = koala_13b, 
      query = query,
      temperature = temperature,
      stop = stop_tokens,
      max_tokens = max_tokens
    )
  except ValueError:
    response.status_code = 400
    return { "detail": [{ "loc": ["query","temperature"],"msg": f"the size of the query plus the max tokens must be lower than {Config.CONTEXT_SIZE} tokens"}] } 
  
@app.get("/models/vicuna/7b/")
async def request_vicuna_7b(
    query : str,
    response: Response,
    temperature: Annotated[float,None] = 0.9,
    stop_tokens: str = "</s>,resposta:,resposta",
    max_tokens: Annotated[int,None] = 400
  ):

  try:
    return await make_request_llama_cpp(
      model = vicuna_7b, 
      query = query,
      temperature = temperature,
      stop = stop_tokens,
      max_tokens = max_tokens
    )
  except ValueError:
    response.status_code = 400
    return { "detail": [{ "loc": ["query","temperature"],"msg": f"the size of the query plus the max tokens must be lower than {Config.CONTEXT_SIZE} tokens"}] } 
  
@app.get("/models/vicuna/13b/")
async def request_vicuna_13b(
    query : str,
    response: Response,
    temperature: Annotated[float,None] = 0.9,
    stop_tokens: str = "</s>,resposta:,resposta",
    max_tokens: Annotated[int,None] = 400
  ):

  try:
    return await make_request_llama_cpp(
      model = vicuna_13b, 
      query = query,
      temperature = temperature,
      stop = stop_tokens,
      max_tokens = max_tokens
    )
  except ValueError:
    response.status_code = 400
    return { "detail": [{ "loc": ["query","temperature"],"msg": f"the size of the query plus the max tokens must be lower than {Config.CONTEXT_SIZE} tokens"}] } 
  
