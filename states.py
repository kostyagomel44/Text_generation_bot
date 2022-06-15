from aiogram.dispatcher.filters.state import State, StatesGroup


class UserData(StatesGroup):
    """Для хранения состояний.
    Наследуется от StatesGroup. Использует State."""
    style = State()
    text = State()
