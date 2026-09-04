from dataclasses import dataclass


@dataclass
class CreateBudgetModel:
    amount: float


@dataclass
class ReadBudgetModel:
    month: int
    year: int


@dataclass
class UpdateBudgetModel:
    month: int
    year: int
    amount: float


@dataclass
class DeleteBudgetModel:
    month: int
    year: int
