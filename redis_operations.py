import redis
import json
import os


# Global Environment Variables
host = os.environ.get("host")
port = os.environ.get("port")
password = os.environ.get("password")


def get_redis_connection():
    """
    This function is used to get the redis connection object
    :return: redis connection object
    """
    try:
        r = redis.StrictRedis(
            host=host,
            port=port,
            password=password,
            charset="utf-8",
            decode_responses=True,
            db=0,
        )
        return r
    except Exception as e:
        print(f"[ Error | In get_redis_connection function: {e}]")
        return None


redis_connection = get_redis_connection()
print(f"Redis Connection: {redis_connection}")
