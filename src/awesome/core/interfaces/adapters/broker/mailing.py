from abc import ABC, abstractmethod


class BaseMailing(ABC):

    @abstractmethod
    async def send_message(self, chat_id: int, text: str) -> None:
        raise NotImplementedError

    @abstractmethod
    async def messages(self):
        raise NotImplementedError
