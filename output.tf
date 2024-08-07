output "api_arn" {
  value = "${aws_api_gateway_rest_api.api.execution_arn}/items"
}

output "api_url" {
  value = "${aws_api_gateway_deployment.api_deployment.invoke_url}/items"
}
