#!/usr/bin/env bash
#

set -e
set -o pipefail

# Sub-functions:
#
function wait_for_database()
{
    wait-for-it -h "${PGHOST}" -p "${PGPORT}"
}

# Main functions:
#
function run_phonebook()
{
    wait_for_database

    gosu phonebook ./run.py ${@}
}

# Execution:
#
case "${1}" in
    -- | phonebook)
        shift

        run_phonebook ${@}
        ;;
    -*)
        run_phonebook ${@}
        ;;
    *)
        cd /home/phonebook

        exec ${@}
        ;;
esac
