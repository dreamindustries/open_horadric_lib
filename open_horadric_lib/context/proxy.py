from __future__ import annotations

import dataclasses
from typing import Type

from google.protobuf.message import Message
from open_horadric_lib.context.base import BaseContext


@dataclasses.dataclass(init=False)
class ProxyContext(BaseContext):
    request_message_type: Type[Message]
    response_message_type: Type[Message]
    request_id: str
