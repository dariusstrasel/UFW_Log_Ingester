from ingester_server import db
# Primary database models


class Log_Events(db.Model):
    """Class Data Model used to represent a single UFW log event."""
    Column = db.Column
    Integer = db.Integer
    String = db.String

    __tablename__ = 'log_events'
    _id = Column(Integer, primary_key=True)
    month = Column(String(250), nullable=False)
    day = Column(Integer)
    time = Column(String(25))
    hostname = Column(String(25))
    block_type = Column(String(25))
    uptime = Column(String(25))
    type = Column(String(25))
    IN = Column(String(25))
    OUT = Column(String(25))
    MAC = Column(String(25))
    SRC = Column(String(25))
    DST = Column(String(25))
    LEN = Column(String(25))
    TOS = Column(String(25))
    PREC = Column(String(25))
    TTL = Column(String(25))
    ID = Column(String(25))
    DF = Column(String(25))
    PROTO = Column(String(25))
    SPT = Column(String(25))
    DPT = Column(String(25))
    WINDOW = Column(String(25))
    RES = Column(String(25))
    SYN = Column(String(25))
    URGP = Column(String(25))
    ACK = Column(String(25))
    CWR = Column(String(25))
    ECE = Column(String(25))

    def __repr__(self):
        return '<Log Event %r>' % self._id

# Create database tables from models
db.create_all()
