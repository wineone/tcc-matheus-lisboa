class Config:
  ## cntx size
  CONTEXT_SIZE = 2048
  N_THREADS = 4

  # llama models
  LLAMA_7B_PATH = "models/llama/ggml-llama-7B-q4_0.bin"
  LLAMA_13B_PATH = "models/llama/ggml-llama-13B-q4_0.bin"

  # alpaca models
  ALPACA_7B_PATH = "models/alpaca/ggml-alpaca-7b-q4.bin"
  ALPACA_13B_PATH = "models/alpaca/ggml-alpaca-13b-4bit.bin"

  # koala models
  KOALA_7B_PATH = "models/koala/koala-7B-4bit-128g.GGML.bin"
  KOALA_13B_PATH = "models/koala/koala-13B-4bit-128g.GGML.bin"

  # vicuna models
  VICUNA_7B_PATH = "models/vicuna/ggml-vicuna-7b-1.1-q4_1.bin"
  VICUNA_13B_PATH = "models/vicuna/ggml-vicuna-13b-1.1-q4_3.bin"