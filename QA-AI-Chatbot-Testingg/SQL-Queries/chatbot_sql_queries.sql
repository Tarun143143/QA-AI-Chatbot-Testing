-- Find all chatbot conversations where user input contains 'error'
SELECT * FROM chatbot_logs WHERE user_message LIKE '%error%';
-- Count number of chatbot responses containing 'I don't understand'
SELECT COUNT(*) FROM chatbot_logs WHERE bot_response = 'I don't understand';