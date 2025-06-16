from typing import Dict, Any, Optional, List
import requests
import base64

def remove_video_background(
    api_key: str,
    video_data: Optional[bytes] = None,
    video_url: Optional[str] = None,
    resolution: Optional[str] = None,
    frame_rate: Optional[str] = None,
    content_moderation: bool = False
) -> Dict[str, Any]:
    


    url = "https://engine.prod.bria-api.com/v1/video/background/remove"
    
    headers = {
        'api_token': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Prepare request data
    data = {
        'content_moderation': content_moderation
    }
    
    # Add video source
    if video_url:
        data['video_url'] = video_url
    elif video_data:
        data['file'] = base64.b64encode(video_data).decode('utf-8')
    else:
        raise ValueError("Either video_data or video_url must be provided")
    
    # Add optional parameters
    if resolution:
        data['resolution'] = resolution
    if frame_rate:
        data['frame_rate'] = frame_rate
    
    try:
        print(f"Making request to: {url}")
        print(f"Headers: {headers}")
        print(f"Data keys: {data.keys()}")  # Don't print full video data
        
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        
        print(f"Response status: {response.status_code}")
        print(f"Response body: {response.text}")
        
        return response.json()
    except Exception as e:
        raise Exception(f"Video background removal failed: {str(e)}")

def check_video_processing_status(
    api_key: str,
    processing_id: str
) -> Dict[str, Any]:
    

    url = f"https://engine.prod.bria-api.com/v1/video/status/{processing_id}"
    
    headers = {
        'api_token': api_key,
        'Accept': 'application/json'
    }
    
    try:
        print(f"Making status request to: {url}")
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        print(f"Status response: {response.status_code}")
        print(f"Status body: {response.text}")
        
        return response.json()
    except Exception as e:
        raise Exception(f"Failed to check processing status: {str(e)}")
    

    