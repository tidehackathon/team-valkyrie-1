import openai
from environs import Env

env = Env()
env.read_env()
openai.api_key = env('OPENAI_API_KEY')


def get_response_from_open_api_summary_model(text_input: str) -> str:
    """ Calls Summary model trough OpenAPI API to generate some summary """
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=text_input,
            temperature=0.7,
            max_tokens=2048,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        result = response['choices'][0]['text']
    except Exception as e:
        result = f"Something went wrong:\n{e}"

    return result
