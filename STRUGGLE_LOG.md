Struggle Log


2025-06-06

Task: Deploy AWS CodeBuild/CodePipeline
- Deploy a lambda function backend Continuous Deployment (CD) using CodeBuild/CodePipeline.
Estimated Time:
- 30 minutes (based on AWS documentation/tutorials).
Actual Time:
- 6 hours
What Went Wrong:
- Build failed because ZIP command triggered silent permissions errors
- Lambda function deployment failed build because import module 'lambda_function' could not be found
How I Solved It: 
- Created ZIP file first then moved it to backend/

Code: 
      'zip -r ../function.zip .'

to
      - zip -r function.zip .
      - mv function.zip ..
  
Lessons Learned:
- ZIP can cause silent permissions errors with "../"
- CodePipe needs to find files relative to the repo root
- Difference between "zip -r function.zip ." and "zip -r function.zip *" is latter excludes zip directory
- Lambda Function Console UI doesn't display files greater than 3 MB
- Lambda Function Console handler must match location of file (i.e. backend.lambda_function.lambda_handler since zip file is in backend/)

----

2025-06-05

Task: Deploy AWS Amplify App
- Deploy a static HTML/CSS frontend to AWS Amplify.
Estimated Time:
- 30 minutes (based on AWS documentation/tutorials).
Actual Time:
- 2 hours
What Went Wrong:
Amplify failed build because:
- Gen 2 expected backend and frontend to be tightly coupled using Amplify service (backend was designed to be decoupled and for use with CodeBuild/CodePipeline)
- Created incorrect Amplify yml file that had gen 2 keys ("applications:" and "appBackend:") 
How I Solved It: 
- Deleted gen 2 app and built new app using gen 1 with empty backend created as placeholder
- Ensure no gen 2 keys 
Lessons Learned:
- Amplify Gen 2 is for an app that uses Amplify services for front and backend
- Amplify Gen 1 is for frontend-only apps
- Try debugging only for a bit of time before deleting whole app and starting over
- Amplify app name can be reused even after deletion
