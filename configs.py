"""Uses python-dotenv and refers to settings.env
   https://rednafi.github.io/digressions/python/2020/06/03/python-configs.html
   sensitive information should be injected as a shell environment variable.
   For example, although I’ve defined an attribute called REDIS_PASS in the GlobalConfig class,
   there is no mention of any REDIS_PASS variable in the .env file.
   MAY NOT WORK in windows ?? """
# import logging  ## wastrying to log here but would not work
from typing import Optional

from pydantic import BaseSettings, Field, BaseModel


# logger = logging.getLogger(__name__)

class AppConfig(BaseModel):
    """Application configurations."""

    VAR_A: int = 33
    VAR_B: float = 22.0
    # logger.debug('Base Model set in AppConfig')


class GlobalConfig(BaseSettings):
    """Global configurations."""

    # These variables will be loaded from the .env file. However, if
    # there is a shell environment variable having the same name,
    # that will take precedence.

    APP_CONFIG: AppConfig = AppConfig()

    # define global variables with the Field class
    ENV_STATE: Optional[str] = Field(None, env="ENV_STATE")

    # environment specific variables do not need the Field class
    OWS_API_KEY: Optional[str] = None
    REDIS_HOST: Optional[str] = None
    REDIS_PORT: Optional[int] = None
    REDIS_PASS: Optional[str] = None

    class Config:
        """Loads the dotenv file."""

        env_file: str = ".env"


class DevConfig(GlobalConfig):
    """Development configurations."""
    # logger.info('In DevConfig now')
    class Config:
        env_prefix: str = "DEV_"


class ProdConfig(GlobalConfig):
    """Production configurations."""
    # logger.debug('In ProdConfig now')
    class Config:
        env_prefix: str = "PROD_"


class FactoryConfig:
    """Returns a config instance depending on the ENV_STATE variable."""

    def __init__(self, env_state: Optional[str]):
        self.env_state = env_state
        # logger.info(f'just did init in FactoryConfig, env_state = {self.env_state}')

    def __call__(self):
        if self.env_state == "dev":
            return DevConfig()

        elif self.env_state == "prod":
            return ProdConfig()


cnf = FactoryConfig(GlobalConfig().ENV_STATE)()

print(cnf.__repr__())  # comment out in production
