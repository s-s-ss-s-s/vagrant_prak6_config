Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64" 

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 1
    vb.memory = "1024"  
  end

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.synced_folder "./", "/vagrant"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get upgrade -y

    apt-get install -y python3 python3-pip sqlite3

    pip3 install fastapi uvicorn

    sqlite3 /home/vagrant/database.db <<EOF
CREATE TABLE IF NOT EXISTS items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);
INSERT INTO items (name) VALUES ('Item 1'), ('Item 2');
EOF

    echo "from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect('/home/vagrant/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get('/')
def read_root():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return {'items': [dict(item) for item in items]}" > /home/vagrant/app.py

    Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/focal64" 

  config.vm.provider "virtualbox" do |vb|
    vb.cpus = 1
    vb.memory = "1024"  
  end

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.synced_folder "./", "/vagrant"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update
    apt-get upgrade -y

    apt-get install -y python3 python3-pip sqlite3

    pip3 install fastapi uvicorn

    sqlite3 /home/vagrant/database.db <<EOF
CREATE TABLE IF NOT EXISTS items (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL
);
INSERT INTO items (name) VALUES ('Item 1'), ('Item 2');
EOF

    echo "from fastapi import FastAPI
import sqlite3

app = FastAPI()

def get_db_connection():
    conn = sqlite3.connect('/home/vagrant/database.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.get('/')
def read_root():
    conn = get_db_connection()
    items = conn.execute('SELECT * FROM items').fetchall()
    conn.close()
    return {'items': [dict(item) for item in items]}" > /home/vagrant/app.py
    sudo nohup uvicorn app:app --host 0.0.0.0 --port 8000 & 
  SHELL
end