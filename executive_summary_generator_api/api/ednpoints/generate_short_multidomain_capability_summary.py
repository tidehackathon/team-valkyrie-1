import logging

from fastapi import APIRouter

from ..models import TextInput
from ..utils import get_response_from_open_api_summary_model

router = APIRouter()


@router.post("/generate-short-multidomain-capability-summary")
def generate_short_executive_summary(text_input: TextInput):
    """ A main endpoint that prepares the input text and calls OpenAPI API
    to generate a Multi-Domain Capability summary

    Example of recommended body for this endpoint:

        {
            "text_input": "nation_name; operational_domain_name; multidomain_rate_2021; multidomain_rate_2022\n
                           Nation 45,Air,100,83.\n3333333333333333\nNation 45,Land,100,100\n
                           Nation 45,Maritime,100,100\nNation 45,Cyberspace,100,100\n
                           Nation 45,Space,100,100\n
                           Nation 45,Other Support Services,80,100"
        }

    It should be like a CSV content.
    """
    final_text_input = f"Summarise in a few sentences if there some improvements or not for the data below. " \
                       f"These data are for the Multi-Domain Capability Rate metric which shows how often " \
                       f"different capabilities, like air or land, were used together during testing. " \
                       f"This helps understand how well different countries can work together in " \
                       f"different situations." \
                       f"Input data:" \
                       f"{text_input}"

    logging.debug(f"Final input text for Open API call: {final_text_input}")

    result = get_response_from_open_api_summary_model(final_text_input)

    return {"message": result}
