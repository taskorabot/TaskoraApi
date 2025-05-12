"""
reCaptchaV3 Solver Example Program

This script demonstrates how to use the reCaptchaV3Solver client
to solve reCAPTCHA v3 tokens using an external API.

Requirements:
- requests (or another library based on the actual implementation)

Run:
    python recaptcha_example.py
"""

from TaskoraApi import AiohttpreChaptchaAPI


def main():
    api_key = "your_api_key"
    site_key = "site_key_here"
    url = "https://example.com"  # The page where the reCAPTCHA is implemented

    solver = AiohttpreChaptchaAPI(api_key=api_key)
    token = solver.rechaptcha_v3_solver(site_key=site_key, url=url)

    print("Solved reCAPTCHA token:", token)



