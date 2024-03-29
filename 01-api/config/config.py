class Config:
  ## cntx size
  CONTEXT_SIZE = 2048
  N_THREADS = 5

  # llama models
  LLAMA_7B_PATH = "models/llama/ggml-llama-7B-q4_0.bin"
  LLAMA_13B_PATH = "models/llama/ggml-llama-13B-q4_0.bin"

  # llama 2 models
  LLAMA_2_7B_PATH = "models/llama-2/llama-2-7b-chat.ggmlv3.q4_1.bin"
  LLAMA_2_13B_PATH = "models/llama-2/llama-2-13b-chat.ggmlv3.q4_1.bin"

  # alpaca models
  ALPACA_7B_PATH = "models/alpaca/ggml-alpaca-7b-q4.bin"
  ALPACA_13B_PATH = "models/alpaca/ggml-alpaca-13b-4bit.bin"

  # koala models
  KOALA_7B_PATH = "models/koala/koala-7B-4bit-128g.GGML.bin"
  KOALA_13B_PATH = "models/koala/koala-13B-4bit-128g.GGML.bin"

  # vicuna models
  VICUNA_7B_PATH = "models/vicuna/ggml-vicuna-7b-1.1-q4_1.bin"
  VICUNA_13B_PATH = "models/vicuna/ggml-vicuna-13b-1.1-q4_3.bin"

  # vicuna 1.5 models
  VICUNA1_5_7B_PATH = "models/vicuna-1.5/vicuna-7b-v1.5-16k.ggmlv3.q4_1.bin"
  VICUNA1_5_13B_PATH = "models/vicuna-1.5/vicuna-13b-v1.5-16k.ggmlv3.q4_1.bin"