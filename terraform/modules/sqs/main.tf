resource "aws_sqs_queue" "queue" {
  name                        = var.queue_name
  visibility_timeout_seconds  = var.visibility_timeout
  message_retention_seconds   = var.message_retention_seconds
  delay_seconds               = var.delay_seconds
  receive_wait_time_seconds   = var.receive_wait_time

  redrive_policy = jsonencode({
    deadLetterTargetArn = aws_sqs_queue.dlq.arn
    maxReceiveCount     = var.max_receive_count
  })
}

resource "aws_sqs_queue" "dlq" {
  name = "${var.queue_name}-dlq"
}

resource "aws_sqs_queue_redrive_allow_policy" "queue_redrive_allow_policy" {
  queue_url = aws_sqs_queue.queue.id

  redrive_allow_policy = jsonencode({
    redrivePermission = "byQueue",
    sourceQueueArns   = [aws_sqs_queue.queue.arn]
  })
}