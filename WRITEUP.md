# Deployment Choice: Azure App Service vs Virtual Machine

For this project, Azure App Service was selected as the deployment platform instead of a Virtual Machine.

Azure App Service is a Platform-as-a-Service (PaaS) solution that simplifies application deployment and management. It automatically handles server maintenance, operating system updates, and scaling, allowing developers to focus primarily on application development.

In contrast, deploying the application on a Virtual Machine would require manual configuration of the operating system, installation of dependencies, server setup, and ongoing maintenance. This approach introduces additional administrative overhead.

Azure App Service also integrates seamlessly with GitHub for continuous deployment and provides built-in monitoring tools such as Log Stream and Application Insights.

Therefore, Azure App Service was chosen because it provides a simpler, more scalable, and more efficient deployment environment for the CMS application.
