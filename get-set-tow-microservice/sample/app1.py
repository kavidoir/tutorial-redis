from redis import Redis

redis = Redis(host="172.17.0.2", decode_responses=True)

try:
    redis.ping()
except ConnectionError:
    print("Connection error.")
else:
    print("OK")

redis.set("test", "devops")
