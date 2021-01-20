import cv2
import time
import calendar
from datetime import datetime
from dateutil import tz
from pathlib import Path


def load_config() -> {}:
    options = {}
    with open('config.txt', 'r') as f:
        lines = f.readlines()
        for line in lines:
            try:
                if line.strip().startswith('#') or len(line.strip()) < 1:
                    continue
                line = line.strip()
                split_index = line.index(':')
                argument = line[:split_index]
                value = line[split_index + 1:]
                options[argument] = value
            except:
                print('invalid line in config: ' + line)
    return options

def grab_frame(url: str, quality: int) -> bytes:
    cap = cv2.VideoCapture(url)
    try:
        ret, frame = cap.read()
        if not ret:
            return None
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), quality]
        res, img = cv2.imencode('.jpg', frame, encode_param)
        return img.tobytes()
    except Exception as err:
        print(f'ERROR: {err}')
        return None
    finally:
        cap.release()

def get_timestamp() -> int:
    return int(calendar.timegm(time.gmtime()))

def format_timestamp(timestamp: str, name_format: str) -> str:
    if name_format == 'unix':
        return timestamp
    if name_format == 'utc':
        return datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%dT%H-%M-%SZ")
    if name_format == 'local':
        from_zone = tz.tzutc()
        to_zone = tz.tzlocal()
        utc = datetime.utcfromtimestamp(timestamp)
        utc = utc.replace(tzinfo=from_zone)
        return utc.astimezone(to_zone).strftime("%Y-%m-%dT%H-%M-%S")
    print('invalid name_format in config')
    return timestamp

if __name__ == "__main__":
    config = load_config()
    print(f'config options: {str(config)}')

    while True:
        current_time = get_timestamp()

        Path(config['image_directory']).mkdir(parents=True, exist_ok=True)
        img_data = grab_frame(config['rtsp_url'], int(config['quality']))
        if img_data is not None:
            with open(f'{config["image_directory"]}{format_timestamp(current_time, config["name_format"])}.jpg', 'wb') as f:
                f.write(img_data)
            print(f'captured: {current_time}.jpg')
        else:
            print(f'capture failed at: {current_time}')

        capture_time = get_timestamp() - current_time
        sleep_time = int(config['interval']) - capture_time
        if sleep_time > 0:
            time.sleep(sleep_time)
