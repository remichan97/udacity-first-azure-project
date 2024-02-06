# Write-up Template

### Analyze, choose, and justify the appropriate resource option for deploying the app.

Background: an Article CMS app that provide CRUD for articles needed to deploy to Azure, a factor to add to the consideration is that the overall price for Database powering the app 
are free as the database is using the free offering from Azure as of writing

**Running cost:** Both VM and App Services provides a low tier (B1lS for VM, and F1 for App Services). Given the $0.01 per hour price for the lowest tier of the VM, while the App Services lowest tier can be run for free, the App Service is the obvious choice for the project for the Cost factor
 
**Scalability:** VM clearly won this as the resources that can be allocated for instances of VM are much higher. This is not the case with App Services, as we can scale up to 14GB of memory with 4 CPU for each running instance . However, as the deploying app isn't that complex nor require significant processing power, App Service is my choice of service.

**Availability:** Both have excellent availability, as they can always be available 24/7, nor can be stopped, restarted if there is something wrong with the app. This is a draw for both service for this factor, however, the final factor is what makes me have the final choice on this.

**Workflow:** For VM, in order to have the app deployed, several manual steps are required to make sure the app is running, and visible on the Internet. With App Services, the initial setup are much less headache, other than setting up suitable environment variables, the app is ready and can be accesses much faster than in VM. 

With all of that factor, I selected App Services for the deployment of the app for the simplicity of deployment, and the running cost of the app itself comparing to running on a VM

### Assess app changes that would change your decision.

Other than switching the configuration saving storage from using a config file to using Azure Key Vault, there is no other factor affecting the choice of deployment other than the above-mentioned