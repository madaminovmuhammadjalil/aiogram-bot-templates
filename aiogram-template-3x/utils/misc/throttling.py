def rate_limit(limit: int, key: str = None):
    """
    Aiogram 3.x uchun rate limit dekoratori.
    Handlerga cheklov (throttling) qo‘yish uchun ishlatiladi.

    :param limit: maksimal so‘rovlar soni / vaqt birligi
    :param key: maxsus kalit nomi (agar kerak bo‘lsa)
    """

    def decorator(func):
        setattr(func, "throttling_rate_limit", limit)
        if key:
            setattr(func, "throttling_key", key)
        return func

    return decorator
