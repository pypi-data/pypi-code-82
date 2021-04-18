from __future__ import annotations
from ._imports import *

from .button import Button

if t.TYPE_CHECKING:
    from ..projectiles.reaction import Reaction
    from .message import Message


class ButtonReaction(Button, metaclass=abc.ABCMeta):
    """
    An abstract class representing a clickable reaction to a message.
    """

    @ap.async_property
    async def reactions(self) -> t.List["Reaction"]:
        """
        :return: The list of reactions generated by this button. It may vary every time this property is accessed,
                 based on the users who have reacted to the button at the time of access.
        """
        raise exc.NotSupportedError()

    @ap.async_property
    async def count(self) -> int:
        """
        :return: The count of reactions that this button generated. It may vary every time this property is accessed,
                 based on how many users have reacted to the button at the time of access.
        """
        raise exc.NotSupportedError()

    @ap.async_property
    async def message(self) -> t.Optional["Message"]:
        """
        :return: The message this button is attached to. Can be :data:`None`, if the button hasn't been attached to a
                 message yet.
        """
        raise exc.NotSupportedError()


__all__ = (
    "ButtonReaction",
)
