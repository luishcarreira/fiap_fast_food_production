from enum import Enum
from typing import TypeVar, Type

from sqlalchemy import inspect

ModelType = TypeVar("ModelType")
EntityType = TypeVar("EntityType")


class GenericMapper:
    @staticmethod
    def to_entity(model: ModelType, entity_class: Type[EntityType]) -> EntityType:
        """Converts a SQLAlchemy model instance to a Pydantic entity."""
        # Use inspect to get the fields of the model
        model_dict = {
            column.name: getattr(model, column.name)
            for column in inspect(model).mapper.column_attrs
            if hasattr(entity_class, column.name)
        }

        # Remove the _sa_instance_state attribute if present
        model_dict.pop('_sa_instance_state', None)

        # Handle Enums conversion if needed
        for key, value in model_dict.items():
            if isinstance(value, Enum):  # For Enum fields
                model_dict[key] = value.value

        # Create the entity instance with the mapped dictionary
        return entity_class(**model_dict)

    @staticmethod
    def to_model(entity: EntityType, model_class: Type[ModelType]) -> ModelType:
        """Converts a Pydantic entity to a SQLAlchemy model instance."""
        entity_dict = entity.dict()  # Use Pydantic's dict method to convert to dictionary
        model_dict = {
            k: v
            for k, v in entity_dict.items()
            if hasattr(model_class, k) and k != '_sa_instance_state'
        }

        # Ensure we convert enums properly (if needed)
        for key, value in model_dict.items():
            if isinstance(value, Enum):  # For Enum fields
                model_dict[key] = value.value

        # Create the model instance with the mapped dictionary
        return model_class(**model_dict)
