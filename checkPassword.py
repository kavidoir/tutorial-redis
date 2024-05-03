from redis import Redis

redis = Redis(host="172.17.0.2", decode_responses=True)

try:
    redis.ping()
except ConnectionError:
    print("Connection error.")
    exit(1)

user = "majid"
password = "123456"

auth_count_key = ":".join(["auth", user, "auth_count"])
auth_blocked_key = ":".join(["auth", user, "blocked"])

ask_password = input("Enter password: ")

if redis.exists(auth_blocked_key) != 0:
    print("Authentication is currently blocked for this user.")
    exit(1)

if password != ask_password:
    # if redis.exists(auth_count_key) == 0:
    #     redis.set(auth_count_key, 0)
    redis.setnx(auth_count_key, 0)
    current_auth_count = redis.get(auth_count_key)
    if int(current_auth_count) < 2:
        redis.incr(auth_count_key)
    else:
        redis.setex(auth_blocked_key, 60, 1)
        redis.set(auth_count_key, 0)
    print("Invalid password")
    exit(1)

redis.set(auth_count_key, 0)
print("Welcome to ...")
