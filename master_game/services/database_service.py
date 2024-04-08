from sqlalchemy import create_engine
from sqlalchemy.orm import Session, declarative_base, sessionmaker
from master_game.config import DATABASE_URL


class DatabaseService:
    base = None
    _cash_service = None
    _session = None
    _engine = None
    _commit = None

    def __new__(cls, database_url: str = "", commit=True):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DatabaseService, cls).__new__(cls)
            cls.base = declarative_base()
            cls._engine = create_engine(database_url, echo=True)
            Session = sessionmaker(bind=cls._engine)
            cls._session = Session()
            cls.base.metadata.create_all(cls._engine)
            cls._commit = commit
        return cls.instance

    @staticmethod
    def init_base() -> None:
        sesion = DatabaseService().get_session()
        DatabaseService.base.metadata.create_all(DatabaseService._engine)
        sesion.commit()

    @staticmethod
    def get_session() -> Session:
        return DatabaseService._session


DatabaseService(DATABASE_URL)
