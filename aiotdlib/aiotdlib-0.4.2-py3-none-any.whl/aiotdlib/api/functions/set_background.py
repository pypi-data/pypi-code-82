# =============================================================================== #
#                                                                                 #
#    This file has been generated automatically!! Do not change this manually!    #
#                                                                                 #
# =============================================================================== #
from __future__ import annotations

from pydantic import Field

from ..base_object import BaseObject
from ..types import BackgroundType, InputBackground


class SetBackground(BaseObject):
    """
    Changes the background selected by the user; adds background to the list of installed backgrounds
    
    Params:
        background (:class:`InputBackground`)
            The input background to use, null for filled backgrounds
        
        type_ (:class:`BackgroundType`)
            Background type; null for default background. The method will return error 404 if type is null
        
        for_dark_theme (:class:`bool`)
            True, if the background is chosen for dark theme
        
    """

    ID: str = Field("setBackground", alias="@type")
    background: InputBackground
    type_: BackgroundType = Field(..., alias='type')
    for_dark_theme: bool

    @staticmethod
    def read(q: dict) -> SetBackground:
        return SetBackground.construct(**q)
