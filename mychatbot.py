import google.generativeai as genai

key = "**** **** **** ****"
print(key)

genai.configure(api_key=key)
Model = genai.GenerativeModel("gemini-2.5-pro")

while True:
    user = input("Search : , Type 'bye bye' to close: ")

    if user.lower() == "exit":
        print("bye bye")
        break

    response = Model.generate_content(user)
    
    print("bot:", response.text)