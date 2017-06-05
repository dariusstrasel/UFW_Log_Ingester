from db.models import Log_Events
from ingester_server import db
from utils import parser
import json


def get_all_log_events():
    """Query all log_events in the database and return as JSON.
    () -> JSON"""

    query_results = Log_Events.query.all()
    output = {'results': []}
    for result in query_results:
        new_result = result.__dict__

        # Remove unneeded ORM metadata
        del new_result['_sa_instance_state']
        output['results'].append(new_result)

    # If no results, insert log_file.
    if len(output['results']) < 2:
        print("Database is empty: inserted new log_file.")
        insert_log_file("./logs/ufw.log")
        output['results'].append(None)

    return output


def insert_log_event(raw_log_event):
    """Inserts an individual log_event into the local database."""
    key = raw_log_event.get
    new_log_event = Log_Events(
        month=key('month'),
        day=key('day'),
        time=key('time'),
        hostname=key('hostname'),
        block_type=key('block_type'),
        uptime=key('uptime'),
        type=key('type'),
        IN=key('IN'),
        OUT=key('OUT'),
        MAC=key('MAC'),
        SRC=key('SRC'),
        DST=key('DST'),
        LEN=key('LEN'),
        TOS=key('TOS'),
        PREC=key('PREC'),
        TTL=key('TTL'),
        ID=key('ID'),
        DF=key('DF'),
        PROTO=key('PROTO'),
        SPT=key('SPT'),
        DPT=key('DPT'),
        WINDOW=key('WINDOW'),
        RES=key('RES'),
        SYN=key('SYN'),
        URGP=key('URGP'),
        ACK=key('ACK'),
        CWR=key('CWR'),
        ECE=key('ECE'),
    )

    db.session.add(new_log_event)
    db.session.commit()


def insert_log_file(log_file_path):
    """Accepts a log file path and inserts into the local database.
    (path string) -> dictionary

    insert_log_file("./logs/ufw.log")
    """
    parser_results = parser.process_file(log_file_path)

    return [insert_log_event(result) for result in parser_results]
