from django.conf import settings
from django.core.management.base import BaseCommand
import json
from school.models import Student, Teacher
import os


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('file_json', type=str)

    def handle(self, *args, **kwargs):
        file_json = kwargs['file_json']
        file_json_path = os.path.join(settings.BASE_DIR, file_json)
        if not os.path.exists(file_json_path):
            print('Не найден файл по указанному адресу:', file_json_path)
            return

        with open(file_json_path, encoding='utf8') as src_file:
            data = json.load(src_file)

        for object in data:
            if object['model'] == 'school.student':
                student = Student.objects.create(id=object['pk'],
                                                 name=object['fields'].get("name"),
                                                 group=object['fields'].get("group"))
                teacher_id = object['fields'].get('teacher', None)
            if teacher_id:
                student.teacher.add(Teacher.objects.get(id=teacher_id))
            elif object['model'] == 'school.teacher':
                teacher = Teacher.objects.create(id=object['pk'], **object['fields'])
