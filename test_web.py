from glob import glob
from os import path
from subprocess import check_output


def test_index():
    assert path.isfile("index.html"), "Il faut le fichier 'index.html'."


def test_html():
    for file in glob("**/*.html", recursive=True):
        output = check_output(
            [
                "curl",
                "-s",
                "-H",
                "Content-Type: text/html",
                "--data-binary",
                f"@{file}",
                "https://validator.w3.org/nu/?out=gnu&level=error",
            ],
        ).decode()
        assert "" == output, f"{file} {output}"


def test_css():
    count: int = 0
    for file in glob("**/*.css", recursive=True):
        count += 1
        output = check_output(
            [
                "curl",
                "-s",
                "-H",
                "Content-Type: text/css",
                "--data-binary",
                f"@{file}",
                "https://validator.w3.org/nu/?out=gnu",
            ],
        ).decode()
        assert "" == output, f"{file} {output}"


def test_filename():
    for file in glob("**/*", recursive=True):
        assert match(
            "^[a-z0-9\\\.\-_/]+$", file
        ), f"{file} ne doit contenir que des lettres minuscules, chiffres, tirets ou underscores. "
