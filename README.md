
# CryptoBuyAdvisor

**An AI-powered crypto insight tool built on the AWS Free Tier.**
It doesn’t just suggest what to buy; it warns you when to be cautious!

---

## Project Goals

CryptoBuyAdvisor is a cloud-native application that:
- Fetches real-time data from public crypto APIs
- Uses OpenAI’s GPT API to provide natural-language recommendations
- Alerts users to risky or hype-driven coins (e.g., meme coins, cash-grab coins, etc)
- Is fully serverless and scalable using AWS Free Tier components

This project also prioritizes ethical crypto awareness—helping users understand not just *what* to buy, but *why* they should be cautious.

---

## Current Working Architecture and Application

![Architecture Diagram](docs/Official-AWS-Architecture-Version1.5.png)
> *Check out the [original architecture diagram](docs/Unofficial-AWS-Architecture.png) to appreciate the updates!*

🔗 Live Demo

👉 [Click here to view the hosted MVP frontend](http://crypto-buy-advisor-site.s3-website.us-east-2.amazonaws.com)

> *This version is the static frontend deployed using S3 + IAM best practices; this is the HTTP version for now until AWS Amplify is implemented.*



### Stack (So far):
- AWS S3 (Landing page hosting and possibly cache for lambda)
- AWS CloudFront (planned)
- AWS Lambda (scaffolded)
- AWS CloudFront (possibly cache for lambda)
- API Gateway (planned)
- AWS WAF (planned)
- AWS Secrets Manager (planned)
- OpenAI GPT API (planned)
- CoinGecko API (planned)
- AWS CodePipeline (GitHub integration)
- AWS Amplify (GitHub integration)
- AWS CodeBuild
- CloudWatch Logs/Alarms

---

## DevOps & CI/CD Setup

CryptoBuyAdvisor is integrated with AWS CodePipeline (backend) and AWS Amplify (frontend) to enable continuous delivery.
- GitHub → CodePipeline → Lambda Deployment (planned)
  > *A change to `/backend/lambda_function.py` will automatically trigger redeployment once the pipeline is active.*
  
- GitHub → AWS Amplify → Website/App front (planned)
  > *A change to `/frontend/index.html` will automatically trigger redeployment once the pipeline is active.*
  
- Dev workflow is CI-ready for future integration with GitHub Actions


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
