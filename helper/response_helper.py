from fastapi.responses import JSONResponse

def success(message: str, data=None):
    data = {"status": "success", "message": message, "data": data}
    response = JSONResponse(data,status_code=200)
    return response


def error(message: str, status_code:int=500,data=None):
    data = {"status": "error", "message": message, "data": data}
    response = JSONResponse(data,status_code=status_code)
    return response
