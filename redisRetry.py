from redis import Redis
from redis.backoff import ExponentialBackoff
from redis.retry import Retry

retry = Retry(ExponentialBackoff(), 3)
redis = Redis(host="172.17.0.2", decode_responses=True, retry=retry)

try:
    redis.ping()
except ConnectionError:
    print("Connection error.")
