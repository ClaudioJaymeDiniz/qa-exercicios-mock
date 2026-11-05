# Installing Dependencies
```sh
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```


# Test Execution
```sh
python -m pytest ./test/* --cov
```

# Trabalho Prático - Mock Objects e Testes Unitários (Custom Stack)

Projeto desenvolvido em Python utilizando **pytest** e **pytest-cov** para validação de testes unitários, cobertura de código de 100% da classe `CustomStack` e implementação do ordenador de números da Mega Sena (`NumberAscOrder`).

## Estrutura do Projeto
- `src/custom_stack_class.py`: Implementação da pilha customizada e exceções.
- `src/number_asc_order.py`: Classe responsável por coletar e ordenar de forma ascendente os números da pilha.
- `test/`: Suíte de testes unitários cobrindo todos os cenários e garantindo 100% de cobertura.

## Execução dos Testes e Cobertura
Para executar os testes e verificar a cobertura de código utilizando o pytest-cov:
```
pytest --cov=src --cov-report=term-missing
````