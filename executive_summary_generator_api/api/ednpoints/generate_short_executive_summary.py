import logging

from executive_summary_generator_api.api.constants import EXECUTIVE_SUMMARY_TEMPLATE
from executive_summary_generator_api.api.models import TextInput
from executive_summary_generator_api.api.utils import get_response_from_open_api_summary_model
from executive_summary_generator_api.service import app


@app.post("/generate-short-executive-summary")
def generate_short_executive_summary(text_input: TextInput):
    """ A main endpoint that prepares the input text and calls OpenAPI API to generate an executive summary """
    final_text_input = f"Write an executive summary with no more than two " \
                       f"paragraphs using such template with placeholders as example:\n " \
                       f"{EXECUTIVE_SUMMARY_TEMPLATE}\n\n" \
                       f"And use such input data:" \
                       f"{text_input}"

    logging.debug(f"Final input text for Open API call: {final_text_input}")

    result = get_response_from_open_api_summary_model(final_text_input)

    return {"message": result}
