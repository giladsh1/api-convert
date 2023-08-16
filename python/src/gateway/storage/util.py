import pika, json


def upload(f, fs, channel, access):
    print("running utils upload function")
    try:
        fid = fs.put(f)
    except Exception as err:
        print("Error in upload function before posting to mongo")
        print(err)
        return "internal server error", 500

    message = {
        "video_fid": str(fid),
        "mp3_fid": None,
        "username": access["username"],
    }

    print(f"fid: {fid}")

    try:
        channel.basic_publish(
            exchange="",
            routing_key="video",
            body=json.dumps(message),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ),
        )
    except Exception as err:
        print("Error in upload function after posting to mongo")
        print(err)
        fs.delete(fid)
        return "internal server error", 500
