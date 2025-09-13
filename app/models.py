from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy import BIGINT, VARCHAR
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_security.models import fsqla_v3 as fsqla

class Base(DeclarativeBase):
    pass

db=SQLAlchemy(model_class=Base)
fsqla.FsModels.set_db_info(db)

class User(Base, fsqla.FsUserMixin):
    __tablename__ = 'user'

    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.username!r}, email={self.email!r})"
    
class Role(Base, fsqla.FsRoleMixin):
    __tablename__ = 'role'