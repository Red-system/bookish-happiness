from app import settings
from app import models
from app import core


if __name__ == "__main__":
    settings.migrate()
    core.start_app()

print("Hello World!")
