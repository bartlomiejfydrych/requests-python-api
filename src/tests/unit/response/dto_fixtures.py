"""
NOTE FOR ME:
Ten plik celowo NIE ma nazwy „test_*.py”, a poniższe klasy celowo NIE mają nazwy „Test*” – w przeciwnym razie pytest
próbowałby zebrać ten moduł/te klasy jako moduł testowy/klasy testowe (domyślne wzorce
python_files/python_classes), co generowałoby ostrzeżenie PytestCollectionWarning (modele pydantic
mają __init__, o którym pytest ostrzega w przypadku wszystkiego, co pasuje do „Test*”).
"""

from typing import Optional

from pydantic import Field

from dto.base_dto import BaseDto


class SampleDto(BaseDto):
    name: str


class SampleNestedDto(BaseDto):
    value: str


class SampleParentDto(BaseDto):
    nested: SampleNestedDto


class SampleValidatedDto(BaseDto):
    name: str = Field(min_length=3)
    number: Optional[str] = Field(default=None, pattern=r"^\d+$")
