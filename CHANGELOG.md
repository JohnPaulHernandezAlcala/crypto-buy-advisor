# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/):

Added — new features
Changed — changes to existing functionality
Deprecated — soon-to-be removed features
Removed — features that were removed
Fixed — bug fixes
Security — vulnerabilities fixed
v1.0.0 → First official version
v1.1.0 → Added some new features
v1.1.1 → Small bug fix
v2.0.0 → Big major update


## [Unreleased]
- 

## [0.2.2] - 2025-06-11

### Added
- Webhook event filter to CodePipeline to push updates if lambda_function.py updated

---

## [0.2.1] - 2025-06-09

### Added
- buildspec.yml edited to correct import error for lambda_function.py in lambda function

---

## [0.2.0] - 2025-06-06

### Added
- CodePipeline pipeline built
- CodeBuild project created
- requirements.txt added to /backend
- buildspec.yml added to /backend
- STRUGGLE_LOG.md added to root


---

## [0.1.0] - 2025-06-05
### Removed
- S3 bucket used for static website hosting.

### Added
- AWS Amplify app created for static hosting.
- Lambda function deployed for backend (`arm64` architecture).

### Changed
- Lambda function architecture from `x86` to `arm64` (cheaper for simple operations).
- AWS resources to be deployed in `us-east-1` instead of `us-east-2` (more resources available in former).


