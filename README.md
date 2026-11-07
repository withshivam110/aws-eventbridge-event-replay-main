# AWS EventBridge Archive & Replay Demonstration

An event-driven architecture project demonstrating how to capture, archive, filter, and replay events using **Amazon EventBridge**, **AWS Lambda**, **Amazon S3**, and **IAM**.

## Architecture Overview
1. **Custom Event Bus**: Isolates demo events from production traffic.
2. **Event Archive**: Automatically captures and stores critical events with selective filtering and configurable retention.
3. **AWS Lambda Processor**: Processes events in real time and detects replayed payloads using the `replay-name` metadata field.
4. **Replay Automation**: CLI scripts and CloudWatch monitoring to trigger and track historical event replays.

## Prerequisites
- AWS CLI v2 configured with appropriate permissions
- Python 3.9+

## Deployment
Run the automated deployment script:
\`\`\`bash
bash deploy.sh
\`\`\`
