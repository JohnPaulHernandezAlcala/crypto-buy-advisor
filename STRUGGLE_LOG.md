# 🧠 Struggle Log

A running journal of challenges, missteps, and lessons learned while building this project which includes actual time taken vs. expected time. While certifications, labs, and tools like GPT make cloud development feel seamless, real-world projects reveal the messy truth: configuration issues, subtle bugs, silent permission errors, and the occasional hallucination or overly simplified advice from AI.

This log documents that journey. Each entry highlights what I was trying to do, what went wrong, how I fixed it, and what I learned because showing the *process* is just as important as showing the *result*.

## 📅 2025-06-13
**Task**: Lambda function backend creation and integration with frontend, api gateway, and secret manager
- Do as many as possible backend and frontend functions and integrations locally, then push to github for pushing to AWS via amplify/codepipeline; from here, integrate api gateway and secrets manager.

**Estimated Time**:  
- 3 hours (based on AWS documentation/tutorials)

**Actual Time**:  
- 14 hours

**What Went Wrong**:  
- lambda function very pick about how zip file with python code and packages are exported to it.


**How I Solved It**:  
- Finally figured out that codepipeline zips the files in an artifact out; so contrary to documentation, zipping of files is not necessary.

---

## 📅 2025-06-11 to 2025-06-12
**Task**: Set up local environment using VS Code to test frontend and backend integration before pushing to Amplify/CodePipeline
- Set up local environment, so I can get everything working together before pushing via Git to save costs on Amplify/CodePipeline

**Estimated Time**:  
- 45 minutes (based on AWS documentation/tutorials)

**Actual Time**:  
- 4 hours

**What Went Wrong**:  
- Packages installed from requirements.txt were not being recongized
- Virtual environment would not set into place even though the UI in VS Code showed it was


**How I Solved It**:  
- Restore terminal to command prompt because trying to default it to bash was causing path confusions and errors
- Deleted onld virutal environment and created a new one
- Closed and opened the repo in VS Code from the "Open Folder" option at the parent level crypto-buy-advisor; otherwise venv was not detected
- Set default interperter to "..\crypto-buy-advisor\.venv-crypto-buy-advisor\Scripts\python.exe"
- Reinstalled requirements.txt file

---

---

## 📅 2025-06-10
**Task**: Fine tune AWS CodePipeline with Webhook event filter
- Set up continuous deployment (CD) for Lambda backend using CodePipeline but only for lambda_function.py to keep cost low

**Estimated Time**:  
- 10 minutes (based on AWS documentation/tutorials)

**Actual Time**:  
- 1.5 hours

**What Went Wrong**:  
- Had the filepath defined correctly, but I wasn't patient; so I thought it was incorrect and kept trying new patterns.

**How I Solved It**:  
- Used `"backend/**"` and went to read docs when I realized this path worked.  
- Set the acutal path to:  
  `backend/lambda_function.py`

---

## 📅 2025-06-07 to 2025-06-09  
**Task**: Deploy AWS CodeBuild/CodePipeline  
- Set up continuous deployment (CD) for a Lambda backend using CodeBuild and CodePipeline.

**Estimated Time**:  
- 30 minutes (based on AWS documentation/tutorials)

**Actual Time**:  
- 15 hours

**What Went Wrong**:  
- Lambda function deployment failed during build due to:  
  `ImportError: cannot import module 'lambda_function'`

**How I Solved It**:  
- Used `"**/*"` to recursively include all files in the `package/` directory for zipping.  
- Set the Lambda handler to match the full module path:  
  `backend.package.lambda_function.lambda_handler`

**Lessons Learned**:  
- ZIP files are not strictly necessary when exporting a Lambda function from CodeBuild.  
- Some unofficial sources incorrectly claim only ZIPs work — always double-check with official AWS documentation.

---

## 📅 2025-06-06  
**Task**: Deploy AWS CodeBuild/CodePipeline  
- Continue Lambda backend deployment with CodeBuild and CodePipeline.

**Estimated Time**:  
- 30 minutes

**Actual Time**:  
- 5 hours

**What Went Wrong**:  
- Build failed silently due to ZIP command permission errors.  
- Lambda function deployment failed again due to import errors.

**How I Solved It**:

**Silent permissions error**:
- Moved ZIP creation to occur *inside* the directory before moving it:  
  ```bash
  zip -r function.zip .
  mv function.zip ..
  ```
---

## 📅 2025-06-05  
**Task**: Deploy AWS Amplify App  
- Deploy a static HTML/CSS frontend to AWS Amplify.

**Estimated Time**:  
- 30 minutes (based on AWS documentation/tutorials)

**Actual Time**:  
- 5 hours

**What Went Wrong**:  
- Started with Amplify Gen 2, which expects the backend and frontend to be tightly coupled using Amplify services.  
- My project had a decoupled backend managed via CodeBuild/CodePipeline.  
- Included a Gen 2-style `amplify.yml` file with keys like `applications:` and `appBackend:`, which broke the build.

**How I Solved It**:  
- Deleted the Gen 2 Amplify app entirely.  
- Created a new Gen 1 app with an empty backend placeholder.  
- Rebuilt the `amplify.yml` file without any Gen 2-specific keys.

**Lessons Learned**:  
- Amplify Gen 2 is intended for full-stack apps using Amplify-managed backends.  
- Amplify Gen 1 is the right choice for frontend-only or decoupled architectures.  
- Don't hesitate to start over if the setup gets too tangled.  
- Amplify app names can be reused even after deletion, making resets less painful.

