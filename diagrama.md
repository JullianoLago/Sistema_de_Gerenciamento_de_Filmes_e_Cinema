# Resolução da atividade 1

Exemplo de resolução da atividade considerando uma das classes solicitadas, incluindo métodos adicionais `get_timestamp` e `iniciar_filme` para complementar a resposta.

```mermaid
classDiagram

    class Movie{
        - _titulo: str
        - _diretor: str
        - _duracao: str
        - _classificacao: Enum
        + timestamp: DateTime
        + exibir_informacoes():str
        + iniciar_filme()
        + get_timestamp():str
    }
```

## Material de estudo:

**Utilizando property:**
https://realpython.com/python-property/

**Utilizando Type hint:**
https://realpython.com/python-type-checking/