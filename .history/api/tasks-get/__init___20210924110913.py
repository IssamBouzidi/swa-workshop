import logging

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            tasks = [
                {
                    "id": 1,
                    "label": "🍔 Eat",
                    "status": ""
                },
                {
                    "id": 2,
                    "label": "🛏 Sleep",
                    "status": ""
                },
                {
                    "id": 3,
                    "label": "</> Code",
                    "status": ""
                }
            ]

            req_body = req.get_json(tasks)
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
