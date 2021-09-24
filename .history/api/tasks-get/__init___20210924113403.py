import logging
import json

import azure.functions as func


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    tasks = {
                [
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
            }

    return func.HttpResponse(
            json.dumps(tasks),
            mimetype="application/json",
            status_code=200
        )
        
    # name = req.params.get('name')
    # if not name:
    #     try:
    #         tasks = {
    #             [
    #                 {
    #                     "id": 1,
    #                     "label": "🍔 Eat",
    #                     "status": ""
    #                 },
    #                 {
    #                     "id": 2,
    #                     "label": "🛏 Sleep",
    #                     "status": ""
    #                 },
    #                 {
    #                     "id": 3,
    #                     "label": "</> Code",
    #                     "status": ""
    #                 }
    #             ]
    #         }

    #         req_body = req.get_json()
    #     except ValueError:
    #         pass
    #     else:
    #         name = req_body.get('name')

    # if name:
    #     return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    # else:
    #     return func.HttpResponse(
    #         json.dumps(tasks),
    #         mimetype="application/json",
    #         status_code=200
    #     )
