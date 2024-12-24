from __future__ import annotations
from abc import ABC, abstractmethod
from random import randrange
from typing import List


class Subject(ABC):
    """
    A interface assunto define uma série de métodos para gerenciar os assinantes
    """

    @abstractmethod
    def attach(self, observer: Observer) -> None:
        """
        Referenciar um observador ao assunto.
        """
        pass

    @abstractmethod
    def detach(self, observer: Observer) -> None:
        """
        Remover um observador do assunto.
        """
        pass

    @abstractmethod
    def notify(self) -> None:
        """
        Notificar todos os observadores sobre um evento.
        """
        pass


class ConcreteSubject(Subject):
    """
    O assunto possui algum importante estado que notificará os observadores quando alterado.
    """

    _state: int = None
    """
    Para simplificação, o estado importante do assunto estará armazenado nesta variável.

    """

    _observers: List[Observer] = []
    """
    Lista de assinantes
    """

    def attach(self, observer: Observer) -> None:
        print("Subject: Attached an observer.")
        self._observers.append(observer)

    def detach(self, observer: Observer) -> None:
        self._observers.remove(observer)

    """
    Os métodos de gerenciamento de assinaturas.
    """

    def notify(self) -> None:
        """
        Acionar uma atualização em cada assinante.
        """

        print("Subject: Notifying observers...")
        for observer in self._observers:
            observer.update(self)

    def some_business_logic(self) -> None:
        """
        Normalmente, a lógica de assinatura é apenas uma fração do que o assunto pode fazer.
        Os assuntos geralmente carregam alguma regra de negócio importante que sempre deve ser notificada.
        """

        print("\nSubject: I'm doing something important.")
        self._state = randrange(0, 10)

        print(f"Subject: My state has just changed to: {self._state}")
        self.notify()


class Observer(ABC):
    """
    A interface observe declara o método de atualização, usada pelos assuntos.
    """

    @abstractmethod
    def update(self, subject: Subject) -> None:
        """
        Receive update from subject.
        """
        pass


"""
Concrete Observers reagirá às atualizações causadas pelo assunto que estavam referenciando.
"""


class ConcreteObserverA(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state < 3:
            print("ConcreteObserverA: Reacted to the event")


class ConcreteObserverB(Observer):
    def update(self, subject: Subject) -> None:
        if subject._state == 0 or subject._state >= 2:
            print("ConcreteObserverB: Reacted to the event")


if __name__ == "__main__":
    # The client code.

    subject = ConcreteSubject()

    observer_a = ConcreteObserverA()
    subject.attach(observer_a)

    observer_b = ConcreteObserverB()
    subject.attach(observer_b)

    subject.some_business_logic()
    subject.some_business_logic()

    subject.detach(observer_a)

    subject.some_business_logic()