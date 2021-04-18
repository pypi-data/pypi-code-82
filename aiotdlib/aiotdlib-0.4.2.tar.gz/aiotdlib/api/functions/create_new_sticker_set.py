# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import InputSticker


class CreateNewStickerSet(BaseObject):
    """
    Creates a new sticker set; for bots only. Returns the newly created sticker set
    
    Params:
        user_id (:class:`int`)
            Sticker set owner
        
        title (:class:`str`)
            Sticker set title; 1-64 characters
        
        name (:class:`str`)
            Sticker set name. Can contain only English letters, digits and underscores. Must end with *"_by_<bot username>"* (*<bot_username>* is case insensitive); 1-64 characters
        
        is_masks (:class:`bool`)
            True, if stickers are masks. Animated stickers can't be masks
        
        stickers (:obj:`list[InputSticker]`)
            List of stickers to be added to the set; must be non-empty. All stickers must be of the same type
        
    """

    ID: str = Field("createNewStickerSet", alias="@type")
    user_id: int
    title: str = Field(..., min_length=1, max_length=64)
    name: str = Field(..., min_length=1, max_length=64)
    is_masks: bool
    stickers: list[InputSticker]

    @staticmethod
    def read(q: dict) -> CreateNewStickerSet:
        return CreateNewStickerSet.construct(**q)
