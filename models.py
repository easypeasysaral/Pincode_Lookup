from pydantic import BaseModel, field_validator

class pincodeRequest(BaseModel):
    pincode : str
    
    @field_validator("pincode")
    @classmethod
    def validate_pincode(cls, val):
        if len(val)!=6 or not val.isdigit():
            raise ValueError("Pincode must be exactly 6 digit ")
        
        return val


class LocationResponse(BaseModel):
    pincode : str
    state : str
    city : str
    district : str
    
class BulkRequest(BaseModel):
    pincodes : list[str]
    
    @field_validator("pincodes")
    @classmethod
    def validate_pincodes(cls, vals):
        if len(vals) == 0:
            raise ValueError("At least one pincode is required")
        
        if len(vals) > 20:
            raise ValueError("Maximum 20 pincodes are allowed per request")
        
        for code in vals:
            if len(code)!=6 or not code.isdigit():
                        raise ValueError("Each Pincode must be exactly 6 digit ")
        
        
        return vals

class BulkResponse(BaseModel):
    status : str = "success"
    found : int 
    not_found : int
    results : list[LocationResponse]
    missings : list[str]