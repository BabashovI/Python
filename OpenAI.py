
import openai
openai.api_key = "qwe"


def generate_text(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return completions.choices[0].text


generated_text = generate_text("create python script for parsing any news ")
print(generated_text)
