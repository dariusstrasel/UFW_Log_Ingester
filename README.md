# UFW Log Ingester // Python
Author: Darius Strasel @dariusstrasel
# Overview:
An API endpoint for getting Uncomplicated Firewall,—(UFW), log data from a local log parser.

# How to install:

1. Clone repo
2. Install module requirements:
```bash
pip install -r requirements.txt
```

# How to Use:
1. Start the endpoint via:
```bash
python ingester_server.py
```
2. Visit the endpoint at the default host location

e.g.
```bash
http://127.0.0.1:5000/
```
The database will create itself (SQLite) and populate via a local log_file if detected as empty. 
```bash
./logs/ufw.log
```

Execute step 2 again to review query results.