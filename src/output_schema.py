from typing import Any, Optional
from pydantic import BaseModel, Field


class AgentOutput(BaseModel):

    answerable: int = Field(
        description="1 if answerable, otherwise 0"
    )

    lookup_value: Optional[Any] = None

    rule_value: Optional[Any] = None

    final_answer: Optional[Any] = None