"""
backend/app/core/config.py

- Central app settings using Pydantic BaseSettings
- Load env vars
- Define Homebrain system prompt
- Initialize shared LLMs
"""

from datetime import timedelta

from pydantic_settings import BaseSettings, SettingsConfigDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI


class Settings(BaseSettings):
    # Tell Pydantic where to read env vars from
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # --- Database ---
    postgres_user: str
    postgres_password: str
    postgres_db: str
    database_url: str

    # --- LLM API keys ---
    gemini_api_key: str
    openai_api_key: str

    # --- Auth / JWT ---
    auth_secret_key: str
    auth_algorithm: str = "HS256"
    auth_access_token_expires_minutes: int = 60

    @property
    def access_token_timedelta(self) -> timedelta:
        return timedelta(minutes=self.auth_access_token_expires_minutes)


# Expose singleton settings object
settings = Settings()

# System Prompt used by LangGraph node
SYSTEM_PROMPT = (
    "You are Homebrain, a fun and nerdy AI assistant, created by Pukar Subedi, "
    "for Pukar Subedi's homelab. "
    "You help with VMs (Proxmox, vSphere, etc.), Kubernetes, Terraform, "
    "Ansible, Cloud, Networking, and related tooling/concepts. "
    "You also help explain Pukar's homelab to others that are interested. "
    "Try not to make your responses too long; keep them concise and to the point "
    "but still fun and engaging. "
)

# 3. Expose LLM objects for other services to use
gemini_llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
    max_retries=2,
    google_api_key=settings.gemini_api_key,
)

openai_llm = ChatOpenAI(
    model_name="gpt-5-nano",
    api_key=settings.openai_api_key,
)
