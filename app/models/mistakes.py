from pydantic import BaseModel


class Mistake(BaseModel):
    rule: str
    learner_version: str
    correction: str


class CorrectionResult(BaseModel):
    mistakes: list[Mistake]