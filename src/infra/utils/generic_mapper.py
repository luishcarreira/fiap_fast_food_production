from typing import TypeVar, Type

ModelType = TypeVar("ModelType")
EntityType = TypeVar("EntityType")


class GenericMapper:
    @staticmethod
    def to_entity(model: ModelType, entity_class: Type[EntityType]) -> EntityType:
        model_dict = {
            k: v for k, v in model.__dict__.items()
            if hasattr(entity_class, k) and k != '_sa_instance_state'
        }
        return entity_class(**model_dict)

    @staticmethod
    def to_model(entity: EntityType, model_class: Type[ModelType]) -> ModelType:
        entity_dict = {
            k: v for k, v in entity.__dict__.items()
            if hasattr(model_class, k) and k != '_sa_instance_state'
        }
        return model_class(**entity_dict)
