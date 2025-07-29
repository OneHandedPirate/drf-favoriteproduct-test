import uuid
from dataclasses import dataclass

from users.models import CustomUser


@dataclass(frozen=True)
class BaseProductIdUserDTO:
    user: CustomUser
    product_id: uuid.UUID | None


class AddFavoriteProductDTO(BaseProductIdUserDTO): ...


class DeleteFavoriteProductDTO(BaseProductIdUserDTO): ...
