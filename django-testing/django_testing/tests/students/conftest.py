import pytest
from model_bakery import baker


# Создаем фабрику курсов
@pytest.fixture
def course_factory():
    def factory(**kwargs):
        return baker.make('Course', _quantity=3, **kwargs)

    return factory


# Создаем фабрику студентов
@pytest.fixture
def student_factory():
    def factory(**kwargs):
        return baker.make('Student', _quantity=3, **kwargs)

    return factory
