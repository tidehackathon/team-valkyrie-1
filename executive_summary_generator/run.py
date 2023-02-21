import logging

import openai
from environs import Env

env = Env()
env.read_env()
openai.api_key = env('OPENAI_API_KEY')


def get_short_executive_summary_from_openai_api(input_data_for_executive_summary: str) -> str:
    """ Calls an OpenAI API that uses model for summarization model and returns a short executive summary text.

    :param input_data_for_executive_summary: (str)
    :return: a short executive summary report (str)
    """
    with open('summary_template.txt', 'r') as file:
        template_text = file.readlines()

    final_text_input = f"Write an executive summary with no more than two " \
                       f"paragraphs using such template:\n {''.join(template_text)}\n\n" \
                       f"And use such input data:" \
                       f"{input_data_for_executive_summary}"
    logging.debug(f"Final input text for Open API call: {final_text_input}")
    result = openai.Completion.create(
        model="text-davinci-003",
        prompt=final_text_input,
        temperature=0.7,
        max_tokens=2048,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.0
    )

    return result['choices'][0]['text']


if __name__ == "__main__":
    # Give some context and metrics as text for input
    example_input_data_for_summary = "\n\nUkraine participated in " \
                 "CWIX 2021 with 2 capability configuration(s) provided by 1 organization(s). " \
                 "National capabilities where deployed in 1 location(s), connected to 2 " \
                 "network(s) and got involved in 2 focus area(s), to assess interoperability " \
                 "with capabilities from 13 nation(s).\n\n" \
                 "Participating Military Organizations:\n\nArmed Forces of Ukraine (2).\n\n" \
                 "Non-military organizations and Industry:\n\n" \
                 "Focus Areas:\n\nMultilateral Interoperability Programme (1); Cyber Defence (1).\n\n" \
                 "Test Partners: Bulgaria; Canada; Denmark; Estonia; France; Germany; Hungary; NATO; Netherlands; " \
                 "Poland; Portugal; Romania; Spain.\n\nCWIX Tasks:\n\nSystem Testing (1); Cyber Defence (1).\n\n" \
                 "Capability Maturity:\n\nDevelopmental (1); Experimental (1).\n\n" \
                 "Deployment Sites:\n\n Home or Office, Internet (NATO) (2).\n\nNetworks:\n\n" \
                 "Cyber (1); MIP VPN (1)."
    # And call the function below to get a short executive summary
    res = get_short_executive_summary_from_openai_api(example_input_data_for_summary)

    print(f"Final ChatGPT response:\n{res}")
