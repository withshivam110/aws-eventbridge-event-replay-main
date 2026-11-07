import json
import logging
import os
from datetime import datetime

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def lambda_handler(event, context):
    try:
        logger.info(f"Received Event: {json.dumps(event, default=str)}")
        
        event_id = event.get('id', 'unknown')
        event_source = event.get('source', 'unknown')
        detail_type = event.get('detail-type', 'unknown')
        event_time = event.get('time', datetime.utcnow().isoformat())
        detail = event.get('detail', {})
        
        # EventBridge injects 'replay-name' during replay operations
        replay_name = event.get('replay-name')
        is_replay = bool(replay_name)
        
        if is_replay:
            logger.info(f"*** REPLAY EVENT *** ReplayName={replay_name} EventID={event_id} Time={event_time}")
        else:
            logger.info(f"*** REALTIME EVENT *** EventID={event_id} Time={event_time}")
        
        if event_source == 'myapp.orders':
            order_id = detail.get('orderId', 'unknown')
            amount = detail.get('amount', 0)
            logger.info(f"[ORDER] ID={order_id} Amount=${amount} Replay={is_replay}")
        elif event_source == 'myapp.users':
            user_id = detail.get('userId', 'unknown')
            email = detail.get('email', 'unknown')
            logger.info(f"[USER] ID={user_id} Email={email} Replay={is_replay}")
        else:
            logger.info(f"[GENERIC] Source={event_source} Type={detail_type}")

        return {
            'statusCode': 200,
            'body': json.dumps({
                'message': 'Processed successfully',
                'eventId': event_id,
                'isReplay': is_replay,
                'replayName': replay_name
            })
        }
    except Exception as err:
        logger.error(f"Error: {str(err)}", exc_info=True)
        raise err
