import json
import os

from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, Field, model_validator

TEST_VECTORS_DIR = "test_vectors"

app = FastAPI()

current_test_vector = ""
last_request = None


class FrequencyRange(BaseModel):
    startHz: int
    endHz: int


class Channel(BaseModel):
    globalOperatingClass: int


class DeviceDescriptor(BaseModel):
    serialNumber: str
    certificationId: list[dict]


class Location(BaseModel):
    ellipse: dict
    elevation: dict
    indoorDeployment: str


class AvailableSpectrumInquiryRequest(BaseModel):
    requestId: str
    deviceDescriptor: DeviceDescriptor
    location: Location
    inquiredFrequencyRange: FrequencyRange | None = None
    inquiredChannels: list[Channel] | None = None

    @model_validator(mode="after")
    def validate_inquiry_fields(cls, values):
        if not values.inquiredFrequencyRange and not values.inquiredChannels:
            raise ValueError(
                "Either inquiredFrequencyRange or inquiredChannels must be provided."
            )
        return values


class SpectrumInquiryRequest(BaseModel):
    version: str
    availableSpectrumInquiryRequests: list[AvailableSpectrumInquiryRequest]


@app.post("/availableSpectrumInquiry")
async def available_spectrum_inquiry(request: SpectrumInquiryRequest):
    global current_test_vector, last_request

    last_request = request.json()

    if not current_test_vector:
        raise HTTPException(status_code=400, detail="Test vector is not set")

    test_vector_path = os.path.join(TEST_VECTORS_DIR, f"{current_test_vector}.json")
    if not os.path.exists(test_vector_path):
        raise HTTPException(status_code=404, detail="Test vector not found")

    with open(test_vector_path, "r") as f:
        response_data = json.load(f)

    return response_data


@app.post("/setTestVector")
async def set_test_vector(test_vector: str):
    global current_test_vector

    test_vector_path = os.path.join(TEST_VECTORS_DIR, f"{test_vector}.json")
    if not os.path.exists(test_vector_path):
        raise HTTPException(status_code=404, detail="Test vector not found")

    current_test_vector = test_vector
    return {
        "message": "Test vector set successfully",
        "test_vector": current_test_vector,
    }


@app.get("/getLastRequest")
async def get_last_request():
    if last_request is None:
        raise HTTPException(status_code=404, detail="No request logged")

    return json.loads(last_request)


if not os.path.exists(TEST_VECTORS_DIR):
    os.makedirs(TEST_VECTORS_DIR)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
