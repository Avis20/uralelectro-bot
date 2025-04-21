from typing import Any, ClassVar, Protocol, Dict, Type, Callable
from dataclasses import dataclass, asdict

import dacite


class DataClass(Protocol):
    __dataclass_fields__: ClassVar[Dict]


@dataclass
class DTO:
    def as_dict(self, exclude_none: bool = False) -> dict:
        if exclude_none:
            return asdict(self, dict_factory=lambda field: {key: value for (key, value) in field if value is not None})
        return asdict(self)

    @classmethod
    def from_dict(cls, data: dict, type_hooks: Dict[Type, Callable[[Any], Any]] | None = None, **kwargs) -> Any:
        data.update(kwargs)
        config = None
        if type_hooks:
            config = dacite.Config(type_hooks=type_hooks)
        return dacite.from_dict(data_class=cls, data=data, config=config)

    @classmethod
    def model_to_dto(cls, from_model_dt_class: DataClass, **kwargs):
        from_dt_dict = asdict(from_model_dt_class)
        return cls.from_dict(from_dt_dict, **kwargs)


@dataclass
class PaginationBaseDTO(DTO):
    page: int = 1
    limit: int | None = None
    all: int | None = None
    offset: int | None = 0

    def __post_init__(self):
        self.offset = self.limit * (self.page - 1) if self.limit else self.page
