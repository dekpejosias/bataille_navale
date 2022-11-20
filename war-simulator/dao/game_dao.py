from ..model.game import Game
from ..model.player import Player
from ..model.vessel import Vessel
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, select
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:////tmp/tdlog.db', echo=True, future=True)
Base = declarative_base(bind=engine)
Session = sessionmaker(bind=engine)

class GameEntity(Base):
    __tablename__ = 'game'
    id = Column(Integer, primary_key=True)
    players = relationship("PlayerEntity", back_populates="game",
    cascade="all, delete-orphan")


class PlayerEntity(Base):
    __tablename__ = 'player'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    game_id = Column(Integer, ForeignKey("game.id"), nullable=False)
    game = relationship("GameEntity", back_populates="players")
    battle_field = relationship("BattlefieldEntity", back_populates="player",
    uselist=False, cascade="all, delete-orphan")

class BattlefieldEntity(Base):
    __tablename__ = 'battlefield'
    id = Column(Integer, primary_key=True)
    min_x = Column(Integer, nullable=False)
    min_x = Column(Integer, nullable=False)
    min_y = Column(Integer, nullable=False)
    min_z = Column(Integer, nullable=False)
    max_x = Column(Integer, nullable=False)
    max_y = Column(Integer, nullable=False)
    max_z = Column(Integer, nullable=False)
    player = relationship("playerEntity", back_populates="player")
    vessel = relationship("vesselEntity",
                                back_populates="vessels", cascade="all, delete-orphan")



class VesselEntity(Base):
    __tablename__ = 'vessel'
    id = Column(Integer, primary_key=True)
    coord_x = Column(Integer, nullable=True)
    coord_y = Column(Integer, nullable=True)
    coord_z = Column(Integer, nullable=True)
    hits_to_be_destroyed = Column(Integer, nullable=True)
    type = Column(String, nullable=False)
    battlefield = relationship("battlefieldEntity", back_populates="battlefield")
    weaponfield = relationship("battlefieldEntity", back_populates="weaponfield",
                               uselist=False, cascade="all, delete-orphan")


class WeaponEntity(Base):
    __tablename__ = 'weapon'
    id = Column(Integer, primary_key=True)
    ammunitions = Column(Integer, nullable=True)
    range = Column(Integer, nullable=True)
    type = Column(Integer, nullable=True)
    vessel = relationship("vesselEntity", back_populates="vessel")


class GameDao:
    def __init__(self):
        Base.metadata.create_all()
        self.db_session = Session()
    def create_game(self, game: Game) -> int:
        game_entity = map_to_game_entity(game)
        self.db_session.add(game_entity)
        self.db_session.commit()
        return game_entity.id

    def find_game(self, game_id: int) -> Game:
        stmt = select(GameEntity).where(GameEntity.id == game_id)
        game_entity = self.db_session.scalars(stmt).one()
        return map_to_game(game_entity)

    def map_to_game_entity(self,game_entity)-> Game:


    def map_to_player(self,player_entity)-> Player:


    def map_to_vessel(self,vessel_entity)-> Vessel:


