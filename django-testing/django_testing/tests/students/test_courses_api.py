import random
import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT, HTTP_400_BAD_REQUEST


# проверка получения 1го курса (retrieve-логика)
# создаем курс через фабрику
# строим урл и делаем запрос через тестовый клиент
# проверяем, что вернулся именно тот курс, который запрашивали
@pytest.mark.django_db
def test_course(api_client, course_factory, student_factory):
    course = course_factory(students=student_factory())[0]
    url = reverse("courses-detail", args=[course.id])

    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert resp_json["id"] == course.id


# проверка получения списка курсов (list-логика)
# аналогично – сначала вызываем фабрики, затем делаем запрос и проверяем результат
@pytest.mark.django_db
def test_course_list(api_client, course_factory, student_factory):
    course_list = course_factory(students=student_factory())
    url = reverse("courses-list")

    resp = api_client.get(url)
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert len(resp_json) == 3


# проверка фильтрации списка курсов по id
# создаем курсы через фабрику, передать id одного курса в фильтр, проверить результат запроса с фильтром
@pytest.mark.django_db
def test_course_filter_id(api_client, course_factory, student_factory):
    course_list = course_factory(students=student_factory())
    random_course_id = random.choice(course_list).id
    url = reverse("courses-list")

    resp = api_client.get(url, {"id": random_course_id})
    resp_json = resp.json()[0]

    assert resp.status_code == HTTP_200_OK
    assert resp_json["id"] == random_course_id


# проверка фильтрации списка курсов по name
@pytest.mark.django_db
def test_course_filter_name(api_client, course_factory, student_factory):
    course_list = course_factory(students=student_factory())
    random_course_name = random.choice(course_list).name
    url = reverse("courses-list")

    resp = api_client.get(url, {"name": random_course_name})
    resp_json = resp.json()[0]

    assert resp.status_code == HTTP_200_OK
    assert resp_json["name"] == random_course_name


# тест успешного создания курса
@pytest.mark.django_db
def test_course_create(api_client):
    url = reverse("courses-list")
    payload = {'name': 'added_course'}

    resp = api_client.post(url, payload, format="json")
    resp_json = resp.json()
    resp_get = api_client.get(url, {"name": 'added_course'}).json()[0]

    assert resp.status_code == HTTP_201_CREATED
    assert resp_json['name'] == payload['name']
    assert resp_get["name"] == payload['name']


# тест успешного обновления курса
@pytest.mark.django_db
def test_course_update(api_client, course_factory, student_factory):
    courses_list = course_factory(students=student_factory())
    random_curse = random.choice(courses_list)
    url = reverse('courses-detail', args=[random_curse.id])
    payload = {
        'name': f'{random_curse.name} update'
    }

    resp = api_client.patch(url, payload, format='json')
    resp_json = resp.json()

    assert resp.status_code == HTTP_200_OK
    assert resp_json['id'] == random_curse.id and resp_json['name'] == payload['name']


# тест успешного удаления курса
@pytest.mark.django_db
def test_course_delete(api_client, course_factory, student_factory):
    courses_list = course_factory(students=student_factory())
    random_curse_id = random.choice(courses_list).id
    url = reverse('courses-detail', args=[random_curse_id])

    resp = api_client.delete(url)
    existing_ids = [course['id'] for course in api_client.get(reverse('courses-list')).json()]

    assert resp.status_code == HTTP_204_NO_CONTENT
    assert random_curse_id not in existing_ids

