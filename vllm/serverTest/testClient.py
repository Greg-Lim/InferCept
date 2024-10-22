import requests
import json
import vllm.sampling_params

# Define the server details
HOST = "http://localhost"
PORT = 8000
BASE_URL = f"{HOST}:{PORT}"

# Test data for the `/generate` endpoint
def test_generate():
    url = f"{BASE_URL}/generate"
    headers = {"Content-Type": "application/json"}

    # """Generate completion for the request.

#     The request should be a JSON object with the following fields:
#     - prompt: the prompt to use for the generation.
#     - stream: whether to stream the results or not.
#     - other fields: the sampling parameters (See `SamplingParams` for details).
#     """
    sampling_param = vllm.sampling_params.SamplingParams()
    print(sampling_param)

    # Sample request body
    request_data = {
        "prompt": "What colors are apples?",
        "stream": False,
        # "sampling_params": {}
    }

    # Make the POST request to `/generate`
    response = requests.post(url, headers=headers, data=json.dumps(request_data))

    # Print out the response
    if response.status_code == 200:
        print("Response from /generate:", response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)

# Test data for the `/resume` endpoint
def test_resume(request_id):
    url = f"{BASE_URL}/resume"
    headers = {"Content-Type": "application/json"}

    # Sample request body for resuming the request
    request_data = {
        "request_id": request_id,
        "api_return_length": 32  # Specify how many tokens to return
    }

    # Make the POST request to `/resume`
    response = requests.post(url, headers=headers, data=json.dumps(request_data))

    # Print out the response
    if response.status_code == 200:
        print("Response from /resume:", response.json())
    else:
        print(f"Error: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    # Test the `/generate` endpoint first
    test_generate()

    # If needed, you can test `/resume` after getting a valid request ID
    # test_resume(request_id="12345")
