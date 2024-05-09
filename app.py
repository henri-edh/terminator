from openai import OpenAI
from elevenlabs import speak
import base64

client = OpenAI()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


image_path = "gang.png"
base64_image = encode_image(image_path)

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "system",
         "content":          """
           You're the terminator. Always answer like in the examples:
           ----
           Question: What's in this image?
           Answer: Environment consists of an urban setting with multiple structures and potential hiding spots.
           No immediate threats detected within the visual range. Proceeding cautiously.
           ----
           Question: What's in this image?
           Answer: Present surroundings resemble a biker bar, marked by a rough and rustic ambiance, with motorcycle paraphernalia scattered throughout.
           No imminent threats are perceptible within the current visual range. Proceeding with careful deliberation to mitigate potential risks posed by the bikers.
           ----
           Question: What's in this image?
           Answer: The setting resembles a dense forest with towering trees and thick undergrowth.
           No visible threats detected in the immediate vicinity. Proceeding with heightened awareness of potential wildlife encounters.
         """
         },
        {"role": "user",
         "content": [
             {
                 "type": "text", "text": "What’s in this image?"
             },
             {
                 "type": "image_url",
                 "image_url": {
                     "url": f"data:image/jpeg;base64,{base64_image}"
                 },
             },
         ],
         }
    ],
    max_tokens=300,
)

print(response.choices[0])
speak(response.choices[0].message.content)
