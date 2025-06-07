Struggle Log

2025-06-06 Deploy AWS Amplify App
Task: Deploy a React frontend to AWS Amplify.Estimated Time: 30 minutes (based on AWS documentation/tutorials).Actual Time: 3 hours 45 minutes.What Went Wrong:
Amplify failed build: incorrect artifact path.
IAM role misconfiguration blocked S3 uploads.
Initial guidance from GPT missed nuances in Amplify build settings.
How I Solved It:
Manually set build artifact path in amplify.yml.
Adjusted IAM role permissions to allow S3 access.
Cross-checked Amplify docs instead of relying solely on AI suggestions.
Lessons Learned:
Always validate artifact paths manually.
Never skip reviewing IAM permissions.
Use AI tools as a guide, but verify against official docs.
