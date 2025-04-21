from pydantic_settings import BaseSettings, SettingsConfigDict


class BotConfig(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="bot_")
    token: str = ""


class CacheSettings(BaseSettings):
    REDIS_HOST: str = "redis"
    REDIS_PORT: int = 6379
    REDIS_PASS: str | None = None

    @property
    def redis_url(self) -> str:
        if self.REDIS_PASS:
            return f"redis://{self.REDIS_PASS}@{self.REDIS_HOST}:{self.REDIS_PORT}/0"
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"


class WebhookSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="webhook_")
    USE_WEBHOOK: bool = False
    WEBHOOK_BASE_URL: str = "https://xxx.ngrok-free.app"
    WEBHOOK_PATH: str = "/webhook"
    WEBHOOK_SECRET: str = ""
    WEBHOOK_HOST: str = "localhost"
    WEBHOOK_PORT: int = 8080

    @property
    def webhook_url(self) -> str:
        return f"{self.WEBHOOK_BASE_URL}{self.WEBHOOK_PATH}"


class SupportSettings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="support_")
    SUPPORT_URL: str = "https://t.me/support"


class Settings(BaseSettings):
    DEBUG: bool = False
    LOG_LEVEL: str = "INFO"
    USE_WEBHOOK: bool = False

    webhook: WebhookSettings = WebhookSettings()
    bot: BotConfig = BotConfig()
    cache: CacheSettings = CacheSettings()
    support: SupportSettings = SupportSettings()


settings = Settings()
