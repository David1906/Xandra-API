import logging
from flask import request
from Utils.ApiValidator import ApiValidator


def ValidateArgs(requiredArgs):
    def decorator(method):
        def wrapper(ref):
            validation = ApiValidator().validate(request.args, requiredArgs)
            if validation != None:
                return validation
            return method(ref)

        return wrapper

    return decorator


def HandleInternalError(method):
    def wrapper(ref):
        try:
            return method(ref)
        except Exception as e:
            logging.error(str(e))
            return {"message": f"Internal error: {str(e)}"}, 500

    return wrapper
