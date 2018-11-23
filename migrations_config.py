import os

DB_URI = os.getenv('DB_URI', 'postgres://postgres:password@localhost:5432')
VERSIONS_PATH = os.getenv('VERSIONS_PATH', os.path.join(os.path.dirname(os.path.realpath(__file__)), 'versions'))
SEPARATOR = '-'
