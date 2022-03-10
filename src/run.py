#!/usr/bin/env python
#

from phonebook import app


def create_db_all():
    from phonebook import db

    db.create_all()


def main():
    app.run(host='0.0.0.0', port=8000, debug=True)


if __name__ == '__main__':
    main()
