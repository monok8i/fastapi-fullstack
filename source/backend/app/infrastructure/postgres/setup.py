from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncEngine,
)

from source.backend.app.core import settings


def async_engine() -> AsyncEngine:
    engine = create_async_engine(
        url=settings.Database.SQLALCHEMY_DATABASE_URI, echo=True
    )
    return engine
