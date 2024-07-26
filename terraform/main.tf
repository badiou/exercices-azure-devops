provider "azurerm" {
  tenant_id       = "${var.tenant_id}"
  subscription_id = "${var.subscription_id}"
  client_id       = "${var.client_id}"
  client_secret   = "${var.client_secret}"
  features {}
}
# terraform {
#   backend "azurerm" {
#     storage_account_name = ""
#     container_name       = ""
#     key                  = ""
#     access_key           = ""
#   }
# }
module "resource_group" {
  source               = "./modules/resource_group"
  resource_group       = "${var.resource_group}"
  location             = "${var.location}"
}

module "app_service" {
  source          = "./modules/appservice"
  location        = var.location
  application_type = "${var.application_type}"
  resource_type   = "AppService"
  resource_group  = module.resource_group.resource_group_name
  tags = {
    environment = "test"
    department  = "IT"
  }
}
