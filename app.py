from openai import OpenAI
import base64

client = OpenAI()


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode('utf-8')


image_path = "bikes.jpg"
base64_image = encode_image(image_path)

image_path2 = "biker.jpg"
base64_image2 = encode_image(image_path2)

response = client.chat.completions.create(
    model="gpt-4-turbo",
    messages=[
        {"role": "user",
         "content": [
          {
              "type": "text", "text": "What’s in this image? Keep it short!"
          },
             {
              "type": "image_url",
              "image_url": {
                  "url": f"data:image/jpeg;base64,{base64_image}"
              },
          },
             {
              "type": "image_url",
              "image_url": {
                  "url": f"data:image/jpeg;base64,{base64_image2}"
              },
          },
         ],
        }
    ],
    max_tokens=300,
)

print(response.choices[0])
