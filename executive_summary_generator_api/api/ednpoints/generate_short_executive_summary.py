import logging

from fastapi import APIRouter

from ..constants import EXECUTIVE_SUMMARY_TEMPLATE
from ..models import TextInput
from ..utils import get_response_from_open_api_summary_model

router = APIRouter()


@router.post("/generate-short-executive-summary")
def generate_short_executive_summary(text_input: TextInput):
    """ A main endpoint that prepares the input text and calls OpenAPI API to generate an executive summary

    Example of recommended body for this endpoint:

        {
            "text_input": "Ukraine participated in CWIX 2021 with 2 capability configuration(s) provided by
                           1 organization(s). National capabilities where deployed in 1 location(s), connected
                           to 2 network(s) and got involved in 2 focus area(s), to assess interoperability with
                           capabilities from 13 nation(s).\n\n Participating Military Organizations:\n\nArmed
                           Forces of Ukraine (2).\n\n Non-military organizations and Industry:\n\n Focus
                           Areas:\n\nMultilateral Interoperability Programme (1); Cyber Defence (1).\n\n Test
                           Partners: Bulgaria; Canada; Denmark; Estonia; France; Germany; Hungary; NATO;
                           Netherlands;  Poland; Portugal; Romania; Spain.\n\nCWIX Tasks:\n\nSystem Testing (1);
                           Cyber Defence (1).\n\n Capability Maturity:\n\nDevelopmental (1);
                           Experimental (1).\n\n Deployment Sites:\n\n Home or Office,
                           Internet (NATO) (2).\n\nNetworks:\n\n Cyber (1); MIP VPN (1)."
        }
    """
    final_text_input = f"Write an executive summary with no more than two " \
                       f"paragraphs using such template with placeholders as example:\n " \
                       f"{EXECUTIVE_SUMMARY_TEMPLATE}\n\n" \
                       f"And use such input data:" \
                       f"{text_input}"

    logging.debug(f"Final input text for Open API call: {final_text_input}")

    result = get_response_from_open_api_summary_model(final_text_input)

    return {"message": result}
