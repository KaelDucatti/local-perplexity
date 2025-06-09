import os
import sys

# Adicionar o diretório src ao path do Python
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from local_perplexity.graph import main

if __name__ == "__main__":
    main()
