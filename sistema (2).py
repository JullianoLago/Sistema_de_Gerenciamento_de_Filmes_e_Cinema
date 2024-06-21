from datetime import datetime

# Classe para representar um filme
class Movie:
    def __init__(self, titulo: str, diretor: str, duracao: int, classificacao: str) -> None:
        self._titulo = titulo
        self._diretor = diretor
        self._duracao = duracao
        self._classificacao = classificacao

    @property
    def titulo(self) -> str:
        return self._titulo

    @property
    def diretor(self) -> str:
        return self._diretor

    @property
    def duracao(self) -> int:
        return self._duracao

    @property
    def classificacao(self) -> str:
        return self._classificacao

    @titulo.setter
    def titulo(self, novo_titulo: str) -> None:
        self._titulo = novo_titulo

    @diretor.setter
    def diretor(self, novo_diretor: str) -> None:
        self._diretor = novo_diretor

    @duracao.setter
    def duracao(self, nova_duracao: int) -> None:
        self._duracao = nova_duracao

    @classificacao.setter
    def classificacao(self, nova_classificacao: str) -> None:
        self._classificacao = nova_classificacao

    def exibir_informacoes(self) -> str:
        infos = f"""
        Filme: {self._titulo}
        Diretor: {self._diretor}
        Duração: {self._duracao} minutos
        Classificação: {self._classificacao}
        """
        print(infos)
        return infos


# Classe para representar uma sala de cinema
class CinemaHall:
    def __init__(self, hall_number: int, capacity: int) -> None:
        self._hall_number = hall_number
        self._capacity = capacity
        self._status = "disponível"

    @property
    def hall_number(self) -> int:
        return self._hall_number

    @property
    def capacity(self) -> int:
        return self._capacity

    @property
    def status(self) -> str:
        return self._status

    @hall_number.setter
    def hall_number(self, novo_hall_number: int) -> None:
        self._hall_number = novo_hall_number

    @capacity.setter
    def capacity(self, nova_capacity: int) -> None:
        self._capacity = nova_capacity

    @status.setter
    def status(self, novo_status: str) -> None:
        self._status = novo_status

    def disponivel(self) -> bool:
        return self._status == "disponível"

    def reservar(self) -> bool:
        if self.disponivel():
            self._status = "ocupada"
            return True
        return False

    def liberar(self) -> None:
        self._status = "disponível"


# Classe para representar uma exibição de um filme
class Screening:
    def __init__(self, filme: Movie, sala: CinemaHall, data: str, hora: str) -> None:
        self._filme = filme
        self._sala = sala
        self._data = data
        self._hora = hora

    @property
    def filme(self) -> Movie:
        return self._filme

    @property
    def sala(self) -> CinemaHall:
        return self._sala

    @property
    def data(self) -> str:
        return self._data

    @property
    def hora(self) -> str:
        return self._hora

    @filme.setter
    def filme(self, novo_filme: Movie) -> None:
        self._filme = novo_filme

    @sala.setter
    def sala(self, nova_sala: CinemaHall) -> None:
        self._sala = nova_sala

    @data.setter
    def data(self, nova_data: str) -> None:
        self._data = nova_data

    @hora.setter
    def hora(self, nova_hora: str) -> None:
        self._hora = nova_hora

    def agendar(self) -> str:
        infos = f"Filme '{self._filme.titulo}' agendado na sala {self._sala.hall_number} em {self._data} às {self._hora}."
        print(infos)
        return infos

    def cancelar(self) -> str:
        infos = f"Exibição de '{self._filme.titulo}' na sala {self._sala.hall_number} em {self._data} às {self._hora} foi cancelada."
        print(infos)
        return infos


# Classe para representar uma reserva de assentos para uma exibição
class Reservation:
    def __init__(self, exibicao: Screening, nome_cliente: str, numero_assentos: int) -> None:
        self._exibicao = exibicao
        self._nome_cliente = nome_cliente
        self._numero_assentos = numero_assentos

    @property
    def exibicao(self) -> Screening:
        return self._exibicao

    @property
    def nome_cliente(self) -> str:
        return self._nome_cliente

    @property
    def numero_assentos(self) -> int:
        return self._numero_assentos

    @exibicao.setter
    def exibicao(self, nova_exibicao: Screening) -> None:
        self._exibicao = nova_exibicao

    @nome_cliente.setter
    def nome_cliente(self, novo_nome_cliente: str) -> None:
        self._nome_cliente = novo_nome_cliente

    @numero_assentos.setter
    def numero_assentos(self, novo_numero_assentos: int) -> None:
        self._numero_assentos = novo_numero_assentos

    def confirmar(self) -> str:
        infos = f"Reserva confirmada para {self._nome_cliente} em {self._exibicao.data} às {self._exibicao.hora} para o filme '{self._exibicao.filme.titulo}' com {self._numero_assentos} assentos."
        print(infos)
        return infos

    def cancelar(self) -> str:
        infos = f"Reserva para {self._nome_cliente} para o filme '{self._exibicao.filme.titulo}' foi cancelada."
        print(infos)
        return infos


# Classe para gerenciar o cinema
class Cinema:
    def __init__(self) -> None:
        self._filmes = []
        self._salas = []
        self._exibicoes = []
        self._reservas = []

    def adicionar_filme(self, filme: Movie) -> None:
        if filme not in self._filmes:
            self._filmes.append(filme)

    def adicionar_sala(self, sala: CinemaHall) -> None:
        if sala not in self._salas:
            self._salas.append(sala)

    def agendar_exibicao(self, exibicao: Screening) -> None:
        if exibicao not in self._exibicoes:
            self._exibicoes.append(exibicao)

    def fazer_reserva(self, reserva: Reservation) -> None:
        if reserva not in self._reservas:
            self._reservas.append(reserva)

    def cancelar_reserva(self, reserva: Reservation) -> None:
        if reserva in self._reservas:
            self._reservas.remove(reserva)


# Exemplo de uso
# Criação de objetos
filme = Movie("Inception", "Christopher Nolan", 148, "PG-13")
sala = CinemaHall(1, 100)
exibicao = Screening(filme, sala, "2024-07-01", "19:00")
reserva = Reservation(exibicao, "João", 4)

# Exibição de informações
filme.exibir_informacoes()

# Operações em sala
print(sala.reservar())  # True
print(sala.disponivel())  # False
sala.liberar()
print(sala.disponivel())  # True

# Agendar exibição
print(exibicao.agendar())

# Fazer reserva
print(reserva.confirmar())

# Operações no cinema
cinema = Cinema()
cinema.adicionar_filme(filme)
cinema.adicionar_sala(sala)
cinema.agendar_exibicao(exibicao)
cinema.fazer_reserva(reserva)
