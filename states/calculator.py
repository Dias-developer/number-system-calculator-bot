from aiogram.fsm.state import StatesGroup, State

class Calculator(StatesGroup):
    waiting_for_to_decimal_conversion = State()
