from deta import Deta
from gtts import gTTS
from io import BytesIO

mp3_fp = BytesIO()
tts = gTTS('hello', lang='en')
tts.save('sp.mp3')
tts.write_to_fp(mp3_fp)

#load env variables
#load_dotenv(".env")
DETA_PROJECT_KEY = 'b0s9fmnfh3t_YZZd4WeTqbFLxrTb3VEafYF874wGktCA'

#initialize
deta = Deta(DETA_PROJECT_KEY)

#connect to database
db = deta.Base('nanny')

def insert_d1(key, type, date_time, year, month, day, time):
    """returns the report on success, otherwise returns errror"""
    return db.put(
                    {
                    'key': key, 
                    'type': type, 
                    'date_time': date_time, 
                    'year': year, 
                    'month': month, 
                    'day': day, 
                    'time': time
                    }
                )

def get_all_periods():
    """returns dict of all periods"""
    response = db.fetch()
    return response.items

def get_period(period):
    return db.get(period)