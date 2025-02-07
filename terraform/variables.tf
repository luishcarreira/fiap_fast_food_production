# AWS ACCOUNT SETTINGS

variable "access_key" {
  description = "Aws access key"
  type        = string
  default     = ""
}

variable "secret_key" {
  description = "Aws secret key"
  type        = string
  default     = ""
}

variable "account_id" {
  description = "Aws account id"
  type        = string
  default     = ""
}

variable "session_token" {
  description = "Aws session token"
  type        = string
  default     = ""
}

variable "aws_region" {
  description = "Região dos recursos"
  type        = string
  default     = "us-east-1"
}

# SQS QUEUE
variable "queue_name" {
  description = "Nome da fila SQS"
  type        = string
  default     = "fiap_fast_food_order_for_production"
}

variable "visibility_timeout" {
  description = "Tempo limite de visibilidade da mensagem (segundos)"
  type        = number
  default     = 30
}

variable "message_retention_seconds" {
  description = "Tempo máximo de retenção de mensagens na fila (segundos)"
  type        = number
  default     = 86400 # 1 dia
}

variable "delay_seconds" {
  description = "Tempo de atraso para mensagens (segundos)"
  type        = number
  default     = 0
}

variable "receive_wait_time" {
  description = "Tempo de espera para polling (segundos)"
  type        = number
  default     = 20
}

variable "enable_dlq" {
  description = "Habilitar Dead Letter Queue (DLQ)"
  type        = bool
  default     = false
}

variable "max_receive_count" {
  description = "Máximo de tentativas antes de enviar para a DLQ"
  type        = number
  default     = 5
}

variable "dlq_message_retention_seconds" {
  description = "Tempo de retenção de mensagens na DLQ (segundos)"
  type        = number
  default     = 1209600 # 14 dias
}