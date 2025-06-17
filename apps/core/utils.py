from config.supabase import supabase
import logging

logger = logging.getLogger(__name__)

def send_email(to_email, subject, message):
    """
    Send an email using Supabase's email service
    """
    try:
        logger.info(f"Attempting to send email to {to_email}")
        
        response = supabase.functions.invoke(
            'send-email',
            invoke_options={
                'body': {
                    'to': to_email,
                    'subject': subject,
                    'message': message
                }
            }
        )
        
        logger.info(f"Supabase function response: {response}")
        
        if hasattr(response, 'error'):
            logger.error(f"Error from Supabase function: {response.error}")
            return False
            
        return True
    except Exception as e:
        logger.error(f"Error sending email: {str(e)}")
        return False 