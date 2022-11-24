# yanked from https://github.com/PrefectHQ/prefect-collection-template/blob/main/tests/test_bake_project.py
import os
import shlex
import subprocess
import sys
from contextlib import contextmanager

from cookiecutter.exceptions import FailedHookException
from cookiecutter.utils import rmtree
from pytest import fixture


@fixture
def python_version():
    v = sys.version_info
    return f"{v.major}.{v.minor}"


@contextmanager
def inside_dir(dirpath):
    """
    Execute code from inside the given directory
    :param dirpath: String, path of the directory the command is being run.
    """
    old_path = os.getcwd()
    try:
        os.chdir(dirpath)
        yield
    finally:
        os.chdir(old_path)


@contextmanager
def bake_in_temp_dir(cookies, *args, **kwargs):
    result = cookies.bake(*args, **kwargs)
    try:
        yield result
    finally:
        if result.project_path is not None:
            rmtree(str(result.project_path))


def run_inside_dir(command, dirpath):
    with inside_dir(dirpath):
        return subprocess.check_call(shlex.split(command))


def test_bake_with_defaults(cookies, python_version):
    context = {"python_version": python_version}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        assert result.project_path.name == "app-odp-template"

        found_toplevel_files = [f.name for f in result.project_path.iterdir()]
        assert "pyproject.toml" in found_toplevel_files
        assert "deployment_config.yml" in found_toplevel_files
        assert "odp" in found_toplevel_files
        assert "README.md" in found_toplevel_files
        assert "MAINTAINERS.md" in found_toplevel_files
        assert "tests" in found_toplevel_files
        assert ".github" in found_toplevel_files
        assert ".gitignore" in found_toplevel_files


def test_bake_with_custom_name(cookies, python_version):
    context = {"project_name": "app-awesome", "python_version": python_version}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert result.project_path.is_dir()
        assert result.exit_code == 0
        assert result.exception is None

        assert result.project_path.name == "app-awesome"
        assert (result.project_path / "app_awesome").exists


def test_bake_and_run_precommit_hooks(cookies, python_version):
    context = {"python_version": python_version}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("git init", str(result.project_path)) == 0
        assert run_inside_dir("git add .", str(result.project_path)) == 0
        assert run_inside_dir("pre-commit run -a", str(result.project_path)) == 0
        print("test_bake_and_run_precommit_hooks path", str(result.project_path))


def test_bake_and_run_tests(cookies, python_version):
    context = {"python_version": python_version}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert result.project_path.is_dir()
        assert run_inside_dir("poetry install", str(result.project_path)) == 0
        assert run_inside_dir("poetry run pytest tests", str(result.project_path)) == 0
        print("test_bake_and_run_tests path", str(result.project_path))


def test_bake_with_prefix_name_fail(cookies, python_version):
    context = {"project_name": "mydata_awesome", "python_version": python_version}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert isinstance(result.exception, FailedHookException)


def test_bake_with_hyphen_slug_fail(cookies, python_version):
    context = {"project_slug": "dataproject-awesome", "python_version": python_version}
    with bake_in_temp_dir(cookies, extra_context=context) as result:
        assert isinstance(result.exception, FailedHookException)
