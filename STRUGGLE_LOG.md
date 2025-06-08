Struggle Log


2025-06-06 Deploy AWS CodeBuild/CodePipeline.
Task: 
- Deploy a lambda function backend Continuous Deployment (CD) using CodeBuild/CodePipeline.
Estimated Time:
- 30 minutes (based on AWS documentation/tutorials).
Actual Time:
- 3 hours
What Went Wrong:
- Lambda function deployment failed build because
How I Solved It: 
- Deleted gen 2 app and built new app using gen 1 with empty backend created as placeholder
- Ensure no gen 2 keys 
Lessons Learned:
- Amplify Gen 2 is for an app that uses Amplify services for front and backend
- Amplify Gen 1 is for frontend-only apps
- Try debugging only for a bit of time before deleting whole app and starting over
- Amplify app name can be reused even after deletion

----

2025-06-05 Deploy AWS Amplify App
Task: 
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
