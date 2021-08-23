import uuid

from datetime import datetime

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime


from app.db.base_class import Base


class Recipe(Base):
    __tablename__ = "recipe"
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    recipe_name = Column(String)
    created_by = Column(String)
    date_created = Column(DateTime, default=datetime.now)
    description = Column(String)

    recipe_ingredients = relationship(
        "RecipeIngredients", back_populates="recipe_ingredients"
    )
