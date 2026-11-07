# Replay automation script
ARCHIVE_NAME=$1
HOURS_BACK=${2:-1}

if [ -z "$ARCHIVE_NAME" ]; then
    echo "Usage: $0 <archive-name> [hours-back]"
    exit 1
fi

# Calculate replay time window
START_TIME=$(date -u -d "${HOURS_BACK} hours ago" +%Y-%m-%dT%H:%M:%SZ)
END_TIME=$(date -u +%Y-%m-%dT%H:%M:%SZ)

# Generate replay name
REPLAY_NAME="auto-replay-$(date +%Y%m%d-%H%M%S)"

echo "Starting automated replay:"
echo "Archive: ${ARCHIVE_NAME}"
echo "Time window: ${START_TIME} to ${END_TIME}"
echo "Replay name: ${REPLAY_NAME}"

# Start replay
aws events start-replay \
    --replay-name ${REPLAY_NAME} \
    --event-source-arn $(aws events describe-archive --archive-name ${ARCHIVE_NAME} --query 'SourceArn' --output text) \
    --event-start-time ${START_TIME} \
    --event-end-time ${END_TIME} \
    --destination '{
      "Arn": "'$(aws events describe-archive --archive-name ${ARCHIVE_NAME} --query 'SourceArn' --output text)'"
    }'

echo "Replay started successfully: ${REPLAY_NAME}"
