import logging

import openai
from fastapi import FastAPI, Body

from .constants import EXECUTIVE_SUMMARY_TEMPLATE

app = FastAPI()


@app.get("/ping")
async def ping():
    return {"message": "pong"}


@app.post("/generate-short-executive-summary")
async def generate_short_executive_summary(text_input: str = Body()):
    try:
        final_text_input = f"Write an executive summary with no more than two " \
                           f"paragraphs using such template with placeholders as example:\n " \
                           f"{EXECUTIVE_SUMMARY_TEMPLATE}\n\n" \
                           f"And use such input data:" \
                           f"{text_input}"

        logging.debug(f"Final input text for Open API call: {final_text_input}")

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=final_text_input,
            temperature=0.7,
            max_tokens=2048,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
        )
        result = response['choices'][0]['text']
    except Exception as e:
        result = f"Something went wrong:\n{e}"

    return {"message": result}