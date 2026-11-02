"""GitHub Events that trigger workflows or Automatic Workflow Triggers""" 
# Starts when a repo event occurs (Ex: Push to main branch, Pull Request, Issue creation, etc.)
# on:
#     push:
#         branches:
#             - main

"""Schedule (starts at a configured time)"""
# on
#   schedule:
#       - cron: '0 2 * * *' # Every day at 2am UTC

"""Manual (triggered by a user)"""
# on:
#     workflow_dispatch:

""" External Event (triggered by an external application)"""
# on:
#     repository_dispatch:
#       types:
#         - deploy-application