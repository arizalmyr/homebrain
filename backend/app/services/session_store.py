from typing import Dict
from uuid import uuid4
from app.models.schemas import ChatMessage

SESSION_STORE: Dict[str, list[ChatMessage]] = {}


def get_or_create_session(session_id: str | None) -> str:
    """
    Return an existing session_id or create a new one if none given.
    """
    if session_id and session_id in SESSION_STORE:
        return session_id

    new_id = str(uuid4())
    SESSION_STORE[new_id] = []
    return new_id


def get_history_for_session(session_id: str) -> list[ChatMessage]:
    return SESSION_STORE.get(session_id, [])


def save_history_for_session(session_id: str, history: list[ChatMessage]) -> None:
    SESSION_STORE[session_id] = history
