import logging
from aiogram import Router, types
from aiogram.exceptions import (
    TelegramBadRequest,
    TelegramConflictError,
    TelegramForbiddenError,
    TelegramNetworkError,
    TelegramUnauthorizedError,
    TelegramAPIError,
    TelegramServerError,
)

router = Router(name="error_handler")


@router.errors()
async def errors_handler(update: types.Update, exception: Exception):
    """
    Aiogram 3.x uchun universal xatolik ushlovchi
    """

    if isinstance(exception, TelegramUnauthorizedError):
        logging.error(f"Unauthorized: {exception}")
        return True

    elif isinstance(exception, TelegramForbiddenError):
        logging.error(f"Forbidden: {exception}")
        return True

    elif isinstance(exception, TelegramBadRequest):
        logging.error(f"Bad Request: {exception}")
        return True

    elif isinstance(exception, TelegramConflictError):
        logging.error(f"Conflict Error: {exception}")
        return True

    elif isinstance(exception, TelegramNetworkError):
        logging.error(f"Network Error: {exception}")
        return True

    elif isinstance(exception, TelegramServerError):
        logging.error(f"Server Error: {exception}")
        return True

    elif isinstance(exception, TelegramAPIError):
        logging.error(f"API Error: {exception}")
        return True

    logging.error(f"Unexpected error:\nUpdate: {update}\nException: {exception}")
    return True
