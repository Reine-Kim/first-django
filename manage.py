#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
"""장고를 관리하기 위해서 내장하고 있는 스크립트."""
"""장고의 각종 프레임워크에서 제공하는 각종 명령어 실행하게 하고, 웹앱/프로젝트 시작할 때 도와줌"""
"""DB 셋업할떄도 사용해서 장고에서 호환되는 규칙 유지하도록 함"""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'firstdjango.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
