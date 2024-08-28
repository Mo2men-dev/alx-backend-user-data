#!/usr/bin/env python3
"""
Tasks: Logging and Obfuscation
"""
import re
import logging
from typing import List
from os import environ
import mysql.connector

PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def main():
    """
    conncet to db and ger req rows
    """
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users;")
    field_names = [i[0] for i in cursor.description]

    logger = get_logger()

    for row in cursor:
        str_row = ''.join(f'{f}={str(r)}; ' for r, f in zip(row, field_names))
        logger.info(str_row.strip())

    cursor.close()
    db.close()


class RedactingFormatter(logging.Formatter):
    """
    Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """
        inits the class
        """
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """
        Log formatter
        """
        record.msg = filter_datum(self.fields,
                                  self.REDACTION,
                                  record.getMessage(),
                                  self.SEPARATOR)

        return super(RedactingFormatter, self).format(record)


def get_logger() -> logging.Logger:
    """ Returns a Logger Object """
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False

    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    logger.addHandler(stream_handler)

    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """ Returns a connector to a MySQL database """
    username = environ.get("PERSONAL_DATA_DB_USERNAME", "root")
    password = environ.get("PERSONAL_DATA_DB_PASSWORD", "")
    host = environ.get("PERSONAL_DATA_DB_HOST", "localhost")
    db_name = environ.get("PERSONAL_DATA_DB_NAME")

    c = mysql.connector.connection.MySQLConnection(user=username,
                                                   password=password,
                                                   host=host,
                                                   database=db_name)

    return c


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """
    function that returns the log message obfuscated
    """
    for field in fields:
        message = re.sub(f"{field}.*?{separator}",
                         f"{field}={redaction}{separator}",
                         message)
    return message


if __name__ == '__main__':
    main()
