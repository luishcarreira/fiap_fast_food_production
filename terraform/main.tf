terraform {
  required_version = ">=1.3.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region     = var.aws_region
  access_key = var.access_key
  secret_key = var.secret_key
  token      = var.session_token
}

module "sqs" {
  source = "./modules/sqs"

  queue_name                    = var.queue_name
  visibility_timeout            = var.visibility_timeout
  message_retention_seconds     = var.message_retention_seconds
  delay_seconds                 = var.delay_seconds
  receive_wait_time             = var.receive_wait_time
  enable_dlq                    = var.enable_dlq
  max_receive_count             = var.max_receive_count
  dlq_message_retention_seconds = var.dlq_message_retention_seconds
}