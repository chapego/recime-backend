# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base  # noqa
from app.models.recipe import Recipe  # noqa
from app.models.recipe_ingredients import RecipeIngredients  # noqa
from app.models.ingredients import Ingredients  # noqa
