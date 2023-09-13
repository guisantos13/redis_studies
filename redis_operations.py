import redis
import json
import os
import spotify_consume



# Global Environment Variables
host = os.environ.get("host")
port = os.environ.get("port")
password = os.environ.get("password")

# Variables to connect spotify API
client_id = os.environ.get("client_id_spotify")
client_secret = os.environ.get("client_secret_spotify")

def get_redis_connection():
    """
    This function is used to get the redis connection object
    :return: redis connection object
    """
    try:
        r = redis.StrictRedis(
            host=host,
            port=int(port),
            password=password,
            charset="utf-8",
            decode_responses=True,
            db=0
            
        )
        return r
    except Exception as e:
        print(f"[ Error | In get_redis_connection function: {e}]")
        return None

def redis_populate_db_spotify(band_name:str, qnt_albums:int):
    """
    This function is used to populate the redis database
    :return: None
    """
    try:
        redis_con = get_redis_connection()
        if redis_con.ping():
            print(f"[ Info | Redis Connection: {redis_con}]")
            albuns = spotify_consume.get_artist_for_name(client_id, client_secret, band_name, qnt_albums)
            if albuns:
                print(f"[ Info | Populate Redis With Albuns: {band_name} ]")
                for key, value in albuns.items():
                    redis_con.set(key, json.dumps(value))
                redis_con.close()
                return albuns                
            else:
                print("[ Error | In redis_populate_db function: Albuns is None]")    
                return None
            
    except Exception as e:
        print(f"[ Error | In redis_populate_db function: {e}]")
        return None

list_od_bands = ["Ponto de Equilibrio", "Mato Seco", "Soja", "Bob Marley"]
add_in_redis = []
for band in list_od_bands:
    add_in_redis.append(redis_populate_db_spotify(band, 50))
print(add_in_redis)


