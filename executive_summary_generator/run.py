import logging

import openai
from environs import Env

from executive_summary_generator.constants import EXECUTIVE_SUMMARY_TEMPLATE

env = Env()
env.read_env()
openai.api_key = env('OPENAI_API_KEY')


def get_short_executive_summary_from_openai_api(input_data_for_executive_summary: str) -> str:
    """ Calls an OpenAI API that uses model for summarization model and returns a short executive summary text.

    :param input_data_for_executive_summary: (str)
    :return: a short executive summary report (str)
    """

    final_text_input = f"Write an executive summary with no more than two " \
                       f"paragraphs using such template with placeholders as example:\n " \
                       f"{EXECUTIVE_SUMMARY_TEMPLATE}\n\n" \
                       f"And use such input data:" \
                       f"{input_data_for_executive_summary}"
    final_text_input = """
Summarise in a few sentences if there some improvements or not for the data below. These data are for the Multi-Domain Capability Rate metric which shows how often different capabilities, like air or land, were used together during testing. This helps understand how well different countries can work together in different situations.

Input data:
nation_name; operational_domain_name; multidomain_rate_2021; multidomain_rate_2022
Nation 45,Air,100,83.3333333333333333
Nation 45,Land,100,100
Nation 45,Maritime,100,100
Nation 45,Cyberspace,100,100
Nation 45,Space,100,100
Nation 45,Other Support Services,80,100

    """
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
