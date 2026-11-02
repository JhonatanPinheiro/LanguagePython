
import pytest

# Seu código principal (ex: operacoes.py)
def soma(a, b):
  return a + b


# Seu teste com pytest (ex: test_operacoes.py)
def test_soma():
  assert soma(2, 3) == 5

# Instalar a biblioteca: python -m pip install --upgrade pip
# Quando retorna um erro aparece quer dizer que a função não está retornando o valor correto 
# Caso execute e não retorne nada, que dizer que está tudo correto, a função está executando como deveria executar!

Somente rodar no terminal: python -m pytest "scripts/dio/clean_code_boas_praticas_python/testando_usando_assert_usando_pyteste.py"
