from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from .context import channel_instance

if TYPE_CHECKING:
    from .channel import Channel

class BaseSchema:
    id: Optional[str] = None
    channel: "Channel" = field(default_factory=lambda: channel_instance.get(), init=False)