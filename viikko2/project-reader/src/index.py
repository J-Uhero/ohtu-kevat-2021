from project_reader import ProjectReader
import ssl


def main():
    url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy-avoin/python-kevat-2021/main/koodi/viikko3/web-login-robot/pyproject.toml"
    ssl._create_default_https_context = ssl._create_unverified_context
    reader = ProjectReader(url)
    print(reader.get_project())


if __name__ == "__main__":
    main()
