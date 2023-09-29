import openai
openai.api_key="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"

def generate_response(myprompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        # ChatGPT role:
        prompt= "Your role is to act as a licensed therapist ###"+ myprompt,
        temperature=.1,
        max_tokens=1024
    )
    print (response.choices)
    return response.choices[0].text.strip()

def main ():
    # st.title("Friendly Chat with Dr. Truong")
    myprompt = input("I am Dr. Truong. I am a licensed Therapist. How can I help you? \n")
    print(generate_response(myprompt))
    # if st.button("Submit"):
    #     st.write(generate_response(myprompt))

if __name__ == "__main__":
    main()
