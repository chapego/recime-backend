import uuid
from datetime import datetime
from sqlalchemy import Column, String, ForeignKey, Float

# from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql.sqltypes import DateTime


from app.db.base_class import Base


class RecipeIngredients(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    recipe_id = Column(UUID, ForeignKey("recipe.id"))
    ingredient_id = Column(UUID, ForeignKey("ingredient.id"))
    amount = Column(Float)
