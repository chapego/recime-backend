import uuid
from sqlalchemy import Column, ForeignKey, Float, String

# from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID


from app.db.base_class import Base


class RecipeIngredients(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    name = Column(String)
    weight = Column(Float)
    volume = Column(Float)
    count = Column(Float)
    calories = Column(Float)
    fat = Column(Float)
    carbohydrates = Column(Float)
    protein = Column(Float)
