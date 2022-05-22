from fastapi.logger import logger
from starlette import status
from fastapi import Response

from .response import ResponseOutCustom


def handle_error_code(out_response: ResponseOutCustom, response: Response):
    """
    This function allows change HTTP status code based on given out_rseponse
    @rtype: object
    """
    # check if not None
    if out_response:
        # FastAPI can understand the success message 200 and 201, so we just handle the error
        http_code = out_response.__dict__.get('http_code', None)
        status_message = out_response.__dict__.get('status', None)
        if http_code:
            response.status_code = http_code
        else:
            if out_response.message_id == "01":

                # if not found
                logger.debug(f"status_message {status_message.lower()}")
                if 'not found' in status_message.lower():
                    response.status_code = 207  # we change to 200 family response as it actually working but no list data.
                else:
                    # The server could not understand the request due to invalid syntax.
                    response.status_code = status.HTTP_400_BAD_REQUEST
            elif out_response.message_id == "02":
                #     The server has encountered a situation it does not know how to handle.
                response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
    else:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR