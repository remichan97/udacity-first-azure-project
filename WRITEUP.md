# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

Here is my deployment of choice when deploying the app:
- The chosen deployment of choice is App Service, as the app, at the current state, is a simple CRUD app for managing articles, as such, there is not much computing powers involved when performing such tasks
- Easier to setup the app, there is no manual setup or having to go through chanegs that apply system-wide, aside from setting up 3 environment variables (Application Configurations in App Services)

### Assess app changes that would change your decision.

Other than switching the configuration saving storage from using a config file to using Azure Key Vault, there is no other factor affecting the choice of deployment other than the above-mentioned