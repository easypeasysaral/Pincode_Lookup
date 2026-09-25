from fastapi.responses import JSONResponse
from fastapi import Request

class PinCodeNotFound(Exception):
    def __init__(self,pincode : str):
        self.pincode = pincode
        
        
class InvalidPinCodeError(Exception):
    def __init__(self, pincode : str, reason:str = "Invalid pincode format"):
        self.pincode = pincode
        self.reason = reason


async def pincode_not_found_handler(request : Request, exc: PinCodeNotFound):
    return JSONResponse(
        status_code=404,
        content = {
            "error" : "Pincode not found",
            "message" : f"No location found with the pincode {exc.pincode}",
            "pincode" : exc.pincode
        }
    )


async def invalid_pincode_error(request : Request, exc : InvalidPinCodeError):
    return JSONResponse(
        status_code=400,
        content={
            "error" : "Invalid pincode",
            "message" : f"Pincode '{exc.pincode}' is invalid. Reason is {exc.reason} ",
            "pincode" : exc.pincode
        }
    )