class ApiValidator:
    def validate(self, requestArgs, requiredArgs):
        for argument in requiredArgs:
            if not argument in requestArgs:
                return {"message": f"Argument required: {argument}"}, 400
        return None
