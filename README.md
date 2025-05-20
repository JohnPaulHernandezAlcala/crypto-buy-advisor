
# CryptoBuyAdvisor

**An AI-powered crypto insight tool built on the AWS Free Tier.**
It doesn’t just suggest what to buy—it warns you when to be cautious.

---

## Project Goals

CryptoBuyAdvisor is a cloud-native application that:
- Fetches real-time data from public crypto APIs
- Uses OpenAI’s GPT API to provide natural-language recommendations
- Alerts users to risky or hype-driven coins (e.g., meme coins)
- Is fully serverless and scalable using AWS Free Tier components

This project also prioritizes ethical crypto awareness—helping users understand not just *what* to buy, but *why* they should be cautious.

---

## Current Working Architecture

![Draft Architecture Diagram](docs/Unofficial AWS Architecture.drawio.png)
> *Official Architecture Diagram coming soon!*



### Stack (So far):
- AWS S3 (Landing page hosting and possibly cache for lambda)
- AWS CloudFront
- AWS Lambda (scaffolded)
- Dynamo DB (possibly cache for lambda)
- API Gateway (planned)
- AWS WAF
- AWS Secrets Manager (planned)
- OpenAI GPT API (planned)
- CoinGecko API (planned)
- AWS CodePipeline (GitHub integration)
- CloudWatch Logs/Alarms

---

## DevOps & CI/CD Setup

CryptoBuyAdvisor is integrated with AWS CodePipeline to enable continuous delivery.
- GitHub → CodePipeline → Lambda Deployment (planned)
- Dev workflow is CI-ready for future integration with GitHub Actions or AWS Amplify

> *A change to `/backend/lambda_function.py` will automatically trigger redeployment once the pipeline is active.*

---

## Why I Built This

I recently passed the AWS Certified Solutions Architect – Associate exam. This project puts those concepts into practice. My goal is to build something intelligent, scalable, and ethically responsible.

Check back soon for live demos, trust scores, and a GPT-powered crypto advisor.

---

## Coming Soon

- Live crypto query interface
- Risk scoring system
- GPT-powered natural-language recommendations
- Trust score display
- Secure & scalable deployment pipeline
