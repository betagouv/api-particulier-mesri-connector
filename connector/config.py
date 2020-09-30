import os


class Config(object):
    DEBUG = False
    TESTING = False
    ERROR_404_HELP = False
    RESTPLUS_MASK_SWAGGER = False
    STUB_CONNECTOR = os.environ.get("STUB_CONNECTOR") == "False"
    AIRTABLE_API_KEY = os.environ.get("AIRTABLE_API_KEY")
    AIRTABLE_API_URL = os.environ.get("AIRTABLE_API_URL")


class DevConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    pass


class TestConfig(Config):
    Testing = True
