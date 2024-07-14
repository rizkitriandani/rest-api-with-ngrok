from dotenv import load_dotenv
from flask import Flask, jsonify, request
from groq import Groq
import os

app = Flask(__name__)

load_dotenv()


def check_spirit_animal(date: str, full_name: str):
    client = Groq(
        api_key=os.environ.get("GROQ_API_KEY"),
    )

    prompt = f"""given a date of birth and full name, check the date on various calendar, from gregorian, chinese, islamic and javanese calendar

and then try to make a fun "spirit animal" based on all those various calendars, the zodiac charesterics based on date of birth and combined with the meaning of the full name.

make it unique but consistent for each calendar. only return the name of spirit animal and its description, don't return the steps you take to reach the conclusion. make it short.

note that the date is in DD-MM-YYYY format
date : {date}
full name: {full_name}"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-70b-8192",
    )

    return chat_completion.choices[0].message.content


@app.route("/hello", methods=["GET"])
def hello():
    # print(f"{check_spirit_animal('what is LLM?')}")
    return jsonify({"message": "Hello, World!"})


@app.route("/check-spirit-animal", methods=["POST"])
def check_spirit_animal_api():
    date = request.json["date"]
    name = request.json["name"]
    response = check_spirit_animal(date=date, full_name=name)
    return jsonify({"message": response})


if __name__ == "__main__":
    app.run(debug=True)
