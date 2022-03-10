import os


class Config:
    @staticmethod
    def get_env(key, default: str = None, raise_if_not_found: bool = True):
        value = os.environ.get(key, default)

        if value is None:
            if raise_if_not_found:
                raise EnvironmentError(f"Environment variable `{key}` not defined.")

            return default

        return value

    PGHOST: str = None
    PGPORT: str = None
    PGUSER: str = None
    PGPASSWORD: str = None
    PGDATABASE: str = None

    @property
    def database_uri(self):
        return f'postgresql+psycopg2://{self.PGUSER}:{self.PGPASSWORD}@{self.PGHOST}:{self.PGPORT}/{self.PGDATABASE}'

    def __init__(self):
        self.PGHOST = Config.get_env('PGHOST')
        self.PGPORT = Config.get_env('PGPORT')
        self.PGUSER = Config.get_env('PGUSER')
        self.PGPASSWORD = Config.get_env('PGPASSWORD')
        self.PGDATABASE = Config.get_env('PGDATABASE')


config = Config()
