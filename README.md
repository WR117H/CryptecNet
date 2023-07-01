# CryptectNet

![](https://github.com/WR117H/CryptecNet/assets/97615989/a066d9bf-c957-4a18-8ff6-d1a89d42eaf2)

CryptectNet, A tool for chatting with freaks
# Setup
First install CryptectNet using git
```
git clone https://github.com/WR117H/ReverseCam.git
```
Then head to the folder
```
cd CryptecNet
```
Install the requirements using pip
```
pip install -r requirements.txt
```
Change the client's file addresses to whatever you want . . .

# Server useage
| Argument | Useage |
| --- | --- |
| `--ip` | IP address of the host for the chatroom  |
| `--port` | Port number of the host you wanna build tha chatroom on |

# Examples
Server:
```
python server.py --ip 127.0.0.1 --port 9999
```

# Client useage
| Argument | Useage |
| --- | --- |
| `--ip` | Host address to connect to the chat room |
| `--port` | Port number of the host server |
| `--user` | Username for the chatroom |


Client:
```
python client.py --ip 127.0.0.1 --port 9999 --user wraith
```
