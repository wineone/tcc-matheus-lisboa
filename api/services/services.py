import copy
from llama_cpp import Llama

async def make_request_llama_cpp(
    model : Llama,
    query: str,
    max_tokens = 400,
    stop : str = "</s>,resposta:,resposta",
    temperature = 0.9
  ):

  stop = stop.split(",")

  stream = model(
    f"pergunta: {query} resposta:",
    max_tokens = max_tokens,
    stop = stop,
    temperature= temperature
  )

  result = copy.deepcopy(stream)
  return {"result":result['choices'][0]['text']}
