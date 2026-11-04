# steps: 
#     - name: Deploy
#       run: |
#         echo "Deploying the application..."
#         echo "Deployment complete!"
#         echo "Deployment complete!"

# Variables vs Secrets
APP_NAME="MyApp" # Variable
APP_ENV="production" # Variable
APP_PASSWORD="SuperSecretPassword" # Secret
AAP_TOKEN="SuperSecretToken" # Secret

# ${{}} - Expression Syntax
# github - Context name
# actor - Property inside the context